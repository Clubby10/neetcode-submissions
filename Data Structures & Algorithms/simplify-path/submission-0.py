class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/") # list contain names between /

        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)

        return "/" + "/".join(stack)