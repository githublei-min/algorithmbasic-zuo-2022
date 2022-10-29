from graph import *

class Dijikstra:
    # dijikstra算法1
    # 规定一个出发点，求该点到其他所有点的最短距离
    # 适用范围：没有权值为负数的边
    # 参考： https://github.com/algorithmzuo/algorithmbasic2020/blob/master/src/class16/Code06_Dijkstra.java
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

    # 改进的dijikstra算法: 利用堆结构
    # 从head出发，所有head能到达的节点，生成到达每个节点的最小路径记录并返回
    # 参考：https://github.com/algorithmzuo/algorithmbasic2020/blob/master/src/class16/Code06_Dijkstra.java
    def dijikstra2(self, first):
        node_heap = NodeHeap()
        node_heap.add_update_ignore(first, 0)
        result = {} # node:distance(first到node的最短距离)
        while not node_heap.is_empty():
            record = node_heap.pop()
            cur = record.node
            cur_dis = record.dis # cur diatance
            for edge in cur.edges:
                node_heap.add_update_ignore(edge.n_to, edge.weight + cur_dis)
            result[cur] = cur_dis

        return result

class NodeHeap:
    def __init__(self):
        self.size = 0
        self.nodes_heap = []
        self.dis_map = {} # distance map
        self.heap_index = {} # heap index map

    def is_empty(self):
        return self.size == 0

    def add_update_ignore(self, node, distance):
        # 如果node已经入堆，更新源点到node的最短距离
        if self.in_heap(node):
            self.dis_map[node] = min(self.dis_map[node], distance)
            # 调整堆 insert heapify
            self.insert_heapify(self.heap_index[node])
        if not self.entered(node):
            self.nodes_heap.append(node)
            self.heap_index[node] = self.size
            self.dis_map[node] = distance
            self.insert_heapify(self.size)
            self.size += 1

    def in_heap(self, node):
        return self.entered(node) and self.heap_index[node] != -1

    def entered(self, node):
        return node in self.heap_index.keys()

    def insert_heapify(self, index):
        while self.dis_map[self.nodes_heap[index]] < self.dis_map[self.nodes_heap[int((index - 1) / 2)]]:
            self.swap(index, int((index-1)/2))
            index = int((index -1) / 2)

    def swap(self, index1, index2):
        self.heap_index[self.nodes_heap[index1]] = index2
        self.heap_index[self.nodes_heap[index2]] = index1
        tmp = self.nodes_heap[index1]
        self.nodes_heap[index1] = self.nodes_heap[index2]
        self.nodes_heap[index2] = tmp

    def pop(self):
        node_record = NodeRecord(node=self.nodes_heap[0], distance=self.dis_map[self.nodes_heap[0]])
        self.swap(0, self.size - 1)
        self.heap_index[self.nodes_heap[self.size-1]] = -1
        self.dis_map.pop(self.nodes_heap[self.size-1])
        self.nodes_heap.pop(self.size - 1)
        self.size -= 1
        self.heapify(0, self.size)
        return node_record

    def heapify(self, index, size):
        left = index * 2 + 1
        while left < size:
            smallest = left + 1 if left + 1 < size and \
            self.dis_map[self.nodes_heap[left+1]] < self.dis_map[self.nodes_heap[left]] \
                else left
            smallest = smallest if self.dis_map[self.nodes_heap[smallest]] < self.dis_map[self.nodes_heap[index]] \
                else index
            if smallest == index: break
            self.swap(smallest, index)
            index = smallest
            left = index * 2 + 1

class NodeRecord:
    def __init__(self, node, distance):
        self.node = node
        self.dis = distance

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
result = D.dijikstra2(first)
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