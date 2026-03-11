import pytest
from src.eight_queens import solve_n_queens

def verify_solution(board: List[str]) -> bool:
    """验证一个解是否合法（皇后互不攻击）"""
    n = len(board)
    queens = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'Q':
                queens.append((r, c))
    
    # 应该有n个皇后
    if len(queens) != n:
        return False
    
    # 检查任意两个皇后是否冲突
    for i in range(n):
        for j in range(i + 1, n):
            r1, c1 = queens[i]
            r2, c2 = queens[j]
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True

def test_n1():
    """测试n=1的情况"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert solutions[0] == ["Q"]
    assert verify_solution(solutions[0])

def test_n2():
    """测试n=2的情况（无解）"""
    solutions = solve_n_queens(2)
    assert len(solutions) == 0

def test_n3():
    """测试n=3的情况（无解）"""
    solutions = solve_n_queens(3)
    assert len(solutions) == 0

def test_n4():
    """测试n=4的情况（2个解）"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    for sol in solutions:
        assert verify_solution(sol)

def test_n8():
    """测试n=8的情况（92个解）"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92
    # 只验证前几个解即可，避免网页端提交内容过多
    for sol in solutions[:5]:
        assert verify_solution(sol)
