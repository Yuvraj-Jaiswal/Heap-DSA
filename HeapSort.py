from Deletion_in_Min_Heap import delete_min_heap
from Min_Heapify_Algorithm_Implimentation import heapify_min

def HeapSort(arr):
    hp_arr = heapify_min(arr)
    sorted_arr = []
    for _ in range(len(arr)):
        elm = delete_min_heap(hp_arr)
        sorted_arr.append(elm)

    return sorted_arr

print(HeapSort([2,7,3,9,10,50]))