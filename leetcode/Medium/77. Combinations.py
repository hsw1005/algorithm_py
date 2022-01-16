from itertools import combinations as combs


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #         def dfs(s, e):
        #             if s < e:
        #                 result.append([s, e])
        #                 return
        #             else:
        #                 for i in range(1, n+1):
        #                     for j in range(i, n):
        #                         dfs(i, j+1)

        #         result = []
        #         if n - k > 1:
        #             dfs(0, 0)
        #         elif n - k == 1:
        #             result.append([n])
        #             result.append([k])
        #         elif n - k == 0:
        #             result.append([n])

        #         return result

        return list(combs(range(1, n + 1), k))