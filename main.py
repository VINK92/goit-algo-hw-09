def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    max_value = float('inf')
    dp = [0] + [max_value] * amount
    last_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_used[i] = coin

    result = {}
    while amount > 0:
        coin = last_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


amount = 113

# Використання жадібного алгоритму
greedy_result = find_coins_greedy(amount)
print("Жадібний алгоритм:", greedy_result)

# Використання алгоритму динамічного програмування
dp_result = find_min_coins(amount)
print("Динамічне програмування:", dp_result)
