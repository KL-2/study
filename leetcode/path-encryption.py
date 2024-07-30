'''
LCR 122. 路径加密

假定一段路径记作字符串 path,其中以 "." 作为分隔符。现需将路径加密，加密方法为将 path 中的分隔符替换为空格 " "，请返回加密后的字符串。


'''

class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        res=[]
        for p in path:
            if p==".":res.append(' ')
            else:
                res.append(p)
        return "".join(res)