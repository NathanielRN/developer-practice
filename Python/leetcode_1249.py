"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, OR
* contains only lowercase characters, OR abc(def)ghi where Φ=abc and Ψ=(def)ghi abc(A)B
* (def)ghi Φ=(def) Ψ=ghi
* (def) Φ=def
* It can be written as ΦΨ (Φ concatenated with Ψ), where Φ and Ψ are valid strings, or
* It can be written as (Ψ), where Ψ is a valid string
"""

# Valid only if [] only lowercase or ABC
# s = "{([a]})" s = "", "abc", "ABS"
# return A or (A)

# s = "((a))" -> (a) return ((a))
# s = (OMEGA)(BETA) -> return (OMEGA)(BETA)
# s = (OMEGA())(BETA) -> (OMEGA())(BETA)
# s = (OMEGA()(BETA) - > (OMEGA)(BETA)
# s = "(abc)(((abc)" stack = [6, 5]
# s = ")(abc)"
# s = "abc(a)b"

class Solution:
    def removeMinParentheses(s: str) -> str:
        # Use a Stack
        stack = []
        remove_indices = set()
        result = ''
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if stack:
                    stack.pop(-1)
                else:
                    remove_indices.add(index)
        remove_indices.update(stack)
        for i in range(len(s)):
            if i not in remove_indices:
                result += s[i]
        return result # ""
