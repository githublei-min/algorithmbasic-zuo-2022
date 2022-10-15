# 参考： https://github.com/algorithmzuo/algorithmbasic2020/tree/master/src/class16

# 点结构的描述
class Node:
    def __init__(self, value):
        self.value = value
        self.in_num = 0 # 入度
        self.out_num = 0 # 出度
        self.nexts = [] # 邻接点
        self.edges = [] # 邻接边

# 边结构的描述
class Edge:
    def __init__(self, weight, n_from, n_to):
        self.weight = weight # 权重
        self.n_from = n_from # 起点
        self.n_to = n_to # 终点

# 图结构的描述
class Graph:
    def __init__(self):
        self.nodes = {} # 点集， 保存 点上值-点 的映射
        self.edges = [] # 边集， 保存所有边信息

class GraphGenerator:
    """
    这相当于一个接口函数，将各种条件统一转化为上面的图的结构，根据具体情况改写此类即可。
    """
    # 下面是一个例子
    # matrix -> 所有的边
    # N*3的矩阵
    # [weight, from节点上的值， to节点上的值]
    #
    # [5, 0, 7]
    # [3, 0, 1]
    #
    def createGraph(self, matrix):
        graph = Graph()
        for i in range(len(matrix)):
            weight = matrix[i][0]
            n_from = matrix[i][1]
            n_to = matrix[i][2]

            if n_from not in graph.nodes.keys():
                graph.nodes[n_from] = Node(n_from)

            if n_to not in graph.nodes.keys():
                graph.nodes[n_to] = Node(n_to)

            fromNode = graph.nodes[n_from] # 起点
            toNode = graph.nodes[n_to] # 终点
            edge = Edge(weight, n_from, n_to) # 记录下该边的信息
            fromNode.nexts.append(toNode) # 记录节点的邻接点信息
            fromNode.out_num += 1 # 更新起点的出度
            toNode.in_num += 1 # 更新终点的入度
            fromNode.edges.append(edge) # 更新节点邻接边的信息
            graph.edges.append(edge) # 更新图的边信息

        return graph

# test
# m = [[5, 0, 7], [3, 0, 1]]
#
# g = GraphGenerator()
# graph = g.createGraph(m)
#
# print(str(graph.nodes.keys()))
# for i in range(len(graph.edges)):
#     print(str([graph.edges[i].weight, graph.edges[i].n_from, graph.edges[i].n_to]))

# 输出结果
# dict_keys([0, 1])
# [3, 0, 1]