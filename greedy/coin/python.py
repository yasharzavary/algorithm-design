# NOTE: i write better version that coins ins't sorted

def coin(coins: list, amount: int) -> dict:
    coin_number = dict()
    while(True):
        if amount == 0: return coin_number
        elif not coins: return -1
        temp = max(coins)
        if temp <= amount:
            amount -= temp
            if temp in coin_number: coin_number[temp]+=1
            else: coin_number[temp]=1
        else: coins.remove(temp)


coin_list = list(map(int , input().split()))
amount = int(input())

result = coin(coin_list, amount)
if result == -1: print(-1)
else:
    for x, y in result.items():
        print(f'{x}\t{y}')
