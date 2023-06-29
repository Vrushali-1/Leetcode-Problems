class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for s,t in zip(s,t):
            if s not in countS and t not in countT:
                countS[s] = t
                countT[t] = s
            elif countS.get(s) != t or countT.get(t) != s:
                return False
        return True
        