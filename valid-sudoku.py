class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)

        rows = []
        columns = []
        boxes = []

        for i in range(n):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        for i in range(n):
            for j in range(n):
                c = board[i][j]
                if c in rows[i]:
                    return False
                elif c != '.':
                    rows[i].add(c)
                if c in columns[j]:
                    return False
                elif c != '.':
                    columns[j].add(c)
                k = (i // 3) * 3 + (j // 3)
                if c in boxes[k]:
                    return False
                elif c != '.':
                    boxes[k].add(c)

        return True


sol = Solution()
print(sol.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))
print(sol.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))