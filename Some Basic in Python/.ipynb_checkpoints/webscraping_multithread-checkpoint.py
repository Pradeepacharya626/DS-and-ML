import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.google.com/document/d/1QMZUo13lDYVlhoDLOfZTdyTnAeit8CPlxLHMMjxL4gs/edit',
    'https://docs.google.com/document/d/1mp0BBgBDnhRilXKC55ID4HPuVdQF-pZ9BMmLYMsvr7Q/edit',
    'https://docs.google.com/document/d/1G3E89YNT3Afl-RC10Y04Sbn4YyUTjOeKBP5t08Vb-4I/edit'
]

def fetch_content(url) :
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} charecters from {url}")


threads=[]

for url in urls :
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads :
    thread.join()

print("All web pages fetched")
    