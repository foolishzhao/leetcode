import re


class Solution:
    def isValid(self, code: str) -> bool:
        i, n, st = 0, len(code), list()
        while i < n:
            # check outermost closed tag
            if i and not st:
                return False

            if code[i:].startswith("<![CDATA["):
                j = code.find("]]>", i + 9)
                if j == -1:
                    return False
                i = j + 3
            elif code[i:].startswith("</"):
                j = code.find(">", i + 2)
                if j == -1:
                    return False
                tag = code[i + 2: j]
                if not self.validTag(tag) or not st or st[-1] != tag:
                    return False
                st.pop()
                i = j + 1
            elif code[i:].startswith("<"):
                j = code.find(">", i + 1)
                if j == -1:
                    return False
                tag = code[i + 1: j]
                if not self.validTag(tag):
                    return False
                st.append(tag)
                i = j + 1
            else:
                i += 1
        return not st

    def validTag(self, tag):
        return 1 <= len(tag) <= 9 and tag.isalpha() and tag.isupper()

    # Use Non Greedy mode (.*?) when matching CDATA.
    # Reference: https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
    #
    # <([A-Z]{1,9})> : match start tag, whose tag name should be upper-case letters, and has length in range [1,9]
    # [^<]*: match tag content, whose character can be anyone except '<'
    # </\1>: match close tag, whose tag name should be exactly the same as start tag
    def isValid2(self, code: str) -> bool:
        if code == 't':
            return False

        code = re.sub(r'<!\[CDATA\[.*?\]\]>', 'c', code)
        prev = ""
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*?</\1>', 't', code)

        return code == 't'
