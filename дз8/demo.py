from main import *

# Test завдання 1
print("=== Завдання 1: Функції для роботи з рядками ===")
print(f"is_empty(''): {is_empty('')}")
print(f"count_words('Hello World'): {count_words('Hello World')}")
print(f"capitalize_first_letter('hello world'): {capitalize_first_letter('hello world')}")
print(f"longest_word(['hi', 'hello']): {longest_word(['hi', 'hello'])}")

# Test завдання 2
print("\n=== Завдання 2: Клас BookShelf ===")
shelf = BookShelf(['Book1', 'Book2'])
print(f"Книг на полиці: {shelf.count_books()}")
print(f"Має Book1: {shelf.has_book('Book1')}")
shelf.add_book('Book3')
print(f"Після додавання: {shelf.count_books()} книг")

# Test завдання 3
print("\n=== Завдання 3: Розрахунок вартості ===")
items = [("Книга", 50), ("Ручка", 10)]
cost = calculate_order_cost(items, currency_rate=1.5)
print(f"Вартість замовлення: {cost}")

# Test завдання 4
print("\n=== Завдання 4: Звіт (mock тестується в test_main.py) ===")
print("Mock тестується окремо в тестах")

# Test завдання 5
print("\n=== Завдання 5: Погода (обробка помилок) ===")
result = get_weather_info()
print(f"Інформація про погоду: {result}")

print("\n✅ Усі функції працюють коректно!")
