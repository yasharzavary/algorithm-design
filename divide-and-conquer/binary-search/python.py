

def search(target, number_list, i, j):
    """
        params:
            target: number we want to find
            number_list: out given number list
            i: index of first element of the number list that you want to go search
            j: index of last element of the number last that you want to search there
        
        returns:
            -1 if we can't find the number
            index of the element if we find it
    """
    if j < i: return -1 # base case, return if number list finish

    temp = (i + j) // 2 # middle index
    # finding and checking proccess
    if number_list[temp] == target: return temp
    elif number_list[temp] > target: return search(target, number_list, i, temp-1)
    else: return search(target, number_list, temp+1, j)

# inputs
num_list = list(map(int, input().split()))
target = int(input())


print(search(target, num_list, 0, len(num_list)-1))
