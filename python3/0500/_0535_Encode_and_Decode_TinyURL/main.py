class Codec:
    def __init__(self):
        self.id = 0
        self.longToShort = dict()
        self.shortToLong = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        self.id += 1
        shortUrl = str(self.id)
        self.longToShort[longUrl] = shortUrl
        self.shortToLong[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong.get(shortUrl, "")
