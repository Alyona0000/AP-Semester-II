import sqlite3
from datetime import datetime

def create_and_populate_shop_db():
    """Task 1 & 2: Create shop.db and manage products table"""
    
    # Connect to database (creates it if doesn't exist)
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    
    # Add at least 6 products
    products = [
        ('Ноутбук', 'Електроніка', 15000, 5),
        ('Миша', 'Електроніка', 250, 50),
        ('Клавіатура', 'Електроніка', 800, 30),
        ('Монітор', 'Електроніка', 2500, 10),
        ('Крісло', 'Меблі', 3000, 8),
        ('Стіл', 'Меблі', 1200, 12),
        ('Лампа', 'Освітлення', 500, 20),
        ('Вентилятор', 'Освітлення', 600, 15)
    ]
    
    # Clear existing data if any
    cursor.execute('DELETE FROM products')
    
    # Insert products
    cursor.executemany('''
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    ''', products)
    conn.commit()
    
    print("=" * 70)
    print("ЗАВДАННЯ 1: Створення бази даних shop.db")
    print("=" * 70)
    
    # Task 1: Display all products
    print("\n1. Всі товари:")
    print("-" * 70)
    cursor.execute('SELECT * FROM products')
    for row in cursor.fetchall():
        print(f"ID: {row[0]:<3} | Назва: {row[1]:<15} | Категорія: {row[2]:<15} | Ціна: {row[3]:<8} | Кількість: {row[4]:<5}")
    
    # Task 1: Products more expensive than 1000
    print("\n2. Товари дорожчі за 1000:")
    print("-" * 70)
    cursor.execute('SELECT * FROM products WHERE price > 1000 ORDER BY price DESC')
    for row in cursor.fetchall():
        print(f"ID: {row[0]:<3} | Назва: {row[1]:<15} | Категорія: {row[2]:<15} | Ціна: {row[3]:<8} | Кількість: {row[4]:<5}")
    
    # Task 1: Products from selected category
    print("\n3. Товари з категорії 'Електроніка':")
    print("-" * 70)
    cursor.execute('SELECT * FROM products WHERE category = ? ORDER BY price DESC', ('Електроніка',))
    for row in cursor.fetchall():
        print(f"ID: {row[0]:<3} | Назва: {row[1]:<15} | Категорія: {row[2]:<15} | Ціна: {row[3]:<8} | Кількість: {row[4]:<5}")
    
    # Task 1: Products sorted by price descending
    print("\n4. Товари, відсортовані за ціною (від більшої до меншої):")
    print("-" * 70)
    cursor.execute('SELECT * FROM products ORDER BY price DESC')
    for row in cursor.fetchall():
        print(f"ID: {row[0]:<3} | Назва: {row[1]:<15} | Категорія: {row[2]:<15} | Ціна: {row[3]:<8} | Кількість: {row[4]:<5}")
    
    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 2: Оновлення та видалення даних")
    print("=" * 70)
    
    # Task 2: Update price of one product
    print("\n1. Змінення ціни товару 'Миша' з 250 на 300:")
    cursor.execute('UPDATE products SET price = 300 WHERE name = ?', ('Миша',))
    conn.commit()
    print("   ✓ Ціна оновлена")
    
    # Task 2: Update quantity of one product
    print("\n2. Змінення кількості товару 'Клавіатура' на складі з 30 на 45:")
    cursor.execute('UPDATE products SET quantity = 45 WHERE name = ?', ('Клавіатура',))
    conn.commit()
    print("   ✓ Кількість оновлена")
    
    # Task 2: Delete a product
    print("\n3. Видалення товару 'Вентилятор':")
    cursor.execute('DELETE FROM products WHERE name = ?', ('Вентилятор',))
    conn.commit()
    print("   ✓ Товар видалений")
    
    # Task 2: Display updated products
    print("\n4. Оновлений список товарів:")
    print("-" * 70)
    cursor.execute('SELECT * FROM products ORDER BY id')
    for row in cursor.fetchall():
        print(f"ID: {row[0]:<3} | Назва: {row[1]:<15} | Категорія: {row[2]:<15} | Ціна: {row[3]:<8} | Кількість: {row[4]:<5}")
    
    # Task 2: Calculate statistics
    print("\n5. Статистика:")
    print("-" * 70)
    
    cursor.execute('SELECT COUNT(*) FROM products')
    count = cursor.fetchone()[0]
    print(f"   • Кількість товарів: {count}")
    
    cursor.execute('SELECT AVG(price) FROM products')
    avg_price = cursor.fetchone()[0]
    print(f"   • Середня ціна: {avg_price:.2f}")
    
    cursor.execute('SELECT MAX(price), name FROM products')
    result = cursor.fetchone()
    print(f"   • Найдорожчий товар: {result[1]} (ціна: {result[0]})")
    
    cursor.execute('SELECT MIN(price), name FROM products')
    result = cursor.fetchone()
    print(f"   • Найдешевший товар: {result[1]} (ціна: {result[0]})")
    
    conn.close()
    print("\n" + "=" * 70)
    print("Готово! База даних shop.db успішно створена.")
    print("=" * 70)

if __name__ == '__main__':
    create_and_populate_shop_db()
