
def return_min_idx(l,r,arr):
    if arr[l] > arr[r] : return r
    else: return l


def delete_min_heap(hp_arr):
    elem = hp_arr[0]
    hp_arr[0] = hp_arr[len(hp_arr)-1]
    hp_arr.pop(len(hp_arr)-1)
    cur = 0
    while cur < len(hp_arr):
        left = (cur*2)+1
        right = (cur*2)+2

        if right < len(hp_arr) and left < len(hp_arr):
            mx_idx = return_min_idx(left,right,hp_arr)
            if hp_arr[cur] > hp_arr[left] or hp_arr[cur] > hp_arr[right]:
                hp_arr[cur], hp_arr[mx_idx] = hp_arr[mx_idx], hp_arr[cur]
                cur = mx_idx
            else: break

        elif left < len(hp_arr) and right >= len(hp_arr):
            if hp_arr[cur] > hp_arr[left]:
                hp_arr[cur], hp_arr[left] = hp_arr[left], hp_arr[cur]
                cur = left
            else: break

        else: break

    return elem


# arr = [5,7,18,12]
# print(delete_min_heap(arr))