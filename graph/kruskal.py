from graph import *

class Kruskal:
    def kruskal(self, graph):
        """
        kruskal算法 适用于无向图
        :param graph: Graph
        :return: list(Edge)
        """
        # 初始化并查集
        union_find = UnionFind()
        # 将所有顶点各自成集
        union_find.makeSets(graph.nodes.values())

        # 用比较器将所有边升序排序放进队列，然后从小到大依次排出
        # python中使用比较器的方式可以参考：https://www.cnblogs.com/ljdsbfj/p/16578925.html#no5
        sorted_edges = sorted(graph.edges, key=lambda edge: edge.weight) # 此处可视为比较器

        # result 用来存放输出的边
        result = []
        while len(sorted_edges) > 0:
            cur_edge = sorted_edges.pop(0) # 排出剩余边中权值最小的边
            # 判断该边两端点是否属于同一个集合
            if not union_find.isSameSet(cur_edge.n_from, cur_edge.n_to):
                # 不属于同一个集合，输出该边
                result.append(cur_edge)
                # 合并两个集合
                union_find.union(cur_edge.n_from, cur_edge.n_to)

        return result

class UnionFind: # 并查集

    def __init__(self):
        self.father_map = {} # key-value： 节点-其上一个节点
        self.size_map = {} # key-value: 某一个集合的代表节点-该集合的节点个数

    def makeSets(self, nodes):
        """
        给输入的值各自创建集合
        :param nodes: list(Node)
        :return: None
        """
        self.father_map.clear()
        self.size_map.clear()
        for node in nodes:
            self.father_map[node] = node
            self.size_map[node] = 1

    def findFather(self, n):
        """
        查找节点n所在集合的代表节点，代表节点就是该集合创建时的原始节点
        :param n: Node
        :return: Node
        """
        path_stack = []
        while n != self.father_map[n]:
            path_stack.append(n) # 记录向上查询经过的节点
            n = self.father_map[n] # 当前节点不是该集合的原始节点，继续向上查询
        # n的最后值就是该集合的原始节点，称为该集合的代表节点
        while len(path_stack) > 0:
            # 将所有节点的上一个节点更新为原始节点
            self.father_map[path_stack.pop()] = n

        return n

    def isSameSet(self, a, b):
        """
        判断两个节点a, b是否属于同一个集合
        :param a: Node
        :param b: Node
        :return: bool
        """
        return self.findFather(a) == self.findFather(b)

    def union(self, a, b):
        """
        合并节点a, b各自所在的两个集合
        :param a: Node
        :param b: Node
        :return: None
        """
        if a is None or b is None:
            return

        # 查询两个集合各自的代表节点
        a_first = self.findFather(a)
        b_first = self.findFather(b)

        # 将小集合并进大集合
        if a_first != b_first:
            a_size = self.size_map[a_first]
            b_size = self.size_map[b_first]
            if a_size <= b_size:
                self.father_map[a_first] = b_first
                self.size_map[b_first] = a_size + b_size
                self.size_map.pop(a_first)
            else:
                self.father_map[b_first] = a_first
                self.size_map[a_first] = a_size + b_size
                self.size_map.pop(b_first)

# test
m = [[7, 'A', 'B'], [5, 'A', 'D'], [9, 'B', 'D'],
     [8, 'B', 'C'], [7, 'B', 'E'], [5, 'C', 'E'],
     [15, 'D', 'E'], [6, 'D', 'F'], [8, 'E', 'F'],
     [9, 'E', 'G'], [11, 'F', 'G']]
generator = GraphGenerator()
graph = generator.createGraph(m)

kruskal = Kruskal()
result = kruskal.kruskal(graph)

output = []
for _, edge in enumerate(result):
    output.append(str(edge.n_from.value) + str(edge.n_to.value))
print(output)

# 输出：['AD', 'CE', 'DF', 'AB', 'BE', 'EG']