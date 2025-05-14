class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each char, increment and then expand out in 
        # each dir until you find a non-palindome
        count = 0
        for i in range(len(s)):
            # Move to the right until a new character
            c = s[i]
            left_pointer = i-1
            right_pointer = i
            while right_pointer < len(s) and s[right_pointer] == c:
                count += 1
                right_pointer += 1
            print(right_pointer)
            while left_pointer >=0 and right_pointer <len(s) and s[left_pointer] == s[right_pointer]:
                count += 1
                left_pointer -= 1
                right_pointer += 1

        return count
    