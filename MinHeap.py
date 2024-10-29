class MinHeap:
    def __init__(self):
        self.heap=[]
    def pushheap (self, item):
        self.heap.append(item)
        self._heapify_upward(len(self.heap)-1)
    def popheap(self):
        if len(self.heap)==0:
            raise IndexError("cannot pop from emty heap")
        
        return_value=self.heap[0]
        last=self.heap.pop()
        if len(self.heap):
            self.heap[0]=last
            self._heapify_downward(0)
        return return_value

        
    def peek(self):
        if not len(self.heap): raise IndexError("empty list")
        return self.heap[0]
    def _heapify_upward(self, index):
        parent=(index-1)//2
        while index>0 and self.heap[index]< self.heap[parent]:
            self.heap[index], self.heap[parent]=self.heap[parent],self.heap[index]
            index=parent
            parent=(index-1)//2
    def _heapify_downward(self,index):
        length=len(self.heap)
        lchild , rchild=2*index+1,2*index+2
        smallest=index
        if lchild<length and self.heap[lchild] <self.heap[smallest]:
            smallest=lchild
        if rchild<length and self.heap[rchild]<self.heap[smallest]:
            smallest=rchild
        if smallest!=index:
            self.heap[index], self.heap[smallest]=self.heap[smallest],self.heap[index]
            self._heapify_downward(smallest)
            
min_heap = MinHeap()
min_heap.pushheap(10)
min_heap.pushheap(5)
min_heap.pushheap(20)
print("Min-Heap peek:", min_heap.peek())  # Output: 5
print("Min-Heap pop:", min_heap.popheap())    # Output: 5
print("Min-Heap peek:", min_heap.peek())  # Output: 10

