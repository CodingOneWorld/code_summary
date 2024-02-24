# -*- coding: utf-8 -*-

# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


# 选择排序
def cal_smallest(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if smallest > nums[i]:
            smallest = nums[i]
            smallest_index = i
    return smallest_index


def select_sort(nums):

    new_arr=[]
    while nums:
        smallest = cal_smallest(nums)
        new_arr.append(nums.pop(smallest))
    return new_arr


nums = [3, 1, 4, 2]
res = bubble_sort(nums)
res = select_sort(nums)
print(res)
