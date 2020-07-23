from typing import List
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        deg_freedom = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        self.Found = False

        def chk(i, j, k):
            if self.Found: return
            if k == word_length:
                self.Found = True
                return

            if i < 0 or i >= b or j < 0 or j >= l: return
            tmp = board[i][j]
            if tmp != word[k]: return

            board[i][j] = "#"
            for x, y in deg_freedom:
                chk(i + x, j + y, k + 1)
            board[i][j] = tmp

        b, l, word_length = len(board), len(board[0]), len(word)
        if word_length == 0 or word_length > l * b:
            return False
        for i in range(b):
            for j in range(l):
                if self.Found: return True
                chk(i, j, 0)
        return self.Found
if __name__=="__main__":
    output=Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
,"ABC")
    print(output)



