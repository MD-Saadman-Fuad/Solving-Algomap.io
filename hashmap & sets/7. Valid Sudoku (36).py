class Solution:
    def isValidSudoku(self, board):
        # basic approach
        # length = len(board)
        # for row in board:
        #     for i in range(length):
        #         for j in range(i+1, length):
        #             if row[i] != "." and row[i] == row[j]:
        #                 return False

                                
        # for col in range(length):           
        #     for row1 in range(length):      
        #         for row2 in range(row1+1, length):
        #             if board[row1][col] != "." and board[row1][col] == board[row2][col]:
        #                 return False
                    
        # for box_row in range(3):
        #     for box_col in range(3):
        #         seen = set()
        #         for row in range(box_row*3, box_row*3 + 3):
        #             for col in range(box_col*3, box_col*3 + 3):
        #                 num = board [row][col]
        #                 if num != ".":
        #                     if num in seen:
        #                         return False
        #                     seen.add(num)
        # Effecient approach

        length = len(board)

        for row in board:
            seen = set()
            for value in range(length):
                # seen = set()
                if row[value] != "." and row[value] in seen:
                    return False
                seen.add(row[value])

        for col in range(length):
            seen = set()       
            for row in range(length):      
                if board[row][col] != "." and board[row][col] in seen:
                    return False
                seen.add(board[row][col])


            
                    
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row*3, box_row*3 + 3):
                    for col in range(box_col*3, box_col*3 + 3):
                        num = board [row][col]
                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)



        return True



x = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(x.isValidSudoku(board))
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(x.isValidSudoku(board))