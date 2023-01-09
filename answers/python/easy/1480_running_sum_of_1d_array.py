import timeit
import numpy as np

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        i = 1
        for n in nums:
            ans.append(sum(nums[:i]))
            i += 1
        return ans

    def runningSum2(self, nums: list[int]):
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i-1] + nums[i])
            i += 1
        return ans

    def timing(self, nums: list[int]):

        results = {"Solution 1": np.mean(timeit.repeat(lambda: self.runningSum(nums=nums))),
                   "Solution 2": np.mean(timeit.repeat(lambda: self.runningSum2(nums=nums)))
                   }

        return results


cases = [[1,2,3,4], [1,1,1,1,1], [3,1,2,10,1]]

answer = Solution()

for case in cases:
    print(answer.runningSum2(case))
    print(answer.timing(case))