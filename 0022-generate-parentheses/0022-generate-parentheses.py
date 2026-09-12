class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []

        def backtrack(pars, l, r):
            if l == 0 and r == 0:
                result.append(str("".join(pars)))
                return
            if l > 0:
                pars.append("(")
                backtrack(pars, l - 1, r)
                pars.pop()
            if r > l:
                pars.append(")")
                backtrack(pars, l, r - 1)
                pars.pop()
            
        backtrack([], n, n)

        return result