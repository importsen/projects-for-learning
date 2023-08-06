class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        i, j, result = 0, 0, ""
        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1 
            j += 1 
        return result + word1[i:] + word2[j:]

solution = Solution()
        
merged_string = solution.mergeAlternatively("hello", "world")

print(merged_string)
