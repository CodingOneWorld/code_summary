# 字典使用方法

dic={}

# 写入数据
dic[1]='a'
dic[2]='b'
dic[3]='c'

# 输出
print(list(dic.keys()))  # [1, 2, 3]
print(list(dic.values())) # ['a', 'b', 'c']

print(dic.get(1,'z'))   # 返回指定键的值，如果键不在字典中返回 default 设置的默认值