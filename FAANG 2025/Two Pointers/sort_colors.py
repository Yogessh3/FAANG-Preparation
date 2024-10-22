#Time - O(N) || Space - O(1)
def sortColors(nums):
    leftIdx = 0
    for idx in range(len(nums)):
        if(nums[idx] == 0):
            nums[leftIdx], nums[idx] = nums[idx], nums[leftIdx]
            leftIdx += 1
    rightIdx = len(nums) - 1
    while rightIdx >= 0 and nums[rightIdx] == 2:
        rightIdx -= 1
    idx = 0
    while idx <= rightIdx :
        if(nums[idx] == 2):
            nums[rightIdx], nums[idx] = nums[idx], nums[rightIdx]
            while rightIdx >= 0 and nums[rightIdx] == 2:
                rightIdx -= 1
        idx += 1