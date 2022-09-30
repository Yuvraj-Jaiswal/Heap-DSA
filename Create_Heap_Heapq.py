import heapq

heap_list = []

heapq.heappush(heap_list,10)
print(heap_list)

heapq.heappush(heap_list,12)
print(heap_list)

heapq.heappush(heap_list,5)
print(heap_list)

heapq.heappush(heap_list,11)
print(heap_list)

print(heapq.heappop(heap_list))
print(heapq.heappop(heap_list))