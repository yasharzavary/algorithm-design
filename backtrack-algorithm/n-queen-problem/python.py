
def validator(queens):
    if len(queens) == 0 or len(queens) == 1: return True
    temp_row = queens[-1]
    temp_col = len(queens)-1
    for j in range(len(queens) - 1):
        if queens[j] == temp_row or abs(temp_col - j) == abs(queens[j] - temp_row): return False
    return True

def solve(n: int, i: int = 0, queens: list = []):
    """
        params:
            n: number of queens,
            i: queen index,
            queens: list for store queens place,

        return:
            one form for n-queen answer
    """
    if validator(queens):
        if i == n: return True 
        for j in range(n):
            queens.append(j)
            find = solve(n, i+1, queens)
            if find and i == 0: return queens
            elif find: return True
    queens.pop()


print(solve(8))
