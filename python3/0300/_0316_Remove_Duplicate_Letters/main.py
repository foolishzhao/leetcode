import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, st = collections.Counter(s), list()
        for c in s:
            counter[c] -= 1
            # why can skip the dup is as we can't make the sequence smaller even if we remove all characters after c
            if c in st:
                continue

            while st and st[-1] > c and counter[st[-1]] > 0:
                st.pop()
            st.append(c)
        return ''.join(st)
