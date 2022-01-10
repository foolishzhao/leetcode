class Solution():

    def toEnglish(self, num):
        def toEnglish100(num):
            str = ""
            if num >= 100:
                str = dic1[num // 100 - 1] + " Hundred " + str
                num %= 100

            if (num >= 11 and num <= 19):
                return str + dic3[num - 11] + " "

            elif (num == 10 or num >= 20):
                str += dic2[num // 10 - 1] + " "
                num %= 10

            if (num >= 1 and num <= 9):
                str += dic1[num - 1] + " "
            return str

        dic1 = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        dic2 = ["Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        dic3 = ["Eleven","Twelve","ThirTteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        dic4 = ["", "Thousand and", "Million,"]

        if num == 0:
            return "Zero"
        if num < 0:
            return "negative" + self.toEnglish(-1 * num)
        count = 0
        str = ""
        while (num > 0):
            if num % 1000 != 0:
                str = toEnglish100(num % 1000) + dic4[count] + " " + str
            num = num // 1000
            count += 1
        return str


if __name__ == '__main__':
    a = 12310010
    print(Solution().toEnglish(a))
