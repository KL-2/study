# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# LeetCode 第79题 单词搜索
# 《剑指Offer第2版》第12题 矩阵中的路径

class Solution:
    def exist(self,board,word):
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,k):
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            board[i][j]=''
            for dir in dirs:
                if dfs(i+dir[0],j+dir[1],k+1):
                    return True
            board[i][j]=word[k]
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

if __name__=="__main__":
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    
    board2 = [["a","b"],["c","d"]]
    word2 = "abcd"

    solution=Solution()
    print(solution.exist(board1,word1))
    print(solution.exist(board2,word2))