class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "\n"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            cur = ""
            while (s[i] != '\n'):
                cur += s[i]
                i += 1
            res.append(cur)
            i += 1
        return res