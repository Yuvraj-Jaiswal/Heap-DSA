def return_max_idx(l,r,arr_c):
    if arr_c[l] > arr_c[r] : return l
    else: return r

def delete_max_heap(hp_arr):
    elem = hp_arr[0]
    hp_arr[0] = hp_arr[len(hp_arr)-1]
    hp_arr.pop(len(hp_arr)-1)
    cur = 0
    while True:
        left = cur*2 + 1
        right = cur*2 + 2

        if left < len(hp_arr) and right < len(hp_arr):
            if hp_arr[cur] < hp_arr[left] or hp_arr[cur] < hp_arr[right]:
                max_idx = return_max_idx(left,right,hp_arr)
                hp_arr[cur] , hp_arr[max_idx] = hp_arr[max_idx] , hp_arr[cur]
                cur = max_idx
            else: break

        elif left < len(hp_arr) and right >= len(hp_arr):
            if hp_arr[cur] < hp_arr[left]:
                hp_arr[cur] , hp_arr[left] = hp_arr[left] , hp_arr[cur]
                cur = left

        else: break

    return elem

# print(delete_max_heap([30,12,14,4,5,6,10,2]))