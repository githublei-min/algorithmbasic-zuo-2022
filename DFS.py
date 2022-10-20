# 深度优先搜索（Depth First Search）
from graph import *

class DFS:
    def dfs(self, start): # 从start开始做深度优先遍历
        if start is None:
            return
        stack = [start]
        set = [start]
        print(start.name)
        while len(stack) > 0:
            cur = stack.pop()
            for next in cur.nexts:
                if next not in set:
                    stack.append(cur)
                    stack.append(next)
                    set.append(next)
                    print(next.name)
                    break

# test
m = [[1, 1, 2],
     [1, 1, 3],
     [1, 2, 5],
     [1, 3, 2],
     [1, 3, 4],
     [1, 4, 5]]
generator = GraphGenerator()
g = generator.createGraph(m)
search = DFS()
print("从1开始深度优先搜索：")
search.dfs(g.nodes[1])
# 输出
# 从1开始深度优先搜索：
# 1
# 2
# 5
# 3
# 4