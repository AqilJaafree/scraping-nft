from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
url = 'https://app.pentas.io/marketplace'

driver = webdriver.Chrome()

driver.get(url)
nfts = driver.find_elements_by_css_selector('#__next > div:nth-child(2) > div > div.flex-grow > div.container.max-w-screen-2xl.py-12.mx-auto.sm\:px-6.xl\:px-8')

for nft in nfts:
    title = nft.find_element_by_css_selector('.title a').text
    owner = nft.find_element_by_css_selector('.owner a').text
    price = nft.find_element_by_css_selector('.price').text
    print(title,owner,price)