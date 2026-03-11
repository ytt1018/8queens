from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    使用回溯法解决n皇后问题
    返回所有解的棋盘表示，每个解是一个字符串列表
    例如 n=4 时返回 [[".Q..","...Q","Q...","..Q."], ...]
    """
    def is_safe(board: List[int], row: int, col: int) -> bool:
        """检查在(row, col)放置皇后是否与已放置的皇后冲突"""
        for r in range(row):
            c = board[r]
            # 检查列冲突和对角线冲突
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    
    def backtrack(board: List[int], row: int):
        """回溯搜索"""
        if row == n:
            # 找到一个解，转换为棋盘表示
            solution = []
            for r in range(n):
                line = ['.'] * n
                line[board[r]] = 'Q'
                solution.append(''.join(line))
            result.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # 回溯
    
    result = []
    board = [-1] * n  # board[i]表示第i行皇后所在的列
    backtrack(board, 0)
    return result
