# Init Answer

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(i)

        for i in nums:
            ans.append(i)

        return (ans)

# Revise 1

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans.extend(ans)

        return(ans)

# Revise 2

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return(nums+nums)