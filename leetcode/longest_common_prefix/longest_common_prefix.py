class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        index = 0
        for char in strs[0]:
            for palabra in strs:
                if index >= len(palabra) or palabra[index] != char:
                    return output
            output += char
            index += 1
        return output
