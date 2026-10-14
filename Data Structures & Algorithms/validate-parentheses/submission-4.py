class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { ")" : "(", "]" : "[", "}" : "{"}

        for x in s:
            if x in hashmap:
                if stack and stack[-1] == hashmap[x]:
                    stack.pop()
                else:
                    return False
            
            else:
              stack.append(x)
            
        return not stack