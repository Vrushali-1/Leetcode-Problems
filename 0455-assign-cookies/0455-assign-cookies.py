class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        satisfied, children, cookies = 0, 0, 0

        while cookies < len(s) and children < len(g):
            if s[cookies] >= g[children]:
                satisfied += 1
                children += 1
            cookies += 1
        return satisfied