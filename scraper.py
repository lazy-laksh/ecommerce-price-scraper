import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re  # 1. Import Regular Expressions to handle dirty text data

all_books_data = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print("Starting robust data extraction pipeline...")

for page_num in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping Page {page_num}/50...")
    
    response = requests.get(url, headers=headers)
    
    # Force UTF-8 encoding to help fix character glitches
    response.encoding = 'utf-8'
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}. Stopping.")
        break
        
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        try:
            title = book.h3.a["title"]
            raw_price = book.find("p", class_="price_color").text
            
            # 2. Extract ONLY numbers and decimals (e.g., 'Â51.77' -> '51.77')
            price_cleaned = re.search(r'\d+\.\d+', raw_price).group()
            price = float(price_cleaned)
            
            availability = book.find("p", class_="instock availability").text.strip()
            
            all_books_data.append({
                "Title": title,
                "Price_GBP": price,
                "Availability": availability
            })
        except Exception as e:
            print(f"Skipped a book on page {page_num} due to error: {e}")
            
    time.sleep(1)

# --- DATA EXPORT ---
if all_books_data:
    df = pd.DataFrame(all_books_data)
    df.to_csv("scraped_market_data.csv", index=False)
    print("\n--- Pipeline Execution Complete ---")
    print(f"Total Records Extracted: {len(df)}")
    print("Data saved successfully to 'scraped_market_data.csv'")
else:
    print("\nNo data extracted. Check your parsing selectors.")