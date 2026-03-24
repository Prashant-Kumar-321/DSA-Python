import heapq 
# Default: minheap

heap = [] # list

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 22)
heapq.heappush(heap, 13)

print(heap)

# Remove Smallest (pop)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

print(heap)

# Peek Smallest Element
print(heap[0])

# Heapify (Convert list -> Heap)
arr = [4, 8, 3, 1, 9, 13, 4, 8]
heapq.heapify(arr) # O(n)
print(arr)

# Push + Pop
print(heapq.heappushpop(heap, 60))
print(heap) 

# Replace (pop+push)
print(heapq.heapreplace(heap, 70)) # pop smallest, inserts new value
print(heap)

# Q: heappushpop(heap, ele) vs heapreplace(heap, ele)

# heappushpop: Push then Pop in one step
# heapreplace: Pops smallest, insert new value

# Max Heap Trick
max_heap = []
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -9)
heapq.heappush(max_heap, -1)

print(max_heap)
print(-max_heap[0])
print(-heapq.heappop(max_heap))
print(max_heap)

# Priority Queue Example
pq = []

# (2, 'task1'), (3, 'task3'), (8, 'task8')

heapq.heappush(pq, (2, 'task2'))
heapq.heappush(pq, (3, 'task3'))
heapq.heappush(pq, (8, 'task8'))

while pq: 
    print(heapq.heappop(pq), end=" ")

print()


# Notes

# Time Complexity Summary
# Operation	Time
# push	    O(log n)
# pop	    O(log n)
# peek	    O(1)
# heapify	O(n)

# 🔥 When to Use (DSA)
# Use heapq in:
    # Top K elements
    # Dijkstra’s algorithm
    # Merge k sorted arrays
    # Scheduling problems
    # Median finding
    # 🚀 Key Takeaways
    # heapq = Min Heap implementation
    # Fast access to smallest element
    # Works great for priority queue problems

# My Opinion (short)
# If you see:
    # “top k”
    # “smallest/largest efficiently”
    # “priority based processing”
# 👉 Immediately think heap




