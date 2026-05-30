class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]

        for i in range(1, len(strs)):
            
            if len(strs[i]) < len(first_word):
                first_word = first_word[:len(strs[i])]

            for j in range(len(first_word)):

                if first_word[j] != strs[i][j]:
                    first_word = first_word[:j]
                    break

        return first_word