class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each char, increment and then expand out in 
        # each dir until you find a non-palindome
        count = 0
        for i in range(len(s)):
            count += 1
            is_palindrome = True
            while is_palindrome:
                if i + 1 > len(s) or i -1 < 0:
                    is_palindrome = False
                else:
                    is_palindrome = s[i+1] == s[i-1]

        return count