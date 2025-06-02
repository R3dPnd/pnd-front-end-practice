class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        section_one = []

        i = 0

        for i in range(len(s)):
            char = s[i]
            if char == "-" and len(section_one) > 0:
                section_one.append(char.lower)
                break
            else:
                section_one.append(char.lower)
        key = [section_one]
        test = "".join(key)
        print(test)
        for i in range(len(s)):
            char = s[i]
            if char == "-":
                continue

        return str(key)