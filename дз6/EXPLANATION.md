# Поясненнякоду: JSON та XML обробка

## 📖 Загальний опис
Цей скрипт розв'язує 4 завдання, пов'язані з обробкою JSON та XML даних в Python.

---

## 🎯 ЗАВДАННЯ 1: Аналіз JSON з інформацією про курси

### Поясненння коду:

```python
import json
```
Імпортуємо модуль `json` для роботи з JSON даними.

```python
courses_json = '''[{...}]'''
courses = json.loads(courses_json)
```
- **`json.loads()`** — преобразує JSON-рядок в Python об'єкт (список словників)
- JSON це текстовий формат, a `loads` перетворює текст → Python структура даних

### Крок 1: Вивід всіх курсів
```python
for course in courses:
    print(f"- {course['title']}")
```
Проходимо через список курсів, звертаємось до поля `'title'` кожного словника.

### Крок 2: Фільтрування активних курсів
```python
active_courses = [course for course in courses if course['active']]
```
- Це **list comprehension** (створення списку з фільтруванням)
- Берему тільки курси, де `course['active']` == `True`
- Результат: курси "Python Basics" та "Data Analysis"

### Крок 3: Кількість студентів
```python
for course in courses:
    print(f"- {course['title']}: {len(course['students'])} студентів")
```
- **`len()`** — повертає довжину списку студентів
- Приклад: курс "Python Basics" має 3 студента

### Крок 4: Курс з найбільшою кількістю студентів
```python
max_students_course = max(courses, key=lambda c: len(c['students']))
```
- **`max()`** з параметром `key` — знаходить максимальний елемент
- **`lambda c: len(c['students'])`** — функція порівняння (кількість студентів)
- Результат: "Web Scraping" з 4 студентами

### Крок 5: Загальна кількість годин активних курсів
```python
total_hours_active = sum(course['hours'] for course in courses if course['active'])
```
- **`sum()`** — сумує значення
- **Generator expression** — генератор, що проходить через активні курси
- Додаємо години тільки для активних курсів: 36 + 42 = 78 годин

---

## 📊 ЗАВДАННЯ 2: Створення JSON-файлу зі звітом

### Поясненння коду:

### Крок 1: Створення нової структури даних
```python
courses_report = []
for course in courses:
    courses_report.append({
        "title": course["title"],
        "teacher": course["teacher"],
        "students_count": len(course["students"]),  # Замість списку - кількість
        "active": course["active"]
    })
```
- Створюємо новий список порожній `[]`
- Для кожного курсу створюємо новий словник з 4 полями
- **`len(course["students"])`** — замість повного списку студентів, запам'ятовуємо тільки їх кількість
- **`append()`** — додаємо новий словник до списку

### Крок 2: Запис у файл JSON
```python
with open('courses_report.json', 'w', encoding='utf-8') as f:
    json.dump(courses_report, f, indent=4, ensure_ascii=False)
```
- **`open('courses_report.json', 'w')`** — відкриває файл на запис
  - `'w'` означає режим запису (write)
  - `encoding='utf-8'` — підтримуємо українські символи
- **`with`** — контекстний менеджер, автоматично закриває файл після завершення
- **`json.dump()`** — записує Python об'єкт як JSON в файл
  - `indent=4` — красивий формат з відступами 4 пробіли
  - `ensure_ascii=False` — дозволяє використовувати кирилицю

### Крок 3: Читання файлу назад
```python
with open('courses_report.json', 'r', encoding='utf-8') as f:
    loaded_report = json.load(f)
```
- **`json.load()`** — читає JSON з файлу та перетворює в Python об'єкт
- `'r'` означає режим читання (read)

---

## 📚 ЗАВДАННЯ 3: Аналіз XML з інформацією про бібліотеку

### Поясненння коду:

```python
import xml.etree.ElementTree as ET
```
Імпортуємо модуль `ElementTree` (ET) для роботи з XML. Це стандартний модуль Python.

### Крок 1: Парсинг XML-рядка
```python
library_xml = """<library>...</library>"""
root = ET.fromstring(library_xml)
```
- **`ET.fromstring()`** — перетворює XML-рядок в дерево об'єктів
- **`root`** — це кореневий елемент дерева (у нашому випадку `<library>`)
- XML має структуру дерева: корінь → гілки → листя

### Крок 2: Вивід кореневого тега
```python
print(f"Кореневий тег документа: {root.tag}")
```
- **`root.tag`** — повертає ім'я тега (`"library"`)

### Крок 3: Вивід всіх назв книг
```python
for book in root.findall('book'):
    title = book.find('title').text
    print(f"- {title}")
```
- **`root.findall('book')`** — знаходить ВСЕ дочірні елементи з тегом `book`
- **`book.find('title')`** — знаходить перший елемент `title` всередину цього `book`
- **`.text`** — отримує текстовий вміст елемента
- Результат: 3 книги

### Крок 4: Вивід всіх деталей про кожну книгу
```python
for book in root.findall('book'):
    book_id = book.get('id')           # Атрибут
    category = book.get('category')    # Атрибут
    title = book.find('title').text    # Вкладений елемент
    author = book.find('author').text
    year = book.find('year').text
    pages = book.find('pages').text
```
- **`book.get('id')`** — отримує атрибут елемента (те, що в тегу)
  - Приклад: `<book id="1">` → `book.get('id')` = `"1"`
- **`book.find(...).text`** — отримує текст вкладеного елемента

### Крок 5: Фільтрування книг за категорією
```python
for book in root.findall("book[@category='programming']"):
    title = book.find('title').text
```
- **`findall("book[@category='programming']")`** — XPath вираз
- **`[@category='programming']`** — умова фільтрування (тільки книги з цією категорією)
- XPath це мова запитів для XML (подібна до SQL для баз даних)

