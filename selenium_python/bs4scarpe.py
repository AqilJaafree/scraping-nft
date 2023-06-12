import requests

from bs4 import BeautifulSoup

# import sys

# Using forward slashes in file path
# import sys
# sys.path.append('C:\\Users\\wanaqil\\AppData\\Local\\Programs\\Python\\Python311\\python.exe C:\\selenium_python\\bs4scarpe.py')



# Using raw string with backslashes in file path
# sys.path.append(r'C:\Users\wanaqil\AppData\Local\Programs\Python\Python311\Lib\site-packages')

search_term = input("Search")
url = f'https://app.pentas.io/user/{search_term}'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
item = doc.find_all('h1',class_='text-textPrimary dark:text-dmTextPrimary pt-12 xl:pt-0 text-3xl xl:text-4xl font-bold')
print(item)
