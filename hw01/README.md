# 八皇后问题求解器

## 实现思路
使用回溯算法解决n皇后问题。核心思想是逐行放置皇后，每行尝试所有列，通过is_safe函数检查是否与已放置的皇后冲突（列冲突、对角线冲突）。当成功放置n个皇后时得到一个解。

## 文件说明
- `src/eight_queens.py`：主求解器实现
- `tests/test_eight_queens.py`：单元测试

## 运行方式
由于本项目完全在GitHub网页端完成，无法直接运行测试。如需验证代码，请下载到本地后执行：
```bash
pip install pytest
pytest tests/ -v
