import json
import xml.etree.ElementTree as ET

print("=" * 80)
print("ЗАВДАННЯ 1. Аналіз JSON з інформацією про курси")
print("=" * 80)

# JSON-рядок з інформацією про курси
courses_json = '''
[
{
"title": "Python Basics",
"teacher": "Koval",
"hours": 36,
"students": ["Anna", "Bohdan", "Iryna"],
"active": true
},
{
"title": "Data Analysis",
"teacher": "Petrenko",
"hours": 42,
"students": ["Maksym", "Olha"],
"active": true
},
{
"title": "Web Scraping",
"teacher": "Ivanenko",
"hours": 24,
"students": ["Taras", "Anna", "Olha", "Roman"],
"active": false
}
]
'''

# Перетворення JSON-рядка у Python-об'єкт
courses = json.loads(courses_json)
print("\n1. Перетворена дані з JSON:")
print(courses)

# Вивести назви всіх курсів
print("\n2. Назви всіх курсів:")
for course in courses:
    print(f"   - {course['title']}")

# Вивести тільки активні курси
print("\n3. Активні курси:")
active_courses = [course for course in courses if course['active']]
for course in active_courses:
    print(f"   - {course['title']}")

# Для кожного курсу показати кількість студентів
print("\n4. Кількість студентів для кожного курсу:")
for course in courses:
    print(f"   - {course['title']}: {len(course['students'])} студентів")

# Знайти курс з найбільшою кількістю студентів
max_students_course = max(courses, key=lambda c: len(c['students']))
print(f"\n5. Курс з найбільшою кількістю студентів:")
print(f"   - {max_students_course['title']}: {len(max_students_course['students'])} студентів")

# Порахувати загальну кількість годин тільки для активних курсів
total_hours_active = sum(course['hours'] for course in courses if course['active'])
print(f"\n6. Загальна кількість годин для активних курсів: {total_hours_active} годин")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 2. Створення JSON-файлу зі звітом")
print("=" * 80)

# Створити нову структуру даних
courses_report = []
for course in courses:
    courses_report.append({
        "title": course["title"],
        "teacher": course["teacher"],
        "students_count": len(course["students"]),
        "active": course["active"]
    })

print("\n1. Сформована структура для звіту:")
print(courses_report)

# Записати у файл courses_report.json з гарним форматуванням
with open('courses_report.json', 'w', encoding='utf-8') as f:
    json.dump(courses_report, f, indent=4, ensure_ascii=False)
print("\n2. Дані записані у файл courses_report.json")

# Зчитати файл назад
with open('courses_report.json', 'r', encoding='utf-8') as f:
    loaded_report = json.load(f)
print("\n3. Дані, прочитані з файлу courses_report.json:")
print(loaded_report)

print("\n" + "=" * 80)
print("ЗАВДАННЯ 3. Аналіз XML з інформацією про бібліотеку")
print("=" * 80)

library_xml = """
<library>
<book id="1" category="programming">
<title>Python Basics</title>
<author>John Smith</author>
<year>2020</year>
<pages>350</pages>
</book>
<book id="2" category="statistics">
<title>Statistics for Beginners</title>
<author>Anna Brown</author>
<year>2018</year>
<pages>280</pages>
</book>
<book id="3" category="programming">
<title>Advanced Python</title>
<author>Kate Wilson</author>
<year>2023</year>
<pages>500</pages>
</book>
</library>
"""

# Прочитати XML-рядок
root = ET.fromstring(library_xml)
print(f"\n1. Кореневий тег документа: {root.tag}")

# Вивести назви всіх книг
print("\n2. Назви всіх книг:")
for book in root.findall('book'):
    title = book.find('title').text
    print(f"   - {title}")

# Для кожної книги показати її деталі
print("\n3. Детальна інформація про кожну книгу:")
for book in root.findall('book'):
    book_id = book.get('id')
    category = book.get('category')
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    pages = book.find('pages').text
    print(f"   ID: {book_id}, Категорія: {category}, Назва: {title}, Автор: {author}, Рік: {year}, Сторінок: {pages}")

# Вивести тільки книги з категорією programming
print("\n4. Книги з категорією 'programming':")
for book in root.findall("book[@category='programming']"):
    title = book.find('title').text
    author = book.find('author').text
    print(f"   - {title} (автор: {author})")

# Знайти середню кількість сторінок
pages_list = [int(book.find('pages').text) for book in root.findall('book')]
average_pages = sum(pages_list) / len(pages_list)
print(f"\n5. Середня кількість сторінок: {average_pages:.2f}")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 4. Створення XML-документа")
print("=" * 80)

# Створити кореневий елемент
students_root = ET.Element('students')

# Додати студентів
students_data = [
    {'group': 'ST-21', 'name': 'Anna', 'age': 20, 'grade': 95},
    {'group': 'ST-22', 'name': 'Bohdan', 'age': 21, 'grade': 82},
    {'group': 'ST-21', 'name': 'Iryna', 'age': 19, 'grade': 88},
    {'group': 'ST-23', 'name': 'Maksym', 'age': 22, 'grade': 91}
]

for student in students_data:
    student_elem = ET.SubElement(students_root, 'student', group=student['group'])
    name_elem = ET.SubElement(student_elem, 'name')
    name_elem.text = student['name']
    age_elem = ET.SubElement(student_elem, 'age')
    age_elem.text = str(student['age'])
    grade_elem = ET.SubElement(student_elem, 'grade')
    grade_elem.text = str(student['grade'])

# Перетворити XML у рядок і вивести
xml_string = ET.tostring(students_root, encoding='unicode')
print("\n1. Створений XML:")
print(xml_string)

# Красиво вивести XML за допомогою форматування
print("\n2. Форматований XML:")
# Форматуємо вручну для красивого висновку
indent_tree = lambda elem, level=0: None if (
    level and not (elem.tail or '').strip() or not len(elem)
) else (
    elem.tail if level and not (elem.text or '').strip() else None,
    [indent_tree(e, level+1) for e in elem],
    elem.tail.rstrip() if level else None
)

tree_string = ET.tostring(students_root, encoding='unicode')
import xml.dom.minidom as minidom
dom = minidom.parseString(tree_string)
pretty_xml = dom.toprettyxml(indent="  ")
print(pretty_xml)

# Записати у файл students.xml
tree = ET.ElementTree(students_root)
tree.write('students.xml', encoding='utf-8', xml_declaration=True)
print("\n3. XML записаний у файл students.xml")

# Прочитати файл назад
parsed_tree = ET.parse('students.xml')
parsed_root = parsed_tree.getroot()
print("\n4. Імена всіх студентів з файлу:")
for student in parsed_root.findall('student'):
    name = student.find('name').text
    group = student.get('group')
    print(f"   - {name} (група: {group})")

print("\n" + "=" * 80)
print("ВСІ ЗАВДАННЯ ЗАВЕРШЕНО УСПІШНО!")
print("=" * 80)
