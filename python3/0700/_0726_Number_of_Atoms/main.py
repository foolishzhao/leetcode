import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st, counter = list(), collections.defaultdict(int)
        n, i = len(formula), 0
        while i < n:
            if formula[i].isupper():
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                t = j
                while t < n and formula[t].isdigit():
                    t += 1
                v = int(formula[j:t]) if t > j else 1
                counter[formula[i: j]] += v
                i = t
            elif formula[i] == '(':
                st.append(counter)
                counter = collections.defaultdict(int)
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                times = int(formula[i + 1: j]) if j > i + 1 else 1
                oldCounter = st.pop()
                for k, v in counter.items():
                    oldCounter[k] += v * times
                counter = oldCounter
                i = j
        return ''.join([k + str(v) if v > 1 else k for k, v in sorted(counter.items())])

    def countOfAtoms2(self, formula: str) -> str:
        counter, times, atom = collections.defaultdict(int), 1, ""
        st, cnt, i = list(), 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ')':
                st.append(cnt)
                times *= cnt
                cnt, i = 0, 0
            elif c == '(':
                times //= st.pop()
            elif c.islower():
                atom += c
            elif c.isupper():
                atom += c
                counter[atom[::-1]] += (cnt or 1) * times
                atom = ""
                cnt, i = 0, 0
        return ''.join([k + str(v) if v > 1 else k for k, v in sorted(counter.items())])
