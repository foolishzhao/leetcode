class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0
        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CM", "DCCCC")
        s = s.replace("CD", "CCCC")
        for char in s:
            number += dic[char]
        return number


if __name__ == '__main__':
    s = "XIV"
    ans = Solution().romanToInt(s)
    print(ans)
