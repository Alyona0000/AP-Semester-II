"""
Модуль з функціями для роботи з рядками, класом BookShelf, 
та функціями для тестування з використанням mock та patch.
"""


# ============================================================================
# Завдання 1: Функції для роботи з рядками
# ============================================================================

def is_empty(text):
    """
    Перевіряє, чи рядок порожній.
    
    Args:
        text (str): Рядок для перевірки
        
    Returns:
        bool: True, якщо рядок порожній або складається тільки з пробілів
    """
    return len(text.strip()) == 0


def count_words(text):
    """
    Підраховує кількість слів у рядку.
    
    Args:
        text (str): Рядок для аналізу
        
    Returns:
        int: Кількість слів у рядку
    """
    return len(text.split())


def capitalize_first_letter(text):
    """
    Переводить першу літеру кожного слова у велику.
    
    Args:
        text (str): Рядок для обробки
        
    Returns:
        str: Рядок з першими літерами у великому регістрі
    """
    return ' '.join(word.capitalize() for word in text.split())


def longest_word(word_list):
    """
    Знаходить найдовше слово у списку.
    
    Args:
        word_list (list): Список слів
        
    Returns:
        str: Найдовше слово. Якщо список порожній, повертає порожній рядок
    """
    if not word_list:
        return ""
    return max(word_list, key=len)


# ============================================================================
# Завдання 2: Клас BookShelf
# ============================================================================

class BookShelf:
    """
    Клас для управління списком книг.
    
    Атрибути:
        books (list): Список книг у бібліотеці
    """
    
    def __init__(self, books=None):
        """
        Ініціалізує бібліотеку з опціональним початковим списком книг.
        
        Args:
            books (list, optional): Початковий список книг. За замовчуванням []
        """
        self.books = books if books is not None else []
    
    def add_book(self, book):
        """
        Додає книгу до бібліотеки.
        
        Args:
            book (str): Назва книги для додавання
        """
        self.books.append(book)
    
    def remove_book(self, book):
        """
        Видаляє книгу з бібліотеки.
        
        Args:
            book (str): Назва книги для видалення
            
        Raises:
            ValueError: Якщо книга не знайдена
        """
        if book not in self.books:
            raise ValueError(f"Книга '{book}' не знайдена в бібліотеці")
        self.books.remove(book)
    
    def has_book(self, book):
        """
        Перевіряє, чи книга присутня в бібліотеці.
        
        Args:
            book (str): Назва книги для перевірки
            
        Returns:
            bool: True, якщо книга присутня, False в іншому випадку
        """
        return book in self.books
    
    def count_books(self):
        """
        Повертає кількість книг у бібліотеці.
        
        Returns:
            int: Кількість книг
        """
        return len(self.books)


# ============================================================================
# Завдання 3: Функція для розрахунку вартості замовлення з курсом валюти
# ============================================================================

def get_exchange_rate():
    """
    Отримує курс валюти.
    
    Returns:
        float: Курс валюти (для тестування може бути замінений через patch)
    """
    # У реальному коді тут була б запит до API
    return 1.0


def calculate_order_cost(items, currency_rate=None):
    """
    Розраховує повну вартість замовлення з урахуванням курсу валюти.
    
    Args:
        items (list): Список кортежів (назва, ціна)
        currency_rate (float, optional): Курс валюти. Якщо None, використовується get_exchange_rate()
        
    Returns:
        float: Загальна вартість замовлення з врахуванням курсу
    """
    if currency_rate is None:
        currency_rate = get_exchange_rate()
    
    total = sum(price for name, price in items)
    return total * currency_rate


# ============================================================================
# Завдання 4: Функція для створення звіту з mock-сервісом
# ============================================================================

class ReportSaver:
    """
    Сервіс для збереження звітів.
    """
    
    def save(self, report_data):
        """
        Зберігає звіт.
        
        Args:
            report_data (dict): Дані звіту
        """
        # У реальному коді тут виконується збереження
        pass


def create_report(data, saver):
    """
    Створює звіт і передає його в сервіс збереження.
    
    Args:
        data (dict): Дані для звіту
        saver (ReportSaver): Сервіс для збереження звіту
    """
    report = {
        "title": data.get("title", "Report"),
        "content": data.get("content", ""),
        "timestamp": data.get("timestamp", "2026-06-03")
    }
    saver.save(report)


# ============================================================================
# Завдання 5: Функція для отримання інформації про погоду з обробкою помилок
# ============================================================================

def get_weather_data():
    """
    Отримує дані про погоду від зовнішнього сервісу.
    
    Returns:
        str: Інформація про погоду
        
    Raises:
        Exception: Якщо не вдалося отримати дані
    """
    # У реальному коді тут запит до API прогнозу
    raise Exception("Unable to fetch weather data")


def get_weather_info():
    """
    Отримує інформацію про погоду з обробкою помилок.
    
    Returns:
        str: Інформація про погоду або запасне значення при помилці
    """
    try:
        return get_weather_data()
    except Exception:
        return "weather unavailable"
