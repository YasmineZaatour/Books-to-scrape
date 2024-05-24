import requests
from bs4 import BeautifulSoup
from pprint import pprint

url="https://books.toscrape.com/"
response=requests.get(url)

# Find all categories 
soup=BeautifulSoup(response.text,'html.parser')
aside=soup.find('div',class_='side_categories')
categories_div=aside.find('ul').find('li').find('ul')
categories=[child.text.strip() for child in categories_div.children if child.name]

# Find all images
images=soup.find('section').find_all('img')
images=[img.get('src') for img in images]

# Find all titles

# Method 1
articles=soup.find_all('article',class_="product_pod")
for article in articles:
    links=article.find_all('a')[1]
#    print(links.get('title'))

# Method 2

titles_tags=soup.find_all('a',title=True)
titles=[tag.get('title') for tag in titles_tags]
pprint(titles)
