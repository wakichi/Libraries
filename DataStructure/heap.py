# You can use heapq
# import heapq
# number of root is the biggest
class Heap:
    def __init__(self):
        self.heap = []

    def push(self,x):
        self.heap.append(x)
        i = len(self.heap) -1 # xの頂点番号
        while (i > 0):
            p = (i-1)//2
            if (self.heap[p] >= x):
                break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x
    

    def pop(self):
        if len(self.heap) == 0: return 
        num_return = self.heap[0]
        x = self.heap.pop(-1)
        i = 0
        # 子孫のーどが一つ以上存在する場合。
        while i*2+1 < len(self.heap) :
            #大きい子頂点をchild1にする。
            child1 = 2*i+1
            child2 = 2*i+2
            if child2< len(self.heap) and self.heap[child1] < self.heap[child2] :
                child1 = child2
            if self.heap[child1] <= x: break
            self.heap[i] = self.heap[child1]
            i = child1
        self.heap[i] = x


    def root(self):
        return self.heap[0] if len(self.heap) != 0 else "Error"

    def heap_print(self):
        print(self.heap)

if __name__ == "__main__":
    heap = Heap()
    heap.push(1)
    heap.push(2)
    heap.push(0)
    heap.push(5)
    heap.push(3)
    heap.heap_print()
    heap.pop()
    heap.heap_print()
    print(heap.root())

