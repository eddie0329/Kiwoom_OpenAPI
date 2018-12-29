import re
import requests
from bs4 import BeautifulSoup

# Request the page from the Internet, the url should be specified by the
# programmer. However, it can be dynamically created given that the stock
# code can be searched from search engines. It could be another database
# contains all the codes of stocks.
stock_code = "005930"
page = requests.get("https://finance.naver.com/item/main.nhn?code=" + stock_code)
soup = BeautifulSoup(page.content, 'html.parser')

# 1. Select element of the html page and process the information (NOT work well
# if the elements are in the complex DOM).
# element_selector = "#tab_con1 > div.first > table > tbody > tr:nth-child(3) > td > em"
# element_selector = '#tab_con1 > div > table > tbody > tf > td'
element_selector = '#_per'

selected_elements = soup.select(element_selector)

for i in selected_elements:
    print(i)

# 2. Use regex (regular expressions) to find the information. It's far more
# complex, so use it when the first method doesn't work.
text_to_search = str(page.content)

regex = '<em></em>'
# match = re.search(regex, text_to_search)
# print(match.group(0))








