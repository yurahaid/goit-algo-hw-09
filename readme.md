# Висновки
Результати бенчмарку алгоритмів
```
Average time taken find_min_coins for amount 100: 0.000050 seconds
Average time taken find_coins_greedy for amount 100: 0.000001 seconds
Average time taken find_min_coins for amount 200: 0.000102 seconds
Average time taken find_coins_greedy for amount 200: 0.000001 seconds
Average time taken find_min_coins for amount 300: 0.000156 seconds
Average time taken find_coins_greedy for amount 300: 0.000001 seconds
Average time taken find_min_coins for amount 400: 0.000211 seconds
Average time taken find_coins_greedy for amount 400: 0.000001 seconds
Average time taken find_min_coins for amount 500: 0.000274 seconds
Average time taken find_coins_greedy for amount 500: 0.000002 seconds
Average time taken find_min_coins for amount 600: 0.000327 seconds
Average time taken find_coins_greedy for amount 600: 0.000002 seconds
Average time taken find_min_coins for amount 700: 0.000382 seconds
Average time taken find_coins_greedy for amount 700: 0.000002 seconds
Average time taken find_min_coins for amount 800: 0.000438 seconds
Average time taken find_coins_greedy for amount 800: 0.000002 seconds
Average time taken find_min_coins for amount 900: 0.000494 seconds
Average time taken find_coins_greedy for amount 900: 0.000003 seconds
Average time taken find_min_coins for amount 1000: 0.000549 seconds
Average time taken find_coins_greedy for amount 1000: 0.000003 seconds
```

Хоча обидві імплементації правильно виконують завдання, часова складність різна
жадібний алгоритм має лінійну складність O(n), алгоритм динамічного програмування O(n*m) - де m кількість номіналів монет
це підтвердив наш бенчмарк, жадібний алгоритм на порядок швидше. Також варто зазначити що жадібний алгоритм значно 
простіший в імплементації та розумінні того як він працює. Тому саме під такий тип задача я вважаю, що жадібні алгоритми
підходять найкраще.