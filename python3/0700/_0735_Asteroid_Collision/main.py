from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n, i = len(asteroids), 0
        st = list()
        while i < n:
            a = asteroids[i]
            if not st or not (st[-1] > 0 and a < 0):
                st.append(a)
                i += 1
            else:
                if st[-1] > -a:
                    i += 1
                elif st[-1] < -a:
                    st.pop()
                else:
                    st.pop()
                    i += 1
        return st
