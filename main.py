import timeit

from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def benchmark_find_min_coins():
    coins = [50, 25, 10, 5, 2, 1]
    test_amounts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for amount in test_amounts:
        time_taken = timeit.timeit(lambda: find_min_coins(amount, coins), number=10)
        print(f"Average time taken find_min_coins for amount {amount}: {time_taken / 10:.6f} seconds")

        time_taken = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=10)
        print(f"Average time taken find_coins_greedy for amount {amount}: {time_taken / 10:.6f} seconds")

benchmark_find_min_coins()
