# Init Answer

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for number in nums:
            ans.append(nums[number])

        return(ans)

# Revise Answer

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return[nums[i] for i in nums]