### Крок 6: Обчислення середньої кількості сторінок
```python
pages_list = [int(book.find('pages').text) for book in root.findall('book')]
average_pages = sum(pages_list) / len(pages_list)
```
- **`int(...)`** — перетворює текст в число (сторінки в XML як текст)
- **List comprehension** — створюємо список чисел
- **`sum() / len()`** — формула для середнього значення
- Розрахунок: (350 + 280 + 500) / 3 = 376.67

---

## 👨‍🎓 ЗАВДАННЯ 4: Створення XML-документа

### Поясненння коду:

### Крок 1: Створення кореневого елемента
```python
students_root = ET.Element('students')
```
- **`ET.Element('students')`** — створює новий XML елемент з тегом `students`
- Це буде коренем дерева

### Крок 2: Додавання студентів
```python
students_data = [
    {'group': 'ST-21', 'name': 'Anna', 'age': 20, 'grade': 95},
    {'group': 'ST-22', 'name': 'Bohdan', 'age': 21, 'grade': 82},
    ...
]

for student in students_data:
    student_elem = ET.SubElement(students_root, 'student', group=student['group'])
```
- **`ET.SubElement(parent, 'tag', attribute='value')`** — створює дочірній елемент
  - `students_root` — батьківський елемент
  - `'student'` — ім'я нового тега
  - `group=student['group']` — атрибут з його значенням
- Це створює: `<student group="ST-21">`

### Крок 3: Додавання вкладених елементів
```python
    name_elem = ET.SubElement(student_elem, 'name')
    name_elem.text = student['name']
    age_elem = ET.SubElement(student_elem, 'age')
    age_elem.text = str(student['age'])
```
- Створюємо вкладені елементи (`<name>`, `<age>`, `<grade>`)
- **`.text`** — присвоюємо текстовий вміст
- **`str()`** — перетворюємо число в текст (XML тримає все як текст)
- Результат:
```xml
<student group="ST-21">
    <name>Anna</name>
    <age>20</age>
    <grade>95</grade>
</student>
```

### Крок 4: Перетворення в рядок
```python
xml_string = ET.tostring(students_root, encoding='unicode')
```
- **`ET.tostring(..., encoding='unicode')`** — перетворює дерево в текстовий рядок
- Результат: `<students><student>...</student></students>`

### Крок 5: Красивий вивід XML
```python
import xml.dom.minidom as minidom
dom = minidom.parseString(tree_string)
pretty_xml = dom.toprettyxml(indent="  ")
```
- **`minidom.parseString()`** — парсить XML рядок
- **`.toprettyxml(indent="  ")`** — форматує з красивими відступами
- Результат — аккуратний XML з розділенням по строкам

### Крок 6: Запис у файл
```python
tree = ET.ElementTree(students_root)
tree.write('students.xml', encoding='utf-8', xml_declaration=True)
```
- **`ET.ElementTree(root)`** — обгортаємо корінь в об'єкт дерева
- **`.write('students.xml', ...)`** — записує в файл
  - `encoding='utf-8'` — кодування
  - `xml_declaration=True` — додаємо `<?xml version='1.0' ?>` на початку

### Крок 7: Читання файлу назад
```python
parsed_tree = ET.parse('students.xml')
parsed_root = parsed_tree.getroot()

for student in parsed_root.findall('student'):
    name = student.find('name').text
```
- **`ET.parse('students.xml')`** — читає XML файл
- **`.getroot()`** — отримує кореневий елемент
- **`.findall('student')`** — знаходить всіх студентів
- Вибираємо імена з вкладених елементів

---

## 🔑 Ключові концепції

### JSON
- Текстовий формат обміну даними
- `json.loads()` — рядок → Python об'єкт
- `json.dump()` — Python об'єкт → файл JSON

### XML
- Структурований формат з тегами, атрибутами та вкладеністю
- `ET.fromstring()` — рядок → дерево
- `ET.Element()` / `ET.SubElement()` — створення елементів
- `ET.tostring()` — дерево → рядок
- `findall()` / `find()` — пошук елементів
- `.text` — текстовий вміст
- `.get()` — атрибути

### Управління файлами
```python
with open('file.json', 'w', encoding='utf-8') as f:
    # Робимо щось з файлом
    # Автоматично закривається після блоку
```
- **`with`** — гарантує закриття файлу
- `'w'` — запис, `'r'` — читання

### List Comprehension
```python
[expression for item in iterable if condition]
```
- Компактний спосіб створення списків з фільтруванням

### Lambda функції
```python
max(list, key=lambda x: x['value'])
```
- Анонімна функція для використання як параметр

---

## 📁 Структура файлів

```
дз6/
├── solution.py              # Основний скрипт
├── courses_report.json      # Виходовий файл (завдання 2)
├── students.xml            # Виходовий файл (завдання 4)
├── ю.md                    # Умови завдань
└── EXPLANATION.md          # Цей файл
```

---

## 🚀 Як запустити

```bash
cd "d:\OneDrive\Repo\AP-Semester-II\AP-Semester-II\дз6"
python solution.py
```

Скрипт автоматично:
1. Обробить JSON дані та виведе результати
2. Створить та прочитає `courses_report.json`
3. Обробить XML дані та виведе результати
4. Створить та прочитає `students.xml`

---

## 💡 Практичні поради

1. **JSON для конфігурацій** — `json.load()` для читання, `json.dump()` для запису
2. **XML для складних структур** — коли потрібна вложеність та атрибути
3. **Завжди використовуйте `encoding='utf-8'`** — для підтримки українських символів
4. **`with` statement** — автоматично закриває файли
5. **XPath в `findall()`** — потужний спосіб фільтрування XML
