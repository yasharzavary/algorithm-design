
def merge(number_list: list, i: int, k: int, j: int) -> None:
    """
        params:
            number_list: our main number list
            i: start position of first element
            k: middle of list
            j: last element of the list
        returns:
            None
    """
    start = i # point to first, so we can replace to main list in last
    temp_k = k+1
    temp = [] # temp list that contain sorted part
    while temp_k <= j and i <= k: # adding with sorted form
        while i <= k and number_list[i] <= number_list[temp_k]:
             temp.append(number_list[i])
             i += 1
        while temp_k <= j and number_list[temp_k] <= number_list[i]:
            temp.append(number_list[temp_k])
            temp_k += 1
        
    while temp_k <= j: # add remained elements
            temp.append(number_list[temp_k])
            temp_k += 1
    while i <= k:
            temp.append(number_list[i])
            i += 1
    number_list[start:j+1] = temp # replace


def  merge_sort(number_list: list, i: int, j: int) -> None:
    """
        params:
            number_list: contain main numbers
            i: first element's index
            j: last element's index
        
        returns:
            None
    """
    if i==j: return
    k = (i+j)//2
    # dividing part
    merge_sort(number_list, i, k)
    merge_sort(number_list, k+1, j)
    merge(number_list, i, k, j) # sort part


candidate_list = list(map(int, input().split()))
merge_sort(candidate_list, 0, len(candidate_list)-1)
print(candidate_list)


