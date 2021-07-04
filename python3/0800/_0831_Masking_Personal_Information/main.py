class Solution:
    def maskPII(self, s: str) -> str:
        def maskEmail(email):
            email = email.lower()
            fields = email.split('@')
            return fields[0][0] + '*' * 5 + fields[0][-1] + '@' + fields[1]

        def maskPhone(phone):
            ds = [c for c in phone if c.isdigit()]
            if len(ds) == 10:
                return '***-***-' + ''.join(ds[-4:])
            else:
                return '+' + '*' * (len(ds) - 10) + '-***-***-' + ''.join(ds[-4:])

        return maskEmail(s) if '@' in s else maskPhone(s)
