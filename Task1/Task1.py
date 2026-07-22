#Task 1: Automated Web Scraper for Property Listings

import requests
from bs4 import BeautifulSoup
import csv
import csv
response=requests.get('https://books.toscrape.com/')
print(response.status_code)
soup=BeautifulSoup(response.content,'html.parser')

all_books=soup.find_all("article",class_="product_pod")
books_data=[]
for book in all_books:
    title=book.h3.a['title']
    price=book.find("p",class_="price_color").text
    rating=book.p['class'][1]
    book_info={
        "Title":title,
        "Price":price,
        "Rating":f"{rating} stars"
    }
    books_data.append(book_info)

with open('books.csv','w',newline='',encoding="utf-8") as csvfile:
    headers=["Title","Price","Rating"]
    writer=csv.DictWriter(csvfile,fieldnames=headers)
    writer.writeheader()
    writer.writerows(books_data)

print("Scrapping complete! Check for books.csv in the file list.")