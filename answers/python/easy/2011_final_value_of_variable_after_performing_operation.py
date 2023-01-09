class Solution:
    def finalValueAfterOperations(self, operations: list[str], x=0):
        for op in operations:
            if '+' in op:
                x += 1
            elif '-' in op:
                x -= 1
            else:
                pass
        return x


answer = Solution()
operations = [["--X", "X++", "X++"], ["++X","++X","X++"], ["X++","++X","--X","X--"]]

for case in operations:
    print(answer.finalValueAfterOperations(operations=case))
