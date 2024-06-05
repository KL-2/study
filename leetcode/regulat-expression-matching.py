'''LeetCode 第10题 正则表达式匹配

《剑指Offer第2版》第19题 正则表达式匹配

给你一个字符串 s 和一个字符规律 p,请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的,而不是部分字符串。

示例 1:

输入:s = "aa", p = "a"
输出:false
解释:"a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:s = "aa", p = "a*"
输出:true
解释:因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:s = "ab", p = ".*"
输出:true
解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

'''

"""
p[j]!='*':
    f[i,j]=f[i-1,j-1]&(i,j)
p[j]=='*':
    f[i,j]=f[i,j-2](0个) ||f[i,j]=f[i-1,j-2]&(i,j-1)(1个)||f[i,j]=f[i-2,j-2]&(i,j-1)&(i-1,j-1)(2个)
    令i-1=i找规律
    f[i,j]=f[i,j-2] ||f[i-1,j]&(i,j-1)
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:#如果s是空字符，都返回False
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]#n为列，m为行
        # print(m,n)#m=2,n=1
        # #f[0][1] = True#[[False, True], [False, False], [False, False]]
        # print(f)#[[False, False], [False, False], [False, False]]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1,n + 1):
            #for j in range(n + 1):时s = "aaa" p = "a"不对
            #空模式只有在i=0时j=0才有用
            #p[j - 1] 会导致访问 p[-1]在python中不会报错，但会访问最后一个元素
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]#f[i,j]=f[i,j-2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]#f[i-1,j]&(i,j-1)
                else:#p[j-1]!='*':
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]#    f[i,j]=f[i-1,j-1]&(i,j)
        return f[m][n]

if __name__=="__main__":
    solution=Solution()
    s = "aaa"
    p = "a"
    print(solution.isMatch(s,p))