class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return {'()'}

        output = set()

        for i in range(1, n // 2 + 1):
            p1 = self.generateParenthesis(i)
            p2 = self.generateParenthesis(n - i)
            for p in p1:
                for q in p2:
                    output.add(p + q)
                    output.add(q + p)

        print(len(output))
        return output

        if n == 1:
            return {'()'}

        output = set()

        patterns = self.generateParenthesis(n - 1)

        for p in patterns:
            output.add('(' + p + ')')
            output.add('()' + p)
            output.add(p + '()')

        print(len(output))
        return output


sol = Solution()
print(sol.generateParenthesis(5))
