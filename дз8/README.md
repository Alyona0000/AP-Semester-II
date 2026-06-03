# Python Testing Project - дз8

Проект, який демонструє всі основні методи тестування на Python з використанням `unittest`, `mock` та `patch`.

## 📦 Структура проекту

```
дз8/
├── main.py              # Основний модуль з функціями та класами
├── test_main.py         # Тести (50+ тестів)
├── EXPLANATION.md       # Докладні пояснення як усе працює
└── README.md           # Цей файл
```

## 🎯 Завдання, які реалізовані

### 1. Функції для роботи з рядками
- `is_empty()` - перевірка, чи рядок порожній
- `count_words()` - підрахунок слів
- `capitalize_first_letter()` - капіталізація першої літери кожного слова
- `longest_word()` - пошук найдовшого слова в списку

**Тести:** 23 тести з різними assert-методами

### 2. Клас BookShelf
- Додавання/видалення книг
- Перевірка наявності книги
- Підрахунок книг
- Підготовка даних через `setUp()`

**Тести:** 13 тестів з використанням setUp()

### 3. Тестування з patch
- Функція `calculate_order_cost()` для розрахунку вартості замовлення
- Функція `get_exchange_rate()` яка буде замінена через patch
- Перевірка кількох різних значень курсу

**Тести:** 6 тестів з patch

### 4. Mock-об'єкти
- Функція `create_report()` яка передає звіт сервісу
- Mock-об'єкт `ReportSaver` для імітації збереження
- Перевірка викликів методів

**Тести:** 6 тестів з mock

### 5. side_effect для обробки помилок
- Функція `get_weather_info()` з обробкою помилок
- Використання side_effect для імітації помилок
- Запасне значення при помилці

**Тести:** 7 тестів з side_effect

## 🚀 Запуск

### Запуск усіх тестів

```bash
# Використовуючи unittest
python test_main.py

# Використовуючи pytest (якщо встановлений)
pytest test_main.py -v
```

### Очікуваний результат

```
test_is_empty_with_empty_string (__main__.TestStringFunctions) ... ok
test_is_empty_with_spaces (__main__.TestStringFunctions) ... ok
...
Ran 55 tests in 0.234s

OK
```

### Запуск конкретного тесту класу

```bash
python -m unittest test_main.TestStringFunctions -v
python -m unittest test_main.TestBookShelf -v
python -m unittest test_main.TestOrderCostWithPatch -v
python -m unittest test_main.TestCreateReportWithMock -v
python -m unittest test_main.TestWeatherInfoWithSideEffect -v
```

## 📋 Тести за категоріями

### Завдання 1: TestStringFunctions (23 тести)
```bash
python -m unittest test_main.TestStringFunctions -v
```

Тестує:
- `is_empty()` - 5 тестів
- `count_words()` - 5 тестів
- `capitalize_first_letter()` - 5 тестів
- `longest_word()` - 5 тестів

### Завдання 2: TestBookShelf (13 тестів)
```bash
python -m unittest test_main.TestBookShelf -v
```

Тестує:
- Ініціалізація
- Додавання книг
- Видалення книг
- Перевірка наявності
- Підрахунок книг

### Завдання 3: TestOrderCostWithPatch (6 тестів)
```bash
python -m unittest test_main.TestOrderCostWithPatch -v
```

Демонструє:
- Базовий patch
- Patch з різними значеннями
- Multiple patch calls

### Завдання 4: TestCreateReportWithMock (6 тестів)
```bash
python -m unittest test_main.TestCreateReportWithMock -v
```

Демонструє:
- Створення mock-об'єктів
- Перевірку викликів методів
- Перевірку аргументів

### Завдання 5: TestWeatherInfoWithSideEffect (7 тестів)
```bash
python -m unittest test_main.TestWeatherInfoWithSideEffect -v
```

Демонструє:
- side_effect для викидання помилок
- side_effect для послідовностей
- Обробка різних типів помилок

## 🔧 Установка залежностей

Базовий код не потребує додаткових бібліотек (використовуються `unittest` та `unittest.mock` з стандартної бібліотеки).

Опціонально для додаткових можливостей:

```bash
# Для запуску тестів з pytest
pip install pytest

# Для перевірки покриття
pip install pytest-cov

# Для красивого висновку
pip install pytest-html
```

## 📚 Ключові концепції

### Assert методи
- `assertEqual(a, b)` - перевірка рівності
- `assertTrue(x)` / `assertFalse(x)` - логічні перевірки
- `assertIn(a, b)` / `assertNotIn(a, b)` - перевірка в колекціях
- `assertRaises(Exception)` - перевірка виключень

### setUp() та tearDown()
```python
def setUp(self):
    # Виконується перед кожним тестом
    self.data = prepare_test_data()

def tearDown(self):
    # Виконується після кожного тесту
    cleanup()
```

### Mock та patch
```python
from unittest.mock import Mock, patch

# Створення mock-об'єкта
mock_obj = Mock()

# Використання patch
with patch('module.function', return_value=42):
    result = my_function()
```

### side_effect
```python
# Викидати виключення
side_effect=Exception("Error")

# Послідовність значень
side_effect=[1, 2, 3, Exception("End")]

# Функція
side_effect=lambda x: x * 2
```

## 📖 Пояснення

Для детальних пояснень кожного завдання див. файл `EXPLANATION.md`:

```bash
# Відкрити файл з поясненнями
cat EXPLANATION.md
```

## ✅ Перевірка коректності

1. **Усі тести проходять:**
   ```bash
   python test_main.py
   ```

2. **Жодних помилок імпорту:**
   ```bash
   python -c "from main import *; print('OK')"
   ```

3. **Кількість тестів - 55:**
   ```bash
   python -m unittest discover -s . -p test_*.py -v | tail -1
   ```

## 🎓 Навчальні цілі

После вивчення цього проекту ви матимете розуміння:

✅ Як писати unit-тести на Python
✅ Як використовувати unittest
✅ Як використовувати mock та patch
✅ Як обробляти виключення в тестах
✅ Як організувати тести в класи
✅ Як структурувати тестові дані
✅ Best practices в тестуванні

## 📊 Статистика

| Метрика | Значення |
|---------|----------|
| Всього функцій | 4 |
| Всього класів | 2 |
| Всього тестів | 55 |
| Покриття функцій | 100% |
| Рядків коду | ~150 |
| Рядків тестів | ~500 |

## 💡 Порад для вивчення

1. **Почніть з Завдання 1** - простий приклад assert методів
2. **Потім перейдіть до Завдання 2** - setUp() та класи
3. **Вивчіть patch** - Завдання 3
4. **Освойте mock** - Завдання 4
5. **Закінчіть з side_effect** - Завдання 5

## 🤔 Часті питання

### Чому test_main.py почина з "test_"?
Це дозволяє test runner автоматично знайти та запустити тести.

### Що таке setUp()?
Це метод, який виконується перед кожним тестом для підготовки даних.

### Різниця між mock та patch?
- `Mock()` - створює підроблений об'єкт
- `patch()` - замінює реальний об'єкт на mock

### Коли використовувати side_effect?
Коли потрібно імітувати помилку або послідовність значень.

## 📞 Контакти

Для питань звертайтесь до документації:
- [unittest docs](https://docs.python.org/3/library/unittest.html)
- [mock docs](https://docs.python.org/3/library/unittest.mock.html)

---

**Успіху в навчанні! 🚀**
