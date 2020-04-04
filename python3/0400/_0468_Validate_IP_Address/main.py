class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.checkIPV4(IP):
            return "IPv4"
        if self.checkIPV6(IP):
            return "IPv6"
        return "Neither"

    def checkIPV4(self, IP):
        fields = IP.split(".")
        if len(fields) != 4:
            return False

        for field in fields:
            if len(field) > 3:
                return False
            if not field.isdigit():
                return False
            if not (0 <= int(field) <= 255):
                return False
            if len(field) > 1 and field[0] == '0':
                return False

        return True

    def checkIPV6(self, IP):
        fields = IP.split(":")
        if len(fields) != 8:
            return False

        for field in fields:
            if not field or len(field) > 4:
                return False
            for c in field:
                if not ('0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'):
                    return False

        return True

    def validIPAddress2(self, IP: str) -> str:
        def isIPV4(s):
            try:
                return 0 <= int(s) <= 255 and str(int(s)) == s
            except:
                return False

        def isIPV6(s):
            try:
                return len(s) <= 4 and int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IP.count(".") == 3 and all(isIPV4(x) for x in IP.split(".")):
            return "IPv4"

        if IP.count(":") == 7 and all(isIPV6(x) for x in IP.split(":")):
            return "IPv6"

        return "Neither"
