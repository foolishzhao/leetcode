class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n, i = len(number), 0
        blocks = list()
        while i < n - 4:
            blocks.append(number[i: i + 3])
            i += 3

        if n - i == 4:
            blocks.append(number[i: i + 2])
            blocks.append(number[i + 2: n])
        else:
            blocks.append(number[i: n])

        return '-'.join(blocks)
