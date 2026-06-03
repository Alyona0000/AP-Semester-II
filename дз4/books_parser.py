import csv
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import Counter


BASE_URL = "https://books.toscrape.com/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
CSV_FILE = "books.csv"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def get_html(url):
    """Отримує HTML-код сторінки з правильною кодуванням"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def parse_price(price_text):
    """Витягує ціну з текстової строки і повертає float"""
    # Використовуємо регулярний вираз для витягування чисел з крапкою
    match = re.search(r'\d+\.\d+', price_text)
    if match:
        return float(match.group())
    raise ValueError(f"Не вдалося розпарсити ціну: {price_text}")

def parse_book(book_tag):
    """Витягує всі дані про одну книгу з тегу"""
    try:
        title = book_tag.h3.a["title"]
        
        price_text = book_tag.select_one(".price_color").text
        price = parse_price(price_text)
        
        rating_class = book_tag.select_one(".star-rating")["class"]
        rating_word = rating_class[1]
        rating = RATING_MAP.get(rating_word, 0)
        
        availability = book_tag.select_one(".availability").text.strip()
        availability = " ".join(availability.split())
        
        relative_link = book_tag.h3.a["href"]
        link = urljoin(BASE_URL + "catalogue/", relative_link)
        
        return {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "link": link
        }
    except Exception as e:
        print(f"Помилка при обробці книги: {e}")
        return None


def parse_books_from_page(html):
    """Витягує список всіх книг зі сторінки"""
    soup = BeautifulSoup(html, "html.parser")
    book_tags = soup.select("article.product_pod")

    books = []
    for book_tag in book_tags:
        book = parse_book(book_tag)
        if book is not None:
            books.append(book)

    return books


def get_next_page_url(html, current_url):
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")

    if next_link is None:
        return None

    next_href = next_link["href"]
    return urljoin(current_url, next_href)


def collect_books(start_url, max_pages=5):
    """Збирає книги з кількох сторінок каталогу"""
    all_books = []
    current_url = start_url
    page_number = 1

    while current_url is not None and page_number <= max_pages:
        try:
            print(f"Обробляється сторінка {page_number}: {current_url}")

            html = get_html(current_url)
            books = parse_books_from_page(html)
            all_books.extend(books)
            print(f"  Знайдено книг на сторінці: {len(books)}")

            current_url = get_next_page_url(html, current_url)
            page_number += 1
        except requests.exceptions.RequestException as e:
            print(f"Помилка мережі при завантаженні сторінки: {e}")
            break
        except Exception as e:
            print(f"Помилка при обробці сторінки: {e}")
            break

    return all_books


def build_statistics(books):
    """Будує статистику по збраних книгах"""
    if not books:
        return None
        
    total_books = len(books)
    rating_counter = Counter(book["rating"] for book in books)
    average_price = sum(book["price"] for book in books) / total_books
    most_expensive = max(books, key=lambda book: book["price"])
    cheapest = min(books, key=lambda book: book["price"])

    return {
        "total_books": total_books,
        "rating_counter": rating_counter,
        "average_price": average_price,
        "most_expensive": most_expensive,
        "cheapest": cheapest
    }


def print_statistics(statistics):
    print("\n===== СТАТИСТИКА =====")

    print(f"Загальна кількість книг: {statistics['total_books']}")

    print("\nКількість книг за рейтингом:")
    for rating in range(1, 6):
        count = statistics["rating_counter"].get(rating, 0)
        print(f"{rating} зірок: {count}")

    print(f"\nСередня ціна: £{statistics['average_price']:.2f}")

    expensive = statistics["most_expensive"]
    cheap = statistics["cheapest"]

    print(f"\nНайдорожча книга: {expensive['title']} — £{expensive['price']:.2f}")
    print(f"Найдешевша книга: {cheap['title']} — £{cheap['price']:.2f}")


def save_to_csv(books, filename):
    fieldnames = ["title", "price", "rating", "availability", "link"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for book in books:
            writer.writerow(book)


def main():
    """Головна функція для запуску скрейпера"""
    print("🔄 Початок збору даних про книги...\n")
    
    books = collect_books(START_URL, max_pages=5)

    if not books:
        print("❌ Книги не знайдено")
        return

    print(f"\n✅ Всього обробленно: {len(books)} книг\n")
    
    statistics = build_statistics(books)
    
    if statistics:
        print_statistics(statistics)

    save_to_csv(books, CSV_FILE)
    print(f"\n💾 Дані збережено у файл: {CSV_FILE}")


if __name__ == "__main__":
    main()