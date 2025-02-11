class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ele in s :
            if not stack :
                stack.append(ele)
            else :
                if (stack[-1] == '(' and ele == ')' )\
                    or (stack[-1] == '[' and ele == ']' )\
                    or (stack[-1] == '{' and ele == '}' ) :
                    stack.pop()
                else : 
                    stack.append(ele)
        return not stack 
