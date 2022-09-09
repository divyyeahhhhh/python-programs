class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = r"{}".format(p)
        p = re.compile(p)
        if p.fullmatch(s):
            return "true"
        else:
            return "false"
