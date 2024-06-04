



def solve(k: int, number_list: list, temp: list=[]):
    """
        params:
            k: expected total sum of the list
            number_list: list of given numbers
            temp: list that store data of the each part

        returns:
            None
    
    """
    if sum(temp) == k: 
        for num in temp: print(num, end=' ')
        print()
        return
    elif sum(temp) > k or not number_list: return
    solve(k, number_list[1:], temp)
    temp.append(number_list[0])
    solve(k, number_list[1:], temp)
    temp.pop()


solve(21, [5, 6, 10, 11, 16])

