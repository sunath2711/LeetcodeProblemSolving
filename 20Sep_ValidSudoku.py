class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Validate rows
        for i in range(9):
            my_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in my_set:
                    return False
                my_set.add(board[i][j])

        #Validate columns
        for i in range(9):
            my_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in my_set:
                    return False
                my_set.add(board[j][i])

        def validBox(sr,sc):
            my_set = set()
            for i in range(sr,sr+3):
                for j in range(sc,sc+3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in my_set:
                        return False
                    my_set.add(board[i][j])
            return True

        sr,sc = 0,0
        for sr in range(0,9,3):
            for sc in range(0,9,3):
                if not validBox(sr,sc):
                    return False

        return True






        
