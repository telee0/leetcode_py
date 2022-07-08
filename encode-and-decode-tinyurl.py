"""

https://leetcode.com/problems/encode-and-decode-tinyurl/

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

"""
import zlib


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return zlib.compress(longUrl.encode(), 9)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return zlib.decompress(shortUrl).decode()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

codec = Codec()
url = "https://stackoverflow.com/questions/29243119/how-to-compress-or-compact-a-string-in-python"
encoded = codec.encode(url)
decoded = codec.decode(encoded)
print("{0} {1} {2}".format(len(url), len(encoded), len(decoded)))