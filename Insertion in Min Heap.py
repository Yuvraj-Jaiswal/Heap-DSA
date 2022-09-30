
def insert_min_heap(hp_arr,elm):
    hp_arr.append(elm)
    cur = len(hp_arr)-1
    while cur > 0:
        parent = (cur-1)//2
        if hp_arr[parent] > hp_arr[cur]:
            hp_arr[parent] , hp_arr[cur] = hp_arr[cur] , hp_arr[parent]
            cur = parent
        else:
            return hp_arr
    return hp_arr


arr = [5,10,20]
print(insert_min_heap(arr,7))