import re


class Solution:
    def decodeString(self, s: str) -> str:
        new_array = re.findall("\[(.*?)\]", s)
        print(new_array)


# tests
test = Solution()
test.decodeString("3[a2[c]]")
