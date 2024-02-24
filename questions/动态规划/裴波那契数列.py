# -*- coding: utf-8 -*-

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        f=[0 for i in range(n+1)]
        print(f)
        f[0]=0
        f[1]=1
        for i in range(2,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]

if __name__ == '__main__':
    s=Solution()
    print(s.fib(4))