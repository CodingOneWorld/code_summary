import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import datetime
import argparse
from time import sleep
import os


def scrape_cloverpool_blocks(target_date):
    """
    爬取指定日期的比特币区块数据
    :param target_date: 日期字符串 (格式: YYYY-MM-DD)
    :return: 包含区块数据的DataFrame
    """
    # 构造带日期参数的URL
    base_url = "https://explorer.cloverpool.com/zh-CN/btc/blocks"
    params = {'date': target_date}

    try:
        # 设置请求头模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        response = requests.get(base_url, params=params, headers=headers, timeout=30)
        response.raise_for_status()  # 检查HTTP错误

        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        if not table:
            raise ValueError(f"未找到表格数据，请检查日期 {target_date} 是否有区块")

        # 提取表头
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]

        # 提取表格数据
        rows = []
        for tr in table.find('tbody').find_all('tr'):
            row = [td.text.strip() for td in tr.find_all('td')]
            rows.append(row)

        # 创建DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # 添加爬取日期列
        df['爬取日期'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return df

    except Exception as e:
        print(f"爬取失败: {str(e)}")
        return pd.DataFrame()


def save_to_csv(df, filename=None):
    """
    保存DataFrame到CSV文件
    :param df: 包含区块数据的DataFrame
    :param filename: 自定义文件名 (可选)
    """
    if df.empty:
        print("无数据可保存")
        return

    # 生成默认文件名
    if not filename:
        date_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'btc_blocks_{date_str}.csv'

    # 确保文件名以.csv结尾
    if not filename.endswith('.csv'):
        filename += '.csv'

    # 保存到CSV
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"数据已保存至: {os.path.abspath(filename)}")
    print(f"共爬取 {len(df)} 条区块记录")


def main():
    """命令行入口函数"""
    # parser = argparse.ArgumentParser(description='Cloverpool比特币区块数据爬虫')
    # parser.add_argument('date', type=str, help='目标日期 (格式: YYYY-MM-DD)')
    # parser.add_argument('-o', '--output', type=str, help='输出文件名 (可选)')
    # args = parser.parse_args()

    date='2025-06-08'

    # 验证日期格式
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("错误: 日期格式应为 YYYY-MM-DD")
        return

    print(f"开始爬取 {date} 的比特币区块数据...")
    data = scrape_cloverpool_blocks(date)

    if not data.empty:
        save_to_csv(data, 'output.csv')


if __name__ == "__main__":
    main()