# leetcode 743题， 用这道题来练习Dijikstra算法
# 参考： https://github.com/algorithmzuo/algorithmbasic2020/blob/master/src/class16/Code06_NetworkDelayTime.java
# python中优先级队列的实现参考：https://geek-docs.com/python/python-examples/python-priority-queue.html
from queue import PriorityQueue

class NetworkDeleyTime:
    # 方法1：普通堆+屏蔽已经计算过的点
    def net_deley_time1(self, times, n, k):
        # 记录每个节点指向的节点和对应的延迟
        nexts = {}
        for record in times:
            nexts[record[0]] = []
        for record in times:
            nexts[record[0]].append([record[1], record[2]])
        # 采用优先级队列来充当小顶堆的角色
        # 有关queue.PriorityQueue的知识，
        # 参考官方文档：https://docs.python.org/zh-cn/3.7/library/queue.html?highlight=priorityqueue#queue.PriorityQueue
        heap = PriorityQueue()
        heap.put((0, [k, 0]))
        # used 记录已经被计算过的节点
        used = []
        # result 记录所有最短距离的最大值，即题目所求
        result = 0
        while not heap.empty() and len(used) < n:
            item = heap.get()
            cur = item[1][0]
            delay = item[1][1]
            if cur in used: continue
            used.append(cur)
            result = max(delay, result)
            if cur in nexts.keys():
                for next in nexts[cur]:
                    new_delay = delay + next[1]
                    heap.put((new_delay, [next[0], new_delay]))
        return -1 if len(used) < n else result

    # 方法2：加强堆的解法
    def net_deley_time2(self, times, n, k):
        nexts = {}
        for item in times:
            nexts[item[0]] = []
        for item in times:
            nexts[item[0]].append([item[1], item[2]])

        heap = Heap(n)
        heap.add(k, 0)
        num = 0
        result = 0
        while not heap.empty():
            cur = heap.pop()
            cur_node = cur[0]
            cur_delay = cur[1]
            num += 1
            result = max(result, cur_delay)
            if cur_node in nexts.keys():
                for item in nexts[cur_node]:
                    heap.add(item[0], cur_delay + item[1])

        return -1 if num < n else result

class Heap:
    def __init__(self, n):
        self.used = []
        self.heap = []
        self.h_index = [-1] * (n+1) # heap index
        self.size = 0

    def empty(self):
        return self.size == 0

    def add(self, node, delay):
        if node in self.used: return
        if self.h_index[node] == -1:
            self.heap.append([node, delay])
            self.h_index[node] = self.size
            self.heap_insert(self.size)
            self.size += 1
        else:
            index = self.h_index[node]
            if delay < self.heap[index][1]:
                self.heap[index][1] = delay
                self.heap_insert(index)

    def heap_insert(self, index):
        parent = int((index - 1) / 2)
        while self.heap[index][1] < self.heap[parent][1]:
            self.swap(index, parent)
            index = parent
            parent = int((index - 1) / 2)

    def swap(self, index1, index2):
        node1 = self.heap[index1]
        node2 = self.heap[index2]
        self.h_index[node1[0]] = index2
        self.h_index[node2[0]] = index1
        self.heap[index1] = node2
        self.heap[index2] = node1

    def pop(self):
        cur = self.heap[0]
        self.size -= 1
        self.swap(0, self.size)
        self.heap.pop()
        self.heapify(0)
        self.used.append(cur[0])
        self.h_index[cur[0]] = -1
        return cur

    def heapify(self, index):
        left = index * 2 + 1
        while left < self.size:
            smallest = left + 1 if (left + 1) < self.size and self.heap[left+1][1] < self.heap[left][1] \
                else left
            smallest = smallest if self.heap[smallest][1] < self.heap[index][1] else index
            if smallest == index: break
            self.swap(index, smallest)
            index = smallest
            left = index * 2 - 1


# 测试
times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n1, k1 = 4, 2
times2 = [[1, 2, 1]]
n2, k2 = 2, 1
times3 = [[1, 2, 1]]
n3, k3 = 2, 2
solution = NetworkDeleyTime()
# 测试方法1
result1 = solution.net_deley_time1(times1, n1, k1)
result2 = solution.net_deley_time1(times2, n2, k2)
result3 = solution.net_deley_time1(times3, n3, k3)
print(result1==2 and result2==1 and result3==-1)
# True
# 测试方法2
result1 = solution.net_deley_time2(times1, n1, k1)
result2 = solution.net_deley_time2(times2, n2, k2)
result3 = solution.net_deley_time2(times3, n3, k3)
print(result1==2 and result2==1 and result3==-1)