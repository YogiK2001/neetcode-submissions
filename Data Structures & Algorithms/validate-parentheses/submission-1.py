class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stk.append(i)
            elif i == ']' or i == ')' or i == '}':
                if len(stk) == 0:
                    return False
                c = stk[-1]
                if i == ')' and c != '(' or i == '}' and c != '{' or i == ']' and c != '[':
                    return False
                stk.pop()
        if len(stk) == 0:
            return True
        return False