lv = 0
master_count = 0


from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random


from tqdm import tqdm

import pandas as pd


def tqdm_sleep(sec):
    for i in tqdm(range(sec)):
        time.sleep(1)


random.seed(time.time())

d = webdriver.Firefox()

keyword = 'pant'
url = 'https://www.daraz.com.bd/catalog/?from=filter&page=1&q=' + keyword + '&rating=1'
d.get(url)

# current_page = d.find_elements(By.CLASS_NAME, 'title--wFj93')


# current_page = d.find_elements(By.XPATH, "//div[@class='title--wFj93']")


current_prods = d.find_elements(By.CSS_SELECTOR, "div[class='title--wFj93']>a")


current_prods[0].get_attribute('href')
current_prods[0].text

# create an Empty DataFrame object
df = pd.DataFrame(columns=['Product Title', 'Link', 'Ratings', 'Reviews'])


for i in current_prods:
    tmp_link = i.get_attribute('href')
    tmp_text = i.text
    d.get(tmp_link)
    tqdm_sleep(10)
    # d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    tmp_rating = d.find_element(By.CLASS_NAME, 'score-average').text
    tmp_review_list = d.find_elements(By.CLASS_NAME, 'item-content')
    if len(tmp_review_list) > 0:
        for j in tmp_review_list:
            tmp_review = j.text
            # print('tmp_link: ', tmp_link)
            # print('tmp_text: ', tmp_text)
            # print('tmp_rating: ', tmp_rating)
            # print('tmp_review: ', tmp_review)
            df = df.append({'Link': tmp_link, 'Product Title': tmp_text, 'Ratings': tmp_rating, 'Reviews':tmp_review}, ignore_index=True)
    print('1 done')
    d.back()
        # break 




d.find_element(By.CLASS_NAME, 'score-average')


d.get(current_prods[0].get_attribute('href'))
d.find_element(By.CSS_SELECTOR, "li[title='Next Page'").click()

    # current_page_titles.append(i.text)

# current_page_links = []
# current_page_titles = []
# for i in current_page:
#     current_page_links.append(i.get_attribute('href'))
#     current_page_titles.append(i.text)



df = pd.DataFrame(current_page, index =['Product Title', 'second'], columns =['x', 'y'])  
