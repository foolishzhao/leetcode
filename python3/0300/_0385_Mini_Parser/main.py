class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        st, cur, i, j = [], None, 0, 0
        while j < len(s):
            if s[j] == '[':
                if cur:
                    st.append(cur)
                cur = NestedInteger()
                i = j + 1
            elif s[j] == ']':
                # corner cases: [], [[]]
                if j > i:
                    cur.add(NestedInteger(int(s[i: j])))
                i = j + 1

                if st:
                    t = st.pop()
                    t.add(cur)
                    cur = t
            elif s[j] == ',':
                if s[j - 1] != ']':
                    cur.add(NestedInteger(int(s[i: j])))
                i = j + 1
            j += 1

        return cur
