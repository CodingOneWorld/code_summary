import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates

# 设置中文字体显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def fetch_recent_btc_blocks():
    """
    爬取最近一个月的比特币区块数据
    """
    base_url = "https://explorer.cloverpool.com/api/btc/blocks"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://explorer.cloverpool.com/zh-CN/btc/blocks"
    }

    # 计算一个月前的日期
    one_month_ago = datetime.utcnow() - timedelta(days=30)
    print(f"开始爬取最近一个月（自 {one_month_ago.strftime('%Y-%m-%d')} 起）的比特币区块数据...")

    all_data = []
    page = 1
    last_block_time = datetime.utcnow()
    max_pages = 50  # 安全限制，防止无限循环

    while (last_block_time > one_month_ago) and (page <= max_pages):
        try:
            # 添加随机延迟避免被封
            time.sleep(np.random.uniform(0.8, 1.5))

            url = f"{base_url}?page={page}&per_page=25"
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()

            # 检查是否还有数据
            if not data.get('data'):
                print(f"第 {page} 页无数据，爬取结束")
                break

            # 处理每个区块的时间
            for block in data['data']:
                # 将时间字符串转换为datetime对象
                block_time = datetime.strptime(block['time'], "%Y-%m-%d %H:%M:%S")
                block['block_time'] = block_time  # 添加datetime对象到数据中

                # 记录最后区块的时间
                if block_time < last_block_time:
                    last_block_time = block_time

                # 如果区块时间早于一个月前，停止收集
                if block_time < one_month_ago:
                    break

            # 添加当前页数据
            all_data.extend(data['data'])
            print(
                f"已爬取第 {page} 页，最新区块时间: {data['data'][0]['time']}，最旧区块时间: {data['data'][-1]['time']}")

            # 检查是否达到时间边界
            if last_block_time < one_month_ago:
                print(f"已达到时间边界（{one_month_ago.strftime('%Y-%m-%d')}），爬取结束")
                break

            page += 1

        except Exception as e:
            print(f"爬取第 {page} 页时出错: {str(e)}")
            break

    print(f"\n爬取完成！共获取 {len(all_data)} 个区块数据")
    return all_data


def process_block_data(block_data):
    """
    处理区块数据并返回DataFrame
    """
    # 创建DataFrame
    df = pd.DataFrame(block_data)

    # 转换时间列为datetime
    df['block_time'] = pd.to_datetime(df['time'])

    # 重命名列
    column_mapping = {
        "height": "区块高度",
        "hash": "区块哈希",
        "time": "出块时间",
        "tx_count": "交易数量",
        "size": "区块大小(B)",
        "miner": "矿池",
        "reward": "区块奖励(BTC)",
        "fees": "手续费(BTC)"
    }
    df = df.rename(columns=column_mapping)

    # 转换数值类型
    df['区块大小(MB)'] = df['区块大小(B)'].astype(float) / (1024 * 1024)
    df['区块奖励(BTC)'] = df['区块奖励(BTC)'].astype(float)
    df['手续费(BTC)'] = df['手续费(BTC)'].astype(float)

    # 添加日期列
    df['日期'] = df['出块时间'].str.split().str[0]

    # 按日期分组计算每日数据
    daily_stats = df.groupby('日期').agg(
        区块数量=('区块高度', 'count'),
        总交易量=('交易数量', 'sum'),
        平均区块大小_MB=('区块大小(MB)', 'mean'),
        总区块奖励_BTC=('区块奖励(BTC)', 'sum'),
        总手续费_BTC=('手续费(BTC)', 'sum')
    ).reset_index()

    daily_stats['日期'] = pd.to_datetime(daily_stats['日期'])

    return df, daily_stats


def save_and_visualize_data(df, daily_stats):
    """
    保存数据并生成可视化图表
    """
    # 创建输出文件夹
    os.makedirs('btc_blocks_data', exist_ok=True)

    # 保存原始数据
    csv_path = os.path.join('btc_blocks_data', 'recent_btc_blocks.csv')
    df.to_csv(csv_path, index=False)
    print(f"原始数据已保存至: {csv_path}")

    # 保存每日统计数据
    daily_csv_path = os.path.join('btc_blocks_data', 'daily_btc_stats.csv')
    daily_stats.to_csv(daily_csv_path, index=False)
    print(f"每日统计数据已保存至: {daily_csv_path}")

    # 生成图表
    print("生成数据可视化图表...")
    plt.figure(figsize=(15, 12))

    # 1. 每日区块数量
    plt.subplot(3, 2, 1)
    plt.plot(daily_stats['日期'], daily_stats['区块数量'], 'o-', color='royalblue')
    plt.title('每日区块数量', fontsize=12)
    plt.xlabel('日期')
    plt.ylabel('数量')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.grid(alpha=0.3)

    # 2. 每日总交易量
    plt.subplot(3, 2, 2)
    plt.bar(daily_stats['日期'], daily_stats['总交易量'], color='seagreen', alpha=0.7)
    plt.title('每日总交易量', fontsize=12)
    plt.xlabel('日期')
    plt.ylabel('交易数量')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.grid(alpha=0.3)

    # 3. 平均区块大小
    plt.subplot(3, 2, 3)
    plt.plot(daily_stats['日期'], daily_stats['平均区块大小_MB'], 's-', color='darkorange')
    plt.title('每日平均区块大小 (MB)', fontsize=12)
    plt.xlabel('日期')
    plt.ylabel('MB')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.grid(alpha=0.3)

    # 4. 区块奖励和手续费
    plt.subplot(3, 2, 4)
    width = 0.35
    dates = daily_stats['日期']
    plt.bar(dates, daily_stats['总区块奖励_BTC'], width, label='区块奖励', color='gold')
    plt.bar(dates + pd.Timedelta(days=width), daily_stats['总手续费_BTC'], width, label='手续费', color='purple')
    plt.title('每日区块奖励和手续费 (BTC)', fontsize=12)
    plt.xlabel('日期')
    plt.ylabel('BTC')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.grid(alpha=0.3)

    # 5. 矿池分布
    plt.subplot(3, 1, 3)
    miner_counts = df['矿池'].value_counts().head(8)
    miner_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90,
                      colors=plt.cm.Paired(np.linspace(0, 1, len(miner_counts))))
    plt.title('矿池分布', fontsize=12)
    plt.ylabel('')

    plt.tight_layout()
    plt.savefig(os.path.join('btc_blocks_data', 'btc_blocks_analysis.png'), dpi=150)
    print(f"可视化图表已保存至: {os.path.join('btc_blocks_data', 'btc_blocks_analysis.png')}")

    # 显示图表
    plt.show()


def main():
    # 爬取数据
    block_data = fetch_recent_btc_blocks()

    if block_data:
        # 处理数据
        df, daily_stats = process_block_data(block_data)

        # 保存并可视化数据
        save_and_visualize_data(df, daily_stats)
    else:
        print("未获取到数据，请检查爬取过程")


if __name__ == "__main__":
    main()