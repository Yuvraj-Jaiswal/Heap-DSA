def return_min_idx(l,r,arr_c):
    if arr_c[l] < arr_c[r] : return l
    else: return r

def heapify_min(arr):
    length = len(arr)
    st = (length//2)-1
    en = 0
    for idx in range(st,en-1,-1):
        cur = idx

        while True:
            left = cur*2 + 1
            right = cur*2 + 2

            if left < len(arr) and right < len(arr):
                if arr[cur] > arr[left] or arr[cur] > arr[right]:
                    min_idx = return_min_idx(left,right,arr)
                    arr[cur] , arr[min_idx] = arr[min_idx] , arr[cur]
                    cur = min_idx
                else:break

            elif left < len(arr) and right >= len(arr):
                if arr[cur] > arr[left]:
                    arr[cur], arr[left] = arr[left], arr[cur]
                    cur = left
                else:break

            else:break

    return arr


# print(heapify_min([10,2,30,4,5,6,14,12]))
