def find_min_coins(coins_amount, coin_denom):
    min_coins = [coins_amount + 1] * (coins_amount + 1)
    min_coins[0] = 0

    coin_combinations = [{} for _ in range(coins_amount + 1)]

    for amount in range(1, coins_amount + 1):
        for coin in coin_denom:
            if coin <= amount:
                # reuse already calculated value for {amount-coin} value, because it should be calculated before
                if min_coins[amount] > min_coins[amount - coin] + 1:
                    min_coins[amount] = min_coins[amount - coin] + 1
                    coin_combinations[amount] = coin_combinations[amount - coin].copy()
                    if coin in coin_combinations[amount]:
                        coin_combinations[amount][coin] += 1
                    else:
                        coin_combinations[amount][coin] = 1

    return coin_combinations[coins_amount]



if __name__ == '__main__':
    print(find_min_coins(113,  [50, 25, 10, 5, 2, 1]))
