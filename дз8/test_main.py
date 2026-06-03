"""
Модуль з тестами для функцій та класу BookShelf.
Використовуються unittest, mock, patch та side_effect.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock, call
from main import (
    is_empty, count_words, capitalize_first_letter, longest_word,
    BookShelf, calculate_order_cost, create_report, ReportSaver,
    get_weather_info, get_weather_data
)


#======================
# Тести для Завдання 1: Функції для роботи з рядками
# ============================================================================

class TestStringFunctions(unittest.TestCase):
    """Тести для функцій роботи з рядками."""
    
    # Тести для is_empty()
    def test_is_empty_with_empty_string(self):
        """Тест перевірки пустого рядка."""
        self.assertTrue(is_empty(""))
    
    def test_is_empty_with_spaces(self):
        """Тест перевірки рядка з тільки пробілами."""
        self.assertTrue(is_empty("   "))
    
    def test_is_empty_with_tabs_and_newlines(self):
        """Тест перевірки рядка з пробільними символами."""
        self.assertTrue(is_empty("\t\n  "))
    
    def test_is_empty_with_text(self):
        """Тест перевірки непустого рядка."""
        self.assertFalse(is_empty("Hello"))
    
    def test_is_empty_with_single_char(self):
        """Тест перевірки рядка з одним символом."""
        self.assertFalse(is_empty("a"))
    
    # Тести для count_words()
    def test_count_words_empty_string(self):
        """Тест підрахунку слів у пустому рядку."""
        self.assertEqual(count_words(""), 0)
    
    def test_count_words_single_word(self):
        """Тест підрахунку одного слова."""
        self.assertEqual(count_words("Hello"), 1)
    
    def test_count_words_multiple_words(self):
        """Тест підрахунку кількох слів."""
        self.assertEqual(count_words("Hello World Python"), 3)
    
    def test_count_words_with_multiple_spaces(self):
        """Тест підрахунку слів з кількома пробілами."""
        self.assertEqual(count_words("Hello  World   Python"), 3)
    
    def test_count_words_with_tabs(self):
        """Тест підрахунку слів з табуляціями."""
        self.assertEqual(count_words("Hello\tWorld\tPython"), 3)
    
    # Тести для capitalize_first_letter()
    def test_capitalize_first_letter_single_word(self):
        """Тест капіталізації одного слова."""
        self.assertEqual(capitalize_first_letter("hello"), "Hello")
    
    def test_capitalize_first_letter_multiple_words(self):
        """Тест капіталізації кількох слів."""
        self.assertEqual(
            capitalize_first_letter("hello world python"),
            "Hello World Python"
        )
    
    def test_capitalize_first_letter_already_capitalized(self):
        """Тест капіталізації вже капіталізованого рядка."""
        self.assertEqual(capitalize_first_letter("Hello World"), "Hello World")
    
    def test_capitalize_first_letter_mixed_case(self):
        """Тест капіталізації змішаного регістру."""
        self.assertEqual(
            capitalize_first_letter("hELLO wORLD"),
            "Hello World"
        )
    
    def test_capitalize_first_letter_with_numbers(self):
        """Тест капіталізації рядка з цифрами."""
        self.assertEqual(capitalize_first_letter("123 test"), "123 Test")
    
    # Тести для longest_word()
    def test_longest_word_empty_list(self):
        """Тест пошуку найдовшого слова в пустому списку."""
        self.assertEqual(longest_word([]), "")
    
    def test_longest_word_single_word(self):
        """Тест пошуку найдовшого слова з одним словом."""
        self.assertEqual(longest_word(["hello"]), "hello")
    
    def test_longest_word_multiple_words(self):
        """Тест пошуку найдовшого слова з кількома словами."""
        self.assertEqual(longest_word(["hi", "hello", "world"]), "hello")
    
    def test_longest_word_equal_length(self):
        """Тест пошуку найдовшого слова з рівною довжиною."""
        # max() повертає перше знайдене найдовше слово
        result = longest_word(["cat", "dog", "ant"])
        self.assertIn(result, ["cat", "dog", "ant"])
        self.assertEqual(len(result), 3)
    
    def test_longest_word_very_long(self):
        """Тест пошуку найдовшого слова з дуже довгим словом."""
        words = ["short", "supercalifragilisticexpialidocious", "mid"]
        self.assertEqual(longest_word(words), "supercalifragilisticexpialidocious")


# ======================================
# Тести для Завдання 2: Клас BookShelf
# ============================================================================

class TestBookShelf(unittest.TestCase):
    """Тести для класу BookShelf."""
    
    def setUp(self):
        """Підготовка тестових даних перед кожним тестом."""
        self.initial_books = ["Python 101", "Web Development", "Data Science"]
        self.shelf = BookShelf(self.initial_books.copy())
    
    def test_init_with_books(self):
        """Тест ініціалізації з початковим списком книг."""
        self.assertEqual(self.shelf.books, self.initial_books)
    
    def test_init_without_books(self):
        """Тест ініціалізації без книг."""
        empty_shelf = BookShelf()
        self.assertEqual(empty_shelf.books, [])
    
    def test_add_book(self):
        """Тест додавання книги."""
        self.shelf.add_book("New Book")
        self.assertIn("New Book", self.shelf.books)
        self.assertEqual(self.shelf.count_books(), 4)
    
    def test_add_multiple_books(self):
        """Тест додавання кількох книг."""
        self.shelf.add_book("Book 4")
        self.shelf.add_book("Book 5")
        self.assertEqual(self.shelf.count_books(), 5)
    
    def test_add_duplicate_book(self):
        """Тест додавання дублікату книги."""
        initial_count = self.shelf.count_books()
        self.shelf.add_book("Python 101")  # Вже існує
        # Система дозволяє додавати дублікати
        self.assertEqual(self.shelf.count_books(), initial_count + 1)
    
    def test_remove_book_exists(self):
        """Тест видалення існуючої книги."""
        self.shelf.remove_book("Python 101")
        self.assertNotIn("Python 101", self.shelf.books)
        self.assertEqual(self.shelf.count_books(), 2)
    
    def test_remove_book_not_exists(self):
        """Тест видалення неіснуючої книги."""
        with self.assertRaises(ValueError):
            self.shelf.remove_book("Non-existent Book")
    
    def test_remove_multiple_books(self):
        """Тест видалення кількох книг."""
        self.shelf.remove_book("Python 101")
        self.shelf.remove_book("Web Development")
        self.assertEqual(self.shelf.count_books(), 1)
        self.assertIn("Data Science", self.shelf.books)
    
    def test_has_book_exists(self):
        """Тест перевірки наявності існуючої книги."""
        self.assertTrue(self.shelf.has_book("Python 101"))
    
    def test_has_book_not_exists(self):
        """Тест перевірки наявності неіснуючої книги."""
        self.assertFalse(self.shelf.has_book("Non-existent"))
    
    def test_has_book_after_add(self):
        """Тест перевірки книги після додавання."""
        self.shelf.add_book("New Book")
        self.assertTrue(self.shelf.has_book("New Book"))
    
    def test_has_book_after_remove(self):
        """Тест перевірки книги після видалення."""
        self.shelf.remove_book("Python 101")
        self.assertFalse(self.shelf.has_book("Python 101"))
    
    def test_count_books_initial(self):
        """Тест підрахунку початкової кількості книг."""
        self.assertEqual(self.shelf.count_books(), 3)
    
    def test_count_books_after_operations(self):
        """Тест підрахунку книг після операцій."""
        self.shelf.add_book("Book 4")
        self.shelf.add_book("Book 5")
        self.shelf.remove_book("Python 101")
        self.assertEqual(self.shelf.count_books(), 4)


# =======================================
# Тести для Завдання 3: Функція з patch для курсу валюти
# ============================================================================

class TestOrderCostWithPatch(unittest.TestCase):
    """Тести для функції calculate_order_cost з використанням patch."""
    
    def test_calculate_order_cost_default_rate(self):
        """Тест розрахунку вартості з використанням rate=1.0."""
        items = [("Book", 10), ("Pen", 5), ("Notebook", 8)]
        cost = calculate_order_cost(items, currency_rate=1.0)
        self.assertEqual(cost, 23.0)
    
    def test_calculate_order_cost_with_patch_rate_2(self):
        """Тест з patch: курс = 2.0."""
        items = [("Book", 10), ("Pen", 5)]
        with patch('main.get_exchange_rate', return_value=2.0):
            cost = calculate_order_cost(items)
            self.assertEqual(cost, 30.0)  # (10 + 5) * 2
    
    def test_calculate_order_cost_with_patch_rate_05(self):
        """Тест з patch: курс = 0.5."""
        items = [("Book", 20), ("Pen", 10)]
        with patch('main.get_exchange_rate', return_value=0.5):
            cost = calculate_order_cost(items)
            self.assertEqual(cost, 15.0)  # (20 + 10) * 0.5
    
    def test_calculate_order_cost_with_patch_rate_125(self):
        """Тест з patch: курс = 1.25."""
        items = [("Keyboard", 100)]
        with patch('main.get_exchange_rate', return_value=1.25):
            cost = calculate_order_cost(items)
            self.assertEqual(cost, 125.0)  # 100 * 1.25
    
    def test_calculate_order_cost_empty_items(self):
        """Тест з patch для пустого списку товарів."""
        items = []
        with patch('main.get_exchange_rate', return_value=2.0):
            cost = calculate_order_cost(items)
            self.assertEqual(cost, 0.0)
    
    def test_calculate_order_cost_multiple_patch_calls(self):
        """Тест декількох викликів з patch."""
        items = [("Item", 100)]
        test_rates = [1.0, 2.0, 0.5, 1.5]
        expected_costs = [100.0, 200.0, 50.0, 150.0]
        
        for rate, expected_cost in zip(test_rates, expected_costs):
            with patch('main.get_exchange_rate', return_value=rate):
                cost = calculate_order_cost(items)
                self.assertEqual(cost, expected_cost)


# =======================================
# Тести для Завдання 4: Mock-об'єкт для сервісу збереження
# ============================================================================

class TestCreateReportWithMock(unittest.TestCase):
    """Тести для функції create_report з використанням mock."""
    
    def test_create_report_calls_save_once(self):
        """Тест перевірки, що save() викликається один раз."""
        mock_saver = Mock()
        report_data = {"title": "Sales Report", "content": "Q1 Results"}
        
        create_report(report_data, mock_saver)
        
        # Перевірка, що save() був викликаний один раз
        mock_saver.save.assert_called_once()
    
    def test_create_report_calls_save_with_correct_data(self):
        """Тест перевірки правильних даних при виклику save()."""
        mock_saver = Mock()
        report_data = {"title": "Monthly Report", "content": "Performance data"}
        
        create_report(report_data, mock_saver)
        
        # Отримання аргументів виклику
        called_report = mock_saver.save.call_args[0][0]
        
        self.assertEqual(called_report["title"], "Monthly Report")
        self.assertEqual(called_report["content"], "Performance data")
    
    def test_create_report_with_minimal_data(self):
        """Тест create_report з мінімальними даними."""
        mock_saver = Mock()
        report_data = {}
        
        create_report(report_data, mock_saver)
        
        called_report = mock_saver.save.call_args[0][0]
        
        self.assertEqual(called_report["title"], "Report")  # Default value
        self.assertEqual(called_report["content"], "")  # Default value
    
    def test_create_report_verify_save_called_with_dict(self):
        """Тест перевірки, що save() викликається з словником."""
        mock_saver = Mock()
        report_data = {
            "title": "Test Report",
            "content": "Test Content",
            "timestamp": "2026-06-03"
        }
        
        create_report(report_data, mock_saver)
        
        # Перевірка, що був переданий словник
        call_args = mock_saver.save.call_args
        called_report = call_args[0][0]
        
        self.assertIsInstance(called_report, dict)
        self.assertIn("title", called_report)
        self.assertIn("content", called_report)
        self.assertIn("timestamp", called_report)
    
    def test_create_report_multiple_calls_different_data(self):
        """Тест кількох викликів create_report з різними даними."""
        mock_saver = Mock()
        
        report1 = {"title": "Report 1"}
        report2 = {"title": "Report 2"}
        
        create_report(report1, mock_saver)
        create_report(report2, mock_saver)
        
        # Перевірка, що save() був викликаний двічі
        self.assertEqual(mock_saver.save.call_count, 2)


# ========================================
# Тести для Завдання 5: side_effect для обробки помилок
# ============================================================================

class TestWeatherInfoWithSideEffect(unittest.TestCase):
    """Тести для функції get_weather_info з використанням side_effect."""
    
    def test_weather_info_success(self):
        """Тест успішного отримання інформації про погоду."""
        with patch('main.get_weather_data', return_value="Sunny, 25°C"):
            result = get_weather_info()
            self.assertEqual(result, "Sunny, 25°C")
    
    def test_weather_info_exception_returns_unavailable(self):
        """Тест обробки помилки - повертає запасне значення."""
        with patch('main.get_weather_data', side_effect=Exception("API Error")):
            result = get_weather_info()
            self.assertEqual(result, "weather unavailable")
    
    def test_weather_info_connection_error(self):
        """Тест обробки помилки підключення."""
        with patch('main.get_weather_data', side_effect=ConnectionError("No connection")):
            result = get_weather_info()
            self.assertEqual(result, "weather unavailable")
    
    def test_weather_info_timeout_error(self):
        """Тест обробки помилки таймауту."""
        with patch('main.get_weather_data', side_effect=TimeoutError("Request timeout")):
            result = get_weather_info()
            self.assertEqual(result, "weather unavailable")
    
    def test_weather_info_multiple_different_exceptions(self):
        """Тест обробки різних типів помилок."""
        exceptions = [
            Exception("Generic error"),
            ConnectionError("Network error"),
            TimeoutError("Timeout"),
            RuntimeError("Runtime error")
        ]
        
        for exc in exceptions:
            with patch('main.get_weather_data', side_effect=exc):
                result = get_weather_info()
                self.assertEqual(result, "weather unavailable")
    
    def test_weather_info_side_effect_sequence(self):
        """Тест sequence side_effect: успіх потім помилка."""
        with patch('main.get_weather_data', side_effect=["Rainy, 15°C", Exception("Error")]):
            # Перший виклик - успіх
            result1 = get_weather_info()
            self.assertEqual(result1, "Rainy, 15°C")
            
            # Другий виклик - помилка
            result2 = get_weather_info()
            self.assertEqual(result2, "weather unavailable")
    
    def test_weather_info_side_effect_with_different_messages(self):
        """Тест side_effect з різними повідомленнями про помилку."""
        error_messages = [
            "API returned 500",
            "Invalid API key",
            "Service unavailable"
        ]
        
        for error_msg in error_messages:
            with patch('main.get_weather_data', side_effect=Exception(error_msg)):
                result = get_weather_info()
                self.assertEqual(result, "weather unavailable")


# ====================================
# Запуск тестів
# ============================================================================

if __name__ == "__main__":
    # Запуск тестів з детальним виводом
    unittest.main(verbosity=2)
