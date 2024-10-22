#Time - O(n) || Space - O(n)
def twoSum(nums, target):
        visitedIdx = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in visitedIdx:
                return[visitedIdx[difference], idx]
            visitedIdx[nums[idx]] = idx
        return []