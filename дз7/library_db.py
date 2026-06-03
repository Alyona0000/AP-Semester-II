import sqlite3

def create_and_populate_library_db():
    """Task 3 & 4: Create library.db with authors and books tables"""
    
    # Connect to database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Create authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    ''')
    
    # Create books table with foreign key to authors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            pages INTEGER NOT NULL,
            author_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    ''')
    conn.commit()
    
    # Add authors (at least 4)
    authors = [
        ('Леонід Українка', 'Україна'),
        ('Тарас Шевченко', 'Україна'),
        ('Джордж Оруелл', 'Велика Британія'),
        ('Франц Кафка', 'Чеська Республіка'),
        ('Джейн Остен', 'Велика Британія'),
        ('Михайло Булгаков', 'Росія')
    ]
    
    # Clear existing data if any
    cursor.execute('DELETE FROM books')
    cursor.execute('DELETE FROM authors')
    
    # Insert authors
    cursor.executemany('''
        INSERT INTO authors (name, country)
        VALUES (?, ?)
    ''', authors)
    conn.commit()
    
    # Add books (at least 8)
    books = [
        ('Лісова пісня', 1911, 120, 1),
        ('Мертві душі', 1842, 512, 2),
        ('1984', 1949, 328, 3),
        ('Процес', 1925, 240, 4),
        ('Гордість та упередженість', 1813, 279, 5),
        ('Майстер і Маргарита', 1967, 480, 6),
        ('Вічні пісні', 1899, 185, 1),
        ('Кобзар', 1840, 203, 2),
        ('О дивний новий світ', 1932, 288, 3),
        ('Замок', 1926, 352, 4),
        ('Емма', 1815, 432, 5),
        ('Записки на манжетах', 1923, 98, 6)
    ]
    
    # Insert books
    cursor.executemany('''
        INSERT INTO books (title, year, pages, author_id)
        VALUES (?, ?, ?, ?)
    ''', books)
    conn.commit()
    
    print("=" * 90)
    print("ЗАВДАННЯ 3: Створення бази даних library.db")
    print("=" * 90)
    
    print("\n1. Таблиця авторів:")
    print("-" * 90)
    cursor.execute('SELECT * FROM authors')
    print(f"{'ID':<5} | {'Ім\'я автора':<30} | {'Країна':<20}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<20}")
    
    print("\n2. Таблиця книг:")
    print("-" * 90)
    cursor.execute('SELECT * FROM books')
    print(f"{'ID':<5} | {'Назва книги':<35} | {'Рік':<6} | {'Сторінок':<10} | {'ID автора':<10}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<5} | {row[1]:<35} | {row[2]:<6} | {row[3]:<10} | {row[4]:<10}")
    
    print("\n" + "=" * 90)
    print("ЗАВДАННЯ 4: Запити з об'єднанням таблиць")
    print("=" * 90)
    
    # Task 4.1: All books with authors
    print("\n1. Всі книги разом з іменами авторів:")
    print("-" * 90)
    cursor.execute('''
        SELECT b.title, b.year, b.pages, a.name, a.country
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.year
    ''')
    print(f"{'Книга':<35} | {'Рік':<6} | {'Сторінок':<10} | {'Автор':<25} | {'Країна':<15}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<35} | {row[1]:<6} | {row[2]:<10} | {row[3]:<25} | {row[4]:<15}")
    
    # Task 4.2: Books by selected author
    print("\n2. Всі книги автора 'Леонід Українка':")
    print("-" * 90)
    cursor.execute('''
        SELECT b.title, b.year, b.pages, a.name
        FROM books b
        JOIN authors a ON b.author_id = a.id
        WHERE a.name = ?
        ORDER BY b.year
    ''', ('Леонід Українка',))
    print(f"{'Книга':<35} | {'Рік':<6} | {'Сторінок':<10} | {'Автор':<25}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<35} | {row[1]:<6} | {row[2]:<10} | {row[3]:<25}")
    
    # Task 4.3: Books sorted by year
    print("\n3. Всі книги, відсортовані за роком видання:")
    print("-" * 90)
    cursor.execute('''
        SELECT b.title, b.year, b.pages, a.name
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.year ASC
    ''')
    print(f"{'Книга':<35} | {'Рік':<6} | {'Сторінок':<10} | {'Автор':<25}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<35} | {row[1]:<6} | {row[2]:<10} | {row[3]:<25}")
    
    # Task 4.4: Book count per author
    print("\n4. Кількість книг у кожного автора:")
    print("-" * 90)
    cursor.execute('''
        SELECT a.name, a.country, COUNT(b.id) as book_count
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.id, a.name, a.country
        ORDER BY book_count DESC
    ''')
    print(f"{'Автор':<30} | {'Країна':<20} | {'Кількість книг':<15}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<30} | {row[1]:<20} | {row[2]:<15}")
    
    # Task 4.5: Average pages per author
    print("\n5. Середня кількість сторінок для кожного автора:")
    print("-" * 90)
    cursor.execute('''
        SELECT a.name, COUNT(b.id) as book_count, AVG(b.pages) as avg_pages
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.id, a.name
        ORDER BY avg_pages DESC
    ''')
    print(f"{'Автор':<30} | {'Кількість книг':<15} | {'Середня кількість сторінок':<30}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(f"{row[0]:<30} | {row[1]:<15} | {row[2]:<30.2f}")
    
    # Task 4.6: Author with most books
    print("\n6. Автор, у якого найбільше книг:")
    print("-" * 90)
    cursor.execute('''
        SELECT a.name, a.country, COUNT(b.id) as book_count
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.id, a.name, a.country
        ORDER BY book_count DESC
        LIMIT 1
    ''')
    row = cursor.fetchone()
    print(f"Автор: {row[0]}")
    print(f"Країна: {row[1]}")
    print(f"Кількість книг: {row[2]}")
    
    conn.close()
    print("\n" + "=" * 90)
    print("Готово! База даних library.db успішно створена.")
    print("=" * 90)

if __name__ == '__main__':
    create_and_populate_library_db()
