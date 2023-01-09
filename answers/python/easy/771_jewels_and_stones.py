import re

class Solution:

    # Init

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        target = re.findall(r'', stones)
        i = 0

        for w in target:
            if w in jewels:
                i += 1
        return i

    # Revise

    def numJewelsInStones2(self, jewels: str, stones: str):
        return sum(map(jewels.count, stones))

jewels = "aA"
stones = "aAAbbbb"

answer = Solution()
print(answer.numJewelsInStones2(jewels=jewels, stones=stones))
