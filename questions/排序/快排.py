# -*- coding: utf-8 -*-



# 1 递归
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 2
# coding=utf-8
def quick_sort(array, start, end):
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        while array[right] >= mid_data and left < right:
            right -= 1
        array[left] = array[right]
        while array[left] < mid_data and left < right:
            left += 1
        array[right] = array[left]
    array[left] = mid_data
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)

# 3 算法导论中的快排
def quick_sort(nums, left, right):
    if left < right:
        partitionIndex = partition(nums, left, right)
        quick_sort(nums, left, partitionIndex - 1)
        quick_sort(nums, partitionIndex + 1, right)

def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    for i in range(index, right + 1):
        if nums[i] < nums[pivot]:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    # swap index-1 and pivot
    nums[pivot], nums[index - 1] = nums[index - 1], nums[pivot]
    return index - 1





# 递归解法
def quick_sort(nums):
    if len(nums)<2:
        return nums
    else:
        tem=nums[0]
        left=[i for i in nums if i<=tem]
        right=[i for i in nums if i>tem]
        return quick_sort(left)+[tem]+quick_sort(right)

# 迭代解法





if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    quick_sort(array, 0, len(array) - 1)
    print(array)

