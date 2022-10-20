from graph import *

# 拓扑排序
class TopologicalOrder:
    def topoSort_bfs(self, graph):
        # 先建立以节点为键值，节点入度为值的映射表
        indegree_map = {}
        zero_degree_nodes = [] # 同时用队列记录下入度为0的节点
        for _, node in graph.nodes.items():
            indegree_map[node] = node.in_num
            if node.in_num == 0:
                zero_degree_nodes.append(node)

        #开始进行拓扑排序，结果保存在数组中
        results = [] # 保存输出的节点的值
        while len(zero_degree_nodes) > 0:
            cur = zero_degree_nodes.pop(0)
            results.append(cur.name)
            for next in cur.nexts:
                indegree_map[next] -= 1
                if indegree_map[next] == 0:
                    zero_degree_nodes.append(next)
        # 返回值就是目标数组
        return results

# test
matrix = [[0, 0, 1],
          [0, 0, 2],
          [0, 0, 3],
          [0, 1, 4],
          [0, 2, 4],
          [0, 2, 5],
          [0, 3, 4],
          [0, 3, 5]]
generator = GraphGenerator()
graph = generator.createGraph(matrix)

topo_sort = TopologicalOrder()
sort_result = topo_sort.topoSort_bfs(graph)
print(str(sort_result))