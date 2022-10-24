# prim（最小生成树-prim算法）
# for undirected graph（要求：无向图）
from graph import *

class Prim:
    def prim(self, graph):
        """
        prim算法，返回图graph的最小生成树（总权值最小的边的集合）
        :param graph: Graph
        :return: list
        """
        # record: 所有访问过的节点
        record = []
        # edges: record中所有节点所解锁的边
        edges = []
        # result: 依次挑选出的边
        result = []
        for node in graph.nodes.values(): # 随意挑选一个点node作为起始点
            # record更新访问过的点
            record.append(node)
            for edge in node.edges: # 由一个点解锁所有相连的边
                edges.append(edge)
            while len(edges) > 0: # 每次取出权重最小的边
                edge = min(edges, key=lambda edge: edge.weight)
                edges.remove(edge)
                to_node = edge.n_to # 解锁该边的另一个端点
                if to_node not in record:
                    record.append(to_node) # record更新访问过的点
                    result.append(edge) # result更新挑选上的边
                    # 根据该端点又解锁新的相连的边
                    for next_edge in to_node.edges:
                        edges.append(next_edge)

        return result

# test
# 自定义一个无向连通图
m = [[7, 'A', 'B'], [5, 'A', 'D'], [9, 'B', 'D'],
     [8, 'B', 'C'], [7, 'B', 'E'], [5, 'C', 'E'],
     [15, 'D', 'E'], [6, 'D', 'F'], [8, 'E', 'F'],
     [9, 'E', 'G'], [11, 'F', 'G'],
     [7, 'B', 'A'], [5, 'D', 'A'], [9, 'D', 'B'],
     [8, 'C', 'B'], [7, 'E', 'B'], [5, 'E', 'C'],
     [15, 'E', 'D'], [6, 'F', 'D'], [8, 'F', 'E'],
     [9, 'G', 'E'], [11, 'G', 'F']]
generator = GraphGenerator()
graph = generator.createGraph(m)

p = Prim()
res_edge_list = p.prim(graph)

# 打印prim算法结果
output = [] # 边信息输出
min_weights_sum = 0 # 权值的最小和
for _, edge in enumerate(res_edge_list):
    output.append(str(edge.n_from.value) + str(edge.n_to.value))
    min_weights_sum += edge.weight
print("Prim算法选出的边：\n", output)
print("最小和=", min_weights_sum)

# 输出
# Prim算法选出的边：
#  ['AD', 'DF', 'AB', 'BE', 'EC', 'EG']
# 最小和= 39