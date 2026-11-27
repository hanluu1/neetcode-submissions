class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #9 rows, 9 collums, 9 boxes
        #using hash maps of sets to track rows, cols, squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if (val in rows[r] 
                    or val in cols[c] 
                    or val in blocks[(r // 3, c // 3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                blocks[(r // 3, c // 3)].add(val)
        return True

                



