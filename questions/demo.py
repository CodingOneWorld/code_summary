# -*- coding: utf-8 -*-

s='asd'

s=[i for i in s]

print(s)


nums=[1,2,3,6,5,4]

nums2=[i for i in nums if i>1]
print(sum(nums2))

nums2=nums[3:]


print(nums2.sort())
print(nums[3:])
print(nums2)


matrix=[[1,2,3],
 [4,5,6],
 [7,8,9]]

arr=matrix[0]
print(arr)

print(id(matrix))
print(id(arr))


num=[1,2,3]
print(sum(num[0:0]))


matrix=[[1,2,3],
 [4,5,6],
 [7,8,9]]
print(max(matrix))

print([[0]*5]*5)


l=[1]
l=None
if l:
 print('tag')


strs='cba'
print(sorted(strs))
print(''.join(sorted(strs)))