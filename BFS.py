# 宽度优先遍历
from graph import *

class BFS:
    def bfs(self, start):
        if start is None: return
        que = [start]
        set = [start]
        while len(que) >0:
            cur = que.pop(0)
            print(cur.name)
            for next in cur.nexts:
                if next not in set:
                    set.append(next)
                    que.append(next)
# test：
m = [[3, 0, 1],
     [2, 0, 2],
     [4, 1, 2],
     [2, 1, 3]]
gen = GraphGenerator()
graph = gen.createGraph(m)
search = BFS()
print("从0开始，宽度优先搜索：")
search.bfs(graph.nodes[0])
# 输出结果：
# 从0开始，宽度优先搜索：
# 0
# 1
# 2
# 3