import requests
import pandas as pd
from time import sleep


def fetch_btc_blocks():
    base_url = "https://explorer.cloverpool.com/api/btc/blocks"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }

    # 获取第一页数据并确定总页数
    first_page = requests.get(f"{base_url}?page=1&per_page=25", headers=headers).json()
    total_pages = first_page['last_page']

    all_data = []
    # 添加第一页数据
    all_data.extend(first_page['data'])

    print(f"开始爬取，共{total_pages}页数据...")

    # 从第二页开始爬取
    for page in range(2, total_pages + 1):
        try:
            url = f"{base_url}?page={page}&per_page=25"
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 检查HTTP错误

            data = response.json()
            all_data.extend(data['data'])

            # 显示进度
            if page % 10 == 0:
                print(f"已爬取第{page}/{total_pages}页...")

            # 礼貌性延迟
            sleep(0.5)

        except Exception as e:
            print(f"第{page}页爬取失败: {str(e)}")
            continue

    print("所有数据爬取完成！")
    return all_data


# 执行爬取
block_data = fetch_btc_blocks()

# 转换为DataFrame并保存
if block_data:
    df = pd.DataFrame(block_data)
    # 重命名列（根据实际JSON键名调整）
    df = df.rename(columns={
        "height": "区块高度",
        "hash": "区块哈希",
        "time": "出块时间",
        "tx_count": "交易数量",
        "size": "区块大小(MB)",
        "miner": "矿池",
        "reward": "区块奖励(BTC)",
        "fees": "手续费(BTC)"
    })

    # 保存到CSV
    df.to_csv("btc_blocks_data.csv", index=False)
    print(f"数据已保存到btc_blocks_data.csv，共{len(df)}条记录")
else:
    print("未获取到数据")