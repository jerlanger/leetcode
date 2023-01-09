import re
import timeit
import numpy as np


class Solution:

    # Init Solution
    def minPartitions(self, n: str) -> int:
        ans = re.findall(r'\d', n)
        return max([int(i) for i in ans])

    # Revise 1
    def minPartitions2(self, n: str):
        return int(max(n))

    def timing(self, n: int):

        results = {"Solution 1": np.mean(timeit.repeat(lambda: self.minPartitions(n=str(n)))),
                   "Solution 2": np.mean(timeit.repeat(lambda: self.minPartitions2(n=str(n))))
                   }

        return results


answer = Solution()

for n in [32, 82734, 27346209830709182346]:
    print(answer.minPartitions2(str(n)))
    print(answer.timing(n))

