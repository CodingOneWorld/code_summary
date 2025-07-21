import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求网页内容
url = 'https://explorer.cloverpool.com/zh-CN/btc/blocks'
response = requests.get(url)
html_content = response.content

# 解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到表格
table = soup.find('table')
rows = table.find_all('tr')

# 提取数据
data = []
for row in rows[1:]:  # 跳过表头
    cols = row.find_all('td')
    if len(cols) > 2:
        broadcaster = cols[1].text.strip()  # 假设播报方在第二列
        block_date = cols[2].text.strip()  # 爆块时间
        block_reward = cols[4].text.strip()  # 假设区块奖励在第三列
        fee = cols[6].text.strip()  # 假设手续费在第四列
        data.append([broadcaster, block_date,block_reward, fee])

# 创建DataFrame
df = pd.DataFrame(data, columns=['播报方', '爆块时间','区块奖励 (BTC)', '手续费 (BTC)'])

# 保存到Excel文件
df.to_excel('btc_blocks.xlsx', index=False)

print("数据已成功保存到 btc_blocks.xlsx 文件中。")