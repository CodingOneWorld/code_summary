

# 寻找一个数
def binary_search(nums,target):
    left =0
    right=len(nums)-1

    while(left<=right):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1

    return -1
# 左侧边界
def left_bound(nums,target):
    if len(nums)==0:
        return -1
    left=0
    right=len(nums)

    while (left<right):
        mid=(left+right)//2
        if nums[mid]==target:
            right=mid
        elif nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid

    if left ==len(nums):
        return -1
    return left if nums[left]==target else -1
# 右侧边界