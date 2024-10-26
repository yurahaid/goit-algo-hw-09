def find_coins_greedy(coins_amount: int, coin_denom) -> dict[int, int]:
    result = {}
    while coins_amount > 0:
        for coin in coin_denom:
            if coin <= coins_amount:
                if coin not in result:
                    result[coin] = 0

                result[coin] += 1
                coins_amount -= coin
                break


    return result

if __name__ == '__main__':
    print(find_coins_greedy(113,  [50, 25, 10, 5, 2, 1]))