class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) == 1:
            return 1
            
        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                new_char = s[j]
                if new_char in chars:
                    break
                else:
                    length = j-i+1
                    max_len = max(length, max_len)
                    chars.add(new_char)
                    
        return max_len