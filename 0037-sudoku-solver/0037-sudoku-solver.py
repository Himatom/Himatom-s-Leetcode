class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(idx=0):
            if idx == len(empty):
                return True
            
            r, c = empty[idx]
            box_idx = (r // 3) * 3 + c // 3
            
            for val in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    if backtrack(idx + 1):
                        return True
                        
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False

        backtrack()