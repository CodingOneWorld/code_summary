# -*- coding: utf-8 -*-

myList = ['a','b','c']
sample_list = ['a',1,('a','b')]

# 取值
value_start = sample_list[0]
end_value = sample_list[-1]

# 删除
del sample_list[0]

# 遍历
for element in sample_list:
  print(element)


# 使用固定值初始化列表
initial_value = 0
list_length = 5
sample_list = [ initial_value for i in range(10)]
sample_list = [initial_value]*list_length
# sample_list ==[0,0,0,0,0]

# 创建连续的list
L = range(1,5)   #即 L=[1,2,3,4],不含最后一个元素
L = range(1, 10, 2) #即 L=[1, 3, 5, 7, 9]

'''
下标：按下标读写，就当作数组处理
以0开始，有负下标的使用
0第一个元素，-1最后一个元素，
-len第一个元 素，len-1最后一个元素


# list的方法
var=10
L.append(var)  #追加元素
L.insert(index,var)
L.pop(var)   #返回最后一个元素，并从list中删除之
L.remove(var)  #删除第一次出现的该元素
L.count(var)  #该元素在列表中出现的个数
L.index(var)  #该元素的位置,无则抛异常
L.extend(list) #追加list，即合并list到L上
L.sort()    #排序   原数组操作，没有返回值
L.reverse()   #倒序   原数组操作，没有返回值
list 操作符:,+,*，关键字del
a[1:]    #片段操作符，用于子list的提取
[1,2]+[3,4] #为[1,2,3,4]。同extend()
[2]*4    #为[2,2,2,2]
del L[1]  #删除指定下标的元素
del L[1:3] #删除指定下标范围的元素
'''

# list的复制
L1 = L   #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
L1 = L[:]  #L1为L的克隆，即另一个拷贝。

