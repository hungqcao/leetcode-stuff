from typing import List
import collections

def slidingPuzzle(board: List[List[int]]):
    maxRow, maxCol = 2, 3
    final_ans =  [float('inf')]

    def toString(bd) -> str:
        ans = ''
        for r in bd:
            for c in r:
                ans += str(c)
        return ans

    def fromString(str):
        ans = [[0 for _ in range(3)] for _ in range(2)]
        for i, c in enumerate(str):
            row = i // 3
            col = i % 3
            ans[row][col]  = int(c)
        return ans

    def bfs(board, r, c):
        
        queue = [(toString(board), r, c)]
        seen = set()
        ans = 0

        #print(str)
        while queue:
            size = len(queue)
            ans += 1
            for i in range(size):
                str, rowOfZero, colOfZero = queue.pop(0)
                pos_moves = list(filter(lambda x: 0 <= x[0] < maxRow and 0 <= x[1] < maxCol, [(rowOfZero + 1, colOfZero), (rowOfZero - 1, colOfZero), (rowOfZero, colOfZero + 1), (rowOfZero, colOfZero - 1)]))
                for moveRow, moveCol in pos_moves:
                    board = fromString(str)
                    tmp_move = board[moveRow][moveCol]
                    board[rowOfZero][colOfZero] = tmp_move
                    board[moveRow][moveCol] = 0
                    tmp_str = toString(board)
                    if tmp_str not in seen:
                        seen.add(tmp_str)
                        queue.append((tmp_str, moveRow, moveCol))
                    if tmp_str == '123450':
                        return ans
        return -1



    def dfs(str, rowOfZero, colOfZero, seen, dp, moves):
        if str == '123450':
            final_ans[0] = min(final_ans[0], moves)
            return
        if str in dp and dp[str] < moves: return
        if str not in dp:
            dp[str] = moves
        else:
            dp[str] = min(moves, dp[str])

        pos_moves = list(filter(lambda x: 0 <= x[0] < maxRow and 0 <= x[1] < maxCol, [(rowOfZero + 1, colOfZero), (rowOfZero - 1, colOfZero), (rowOfZero, colOfZero + 1), (rowOfZero, colOfZero - 1)]))
        #print(str)
        for moveRow, moveCol in pos_moves:
            board = fromString(str)
            tmp_move = board[moveRow][moveCol]
            board[rowOfZero][colOfZero] = tmp_move
            board[moveRow][moveCol] = 0
            tmp_str = toString(board)
            if tmp_str not in seen:
                seen.add(tmp_str)    
                dfs(tmp_str, moveRow, moveCol, seen, dp, moves + 1)
                seen.remove(tmp_str)    
    for r in range(2):
        for c in range(3):
            if board[r][c] == 0:
                #dfs(toString(board), r, c, set(), dict(), 0)
                return bfs(board, r, c)
    return final_ans[0] if final_ans[0] != float('inf') else -1


#print(slidingPuzzle([[1,2,3],[4,0,5]]))
#print(slidingPuzzle([[1,2,3],[5,4,0]]))
print(slidingPuzzle([[4,1,2],[5,0,3]]))