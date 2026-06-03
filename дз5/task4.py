"""
Task 4: Greedy Algorithm vs Brute Force (Жадібний алгоритм і повний перебір)
Задача про здачу: монети {1, 3, 4}, цільова сума 6.
Порівняти жадібний підхід з повним перебором.
"""

def greedy_coin_change(coins, target):
    """
    Жадібний підхід: на кожному кроці беремо найбільшу монету, яка підходить.
    
    Args:
        coins: список номіналів монет
        target: цільова сума
    
    Returns:
        список монет, обраних жадібним алгоритмом
    """
    # Сортуємо монети у спадному порядку
    sorted_coins = sorted(coins, reverse=True)
    result = []
    remaining = target
    
    for coin in sorted_coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return result

def brute_force_coin_change(coins, target, memo=None):
    """
    Повний перебір: знаходимо комбінацію з мінімальною кількістю монет.
    
    Args:
        coins: список номіналів монет
        target: цільова сума
        memo: словник для мемоізації
    
    Returns:
        список монет для оптимальної комбінації
    """
    if memo is None:
        memo = {}
    
    if target == 0:
        return []
    if target < 0:
        return None
    
    if target in memo:
        return memo[target]
    
    min_coins = None
    
    for coin in coins:
        remainder = target - coin
        result = brute_force_coin_change(coins, remainder, memo)
        
        if result is not None:
            current = [coin] + result
            if min_coins is None or len(current) < len(min_coins):
                min_coins = current
    
    memo[target] = min_coins
    return min_coins

def solve_task4():
    """Порівнює жадібний і повний перебір"""
    
    coins = [1, 3, 4]
    target = 6
    
    greedy_result = greedy_coin_change(coins, target)
    brute_force_result = brute_force_coin_change(coins, target)
    
    return coins, target, greedy_result, brute_force_result

def main():
    print("=" * 60)
    print("Завдання 4: Жадібний алгоритм і повний перебір")
    print("=" * 60)
    print()
    
    coins, target, greedy_result, brute_force_result = solve_task4()
    
    print(f"Монети: {coins}")
    print(f"Цільова сума: {target}")
    print()
    
    # Жадібний результат
    print("1. ЖАДІБНИЙ ПІДХІД:")
    print(f"   Вибрані монети: {greedy_result}")
    print(f"   Кількість монет: {len(greedy_result)}")
    greedy_sum = sum(greedy_result)
    print(f"   Сума: {greedy_sum}")
    print()
    
    # Результат повного перебору
    print("2. ПОВНИЙ ПЕРЕБІР (оптимальний):")
    print(f"   Вибрані монети: {brute_force_result}")
    print(f"   Кількість монет: {len(brute_force_result)}")
    brute_force_sum = sum(brute_force_result)
    print(f"   Сума: {brute_force_sum}")
    print()
    
    # Порівняння
    print("3. ПОРІВНЯННЯ:")
    print(f"   Жадібний використав: {len(greedy_result)} монет")
    print(f"   Повний перебір використав: {len(brute_force_result)} монет")
    
    if len(greedy_result) == len(brute_force_result):
        print(f"   ✓ Обидва підходи дають оптимальний результат")
    else:
        diff = len(greedy_result) - len(brute_force_result)
        print(f"   ✗ Жадібний неоптимальний! На {diff} монет більше")
    print()
    
    # Висновок
    print("4. ВИСНОВОК:")
    print("   Жадібний алгоритм НЕ ЗАВЖДИ дає оптимальний результат!")
    print()
    print("   Пояснення:")
    print(f"   - Жадібний дав: {greedy_result} = {greedy_sum}")
    print(f"   - Оптимальний: {brute_force_result} = {brute_force_sum}")
    print()
    print("   Набір монет {1, 3, 4} НЕ є канонічним для жадібного алгоритму.")
    print("   На канонічній множині {1, 5, 10, 25} жадібний завжди оптимальний.")
    print("   Але для довільних наборів потрібно використовувати динамічне")
    print("   програмування або повний перебір.")
    print()

if __name__ == '__main__':
    main()
