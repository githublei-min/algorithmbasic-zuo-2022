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
        self.weight = weight # 权重值
        self.n_from = n_from # 起点
        self.n_to = n_to # 终点

# 图结构的描述
class Graph:
    def __init__(self):
        self.nodes = {} # 点集， 保存 value-Node 的映射
        self.edges = [] # 边集， 保存所有边Edge信息

class GraphGenerator:
    """
    这相当于一个接口函数，将各种条件统一转化为上面的图的结构，根据具体情况改写此类即可。
    """
    # 下面是一个例子
    # matrix -> 所有的边
    # N*3的矩阵
    # [weight, from节点， to节点]
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

            Node1 = graph.nodes[n_from] # 起点
            Node2 = graph.nodes[n_to] # 终点
            edge = Edge(weight, Node1, Node2) # 记录下该边的信息
            Node1.nexts.append(Node2) # 记录节点的邻接点信息
            Node1.out_num += 1 # 更新起点的出度
            Node2.in_num += 1 # 更新终点的入度
            Node1.edges.append(edge) # 更新节点邻接边的信息
            graph.edges.append(edge) # 更新图的边信息

        return graph

# test
# 初始化matrx矩阵
# m = [[5, 0, 7], [3, 0, 1]]
# g = GraphGenerator()
# graph = g.createGraph(m)
# print("[weight, node_from, node_to]")
# for i in range(len(graph.edges)):
#     print(str([graph.edges[i].weight, graph.edges[i].n_from.value, graph.edges[i].n_to.value]))
# 输出
# [weight, node_from, node_to]
# [5, 0, 7]
# [3, 0, 1]