class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        check = {
            "1":0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
            "6":0,
            "7":0,
            "8":0,
            "9":0
        }
        rows = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        cols = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        boxs = [{}, {}, {}, {}, {}, {}, {}, {}, {}]


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                rows[r][board[r][c]] = rows[r].get(board[r][c], 0) + 1
                if rows[r][board[r][c]] > 1:
                    print(rows)
                    return False
                cols[c][board[r][c]] = cols[c].get(board[r][c], 0) + 1
                if cols[c][board[r][c]] > 1:
                    print(cols)
                    return False
                
                box_idx = (r // 3) * 3 + (c // 3)
                
                boxs[box_idx][board[r][c]] = boxs[box_idx].get(board[r][c], 0) + 1
                if boxs[box_idx][board[r][c]] > 1:
                    return False

        return True

