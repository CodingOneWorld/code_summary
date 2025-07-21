import requests
import pandas as pd
from datetime import datetime, timedelta


def scrape_btc_blocks():
    base_url = "https://explorer.cloverpool.com/api/v1/blocks?page={}&limit=100"
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    data = []
    page = 1

    while True:
        response = requests.get(base_url.format(page), headers={"User-Agent": "Mozilla/5.0"})
        blocks = response.json()['data']
        if not blocks: break

        for block in blocks:
            block_time = datetime.fromisoformat(block['timestamp'].replace('Z', '+00:00'))
            if block_time < start_date: return pd.DataFrame(data)
            data.append({
                "height": block['height'],
                "timestamp": block_time.strftime("%Y-%m-%d %H:%M:%S"),
                "transactions": block['tx_count'],
                "miner": block['miner']['name'],
                "size_kb": round(block['size'] / 1024, 1),
                "reward": block['reward'] / 10 ** 8
            })
        page += 1


df = scrape_btc_blocks()
df.to_csv("btc_blocks_last_month.csv", index=False)