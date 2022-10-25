from graph import *
# dijikstra算法1
# 规定一个出发点，求该点到其他所有点的最短距离
# 适用范围：没有权值为负数的边
# 参考： https://github.com/algorithmzuo/algorithmbasic2020/blob/master/src/class16/Code06_Dijkstra.java
class Dijikstra:
    def dijikstra1(self, first):
        """
        从first出发, 到所有点的最小距离
        :param first: Node
        :return: dict{} -> key: 从first出发达到key；value: 从first到key的最小距离；
        如果表中没有T的记录，表示从first到T的距离为正无穷
        """
        distance_map = {}
        distance_map[first] = 0
        # 已经确定最短距离的点，存在selected_nodes中，后面不再动
        selected_nodes = []
        cur_min = self.getMinDistanceAndUnselectedNode(distance_map, selected_nodes)
        while cur_min is not None:
            distance = distance_map[cur_min]
            for edge in cur_min.edges:
                to_node = edge.n_to
                if to_node not in distance_map.keys():
                    distance_map[to_node] = distance + edge.weight
                distance_map[to_node] = min(distance_map[to_node], distance + edge.weight)
            selected_nodes.append(cur_min)
            cur_min = self.getMinDistanceAndUnselectedNode(distance_map, selected_nodes)

        return distance_map

    def getMinDistanceAndUnselectedNode(self, distance_map, selected_nodes):
        minNode = None
        min_distance = float('inf') # python中的无穷大
        for key in distance_map.keys():
            node = key
            distance = distance_map[key]
            if node not in selected_nodes and distance < min_distance:
                minNode = node
                min_distance = distance

        return minNode

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
# 指定出发点
first = graph.nodes['C']
D = Dijikstra()
result = D.dijikstra1(first)
for node in result.keys():
    print(str(first.value)+str(node.value)+':'+str(result[node]))

# 输出
# CC:0
# CE:5
# CB:8
# CF:13
# CG:14
# CD:17
# CA:15