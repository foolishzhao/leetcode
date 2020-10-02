class Solution:
    def entityParser(self, text: str) -> str:
        text = text.replace("&quot;", '"')
        text = text.replace("&apos;", "'")
        text = text.replace("&gt;", '>')
        text = text.replace("&lt;", '<')
        text = text.replace("&frasl;", '/')
        # put this at last, coz & can be used to form a new entity
        text = text.replace("&amp;", '&')
        return text
