class Solution:

    # Init

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []

        for i in range(0,n):
            ans.append(nums[i])
            ans.append(nums[n+i])

        return ans


nums = [[2,5,1,3,4,7], [1,2,3,4,4,3,2,1], [1,1,2,2]]
n = [3,4,2]

answer = Solution()

for i in range(0,len(n)):
    print(answer.shuffle(nums=nums[i], n=n[i]))