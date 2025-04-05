import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


import os
import sys
PROGRESS_FILE = "end_to_end/page_num.txt"
CSV_FILE = "end_to_end/books_to_scrape.csv"
MAX_PAGE = 50 # stop after 5 pages (you can increase later)


def get_last_scraped_page():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    return 1

def update_scraped_page(page_num):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(page_num))



def get_rating(star_tag):
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    for cls in star_tag.get("class", []):
        if cls in rating_map:
            return rating_map[cls]
    return None

def scrape_books(page_num):

    print(f"Scraping page {page_num}...")
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"

    page_books=[]
    
   
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open("end_to_end/soup.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print("HTML content saved to soup.html")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            star_tag = book.find("p", class_="star-rating")
            rating = get_rating(star_tag)
            
            print("Extracting Successful, Now saving in file")
            page_books.append({
                "Page": page_num,
                "Title": title,
                "Price": price,
                "Rating": rating
            })
        
    time.sleep(1)  # polite delay

    return page_books

def main():
    current_page = get_last_scraped_page()

    if current_page > MAX_PAGE:
        print("✅ All pages already scraped. Nothing more to do.")
        return

    books = scrape_books(current_page)
    if not books:
        print("❌ No books found on this page.")
        return
    df = pd.DataFrame(books)

    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode="a", index=False, header=False)
    else:
        df.to_csv(CSV_FILE, index=False)

    update_scraped_page(current_page + 1)
    print(f"✅ Scraped page {current_page}, updated to page {current_page + 1}")
    


if __name__ == "__main__":
    main()