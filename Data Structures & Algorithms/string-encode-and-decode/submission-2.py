class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("$")
            encoded.append(s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            num = ""
            while s[i] != "$":
                num += s[i]
                i += 1
            i += 1
            string = ""
            for j in range(int(num)):
                string += s[i + j]
            i += int(num)
            result.append(string)
        return result

