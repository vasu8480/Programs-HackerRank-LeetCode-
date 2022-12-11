class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
codec=Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))
#--------------------------------------------------------------------------------------------------------------
class Codec:
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodingMap[shortUrl]
codec=Codec()
print(codec.decode(codec.encode("http://nurukurthivasu.tk")))
print(codec.encode("http://nurukurthivasu.tk"))
print(codec.decode('https://tinyurl.com/1'))
