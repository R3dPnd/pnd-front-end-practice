class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ""
        for i in range(len(s)-1):
            left, right = i-1, i+1
            print(s[i])
            while s[i] == s[right]:
                right +=1
                print(f"{right}:{left}")
            while s[left] == s[right]:
                left -= 1
                right += 1
            # print(s[left:right-1])
            if len(s[left:right-1]) > len(longest_pal):
                longest_pal = s[left:right-1]
        return longest_pal