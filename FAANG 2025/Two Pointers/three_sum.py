class Solution:
    def threeSum(nums):
        nums.sort()
        target = 0
        triplets = set()
        for idx in range(len(nums)-2):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[idx] + nums[left] + nums[right]
                if(currSum < target):
                    left += 1
                elif(currSum > target):
                    right -= 1
                else :
                    triplet = tuple([nums[idx], nums[left], nums[right]])
                    triplets.add(triplet)
                    left += 1
                    right -= 1
        return list(triplets)



            
        