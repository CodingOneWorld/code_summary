# -*- coding: utf-8 -*-



def transfer(a):
    m=''
    while a>0:
        m+=str(a%2)  #a对2求余，添加到字符串m最后
        a=a//2
    print(m[::-1])   #反向输出


transfer(10)