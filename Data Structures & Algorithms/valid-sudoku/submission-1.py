class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            #vertical check duplicates number
            dict1 = set()
            for j in range(9):
                if board[j][i] in dict1:
                    return False
                if board[j][i] == '.':
                    continue
                dict1.add(board[j][i])
                
        #horizontal check duplicates numner
        for i in range(9):
            dict2 = set()
            for j in range(9):
                if board[i][j] in dict2:
                    return False
                if board[i][j] == '.':
                    continue
                dict2.add(board[i][j])
                
        #check 3x3 sub-boxes
        for r in range(0,9,3):
            for c in range(0,9,3):
                # (0,0) (2,2)   (x,y)
                # (0,3) (2,5)   x, y+3
                # (0,6) (2,8).  x, y+3
                # (3,0) (5,2)   x+3, y
                # (3,3) (5,5)   x+3, y+3
                # (3,6) (5,8)
                dict3 = set()
                for x in range(3):
                    for y in range(3):
                        if board[r+x][c+y] in dict3:
                            return False
                        if board[r+x][c+y] == '.':
                            continue
                        dict3.add(board[r+x][c+y])
                        

               
                


                
                    
            
        
        return True