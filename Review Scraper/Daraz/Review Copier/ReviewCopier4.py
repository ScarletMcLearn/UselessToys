lv = 0
master_count = 0


from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random


from tqdm import tqdm

import pandas as pd

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def scroll(d):
    SCROLL_PAUSE_TIME = 0.5 
    # Get scroll height
    last_height = d.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = d.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



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

global_prods = []


cnt = 1
while cnt<104:
    url = 'https://www.daraz.com.bd/catalog/?from=filter&page=' + str(cnt) + '&q=' + keyword + '&rating=1'
    d.get(url)
    tqdm_sleep(5)
    current_prods = d.find_elements(By.CSS_SELECTOR, "div[class='title--wFj93']>a")
    for i in current_prods:
        global_prods.append(i.get_attribute('href'))
        # d.find_element(By.CSS_SELECTOR, "li[title='Next Page'").click()
    cnt = cnt + 1

    # i.text

global_prods_df = pd.DataFrame(global_prods, columns=['Link'])
# global_prods_df.to_csv('/media/scarlet/Project/Project Files/Review Copier/Scraped Files/global_prods_df.csv', index=False)

global_prods_df = pd.read_csv('/media/scarlet/Project/Project Files/Review Copier/Scraped Files/global_prods_df.csv')

# create an Empty DataFrame object
df = pd.DataFrame(columns=['Product Title', 'Link', 'Ratings', 'Reviews'])


cnt = 20
for i in range(len(global_prods_df)):
        tmp_link = global_prods_df.iloc[i]['Link']
        # tmp_text = i.text
        print('Before going to link')
        d.get(tmp_link)
        # tqdm_sleep(10)
        # print('Before scrolling')
        # scroll(d)
        time.sleep(5)
        # tmp_text = d.find_element(By.CLASS_NAME, #'pdp-mod-product-badge-title'
        # 'pdp-mod-product-badge-wrapper').text
        print('Before getting error')
        try:
            tmp_text = WebDriverWait(d, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 
        'pdp-mod-product-badge-wrapper')
        )).text
        except:
            continue
        print('Before getting title')
        tmp_text = WebDriverWait(d, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 
        'pdp-mod-product-badge-wrapper')
        )).text
        print('Before scrolling')
        scroll(d)
        # d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # tmp_rating = d.find_element(By.CLASS_NAME, 'score-average').text
        print('Before getting rating')
        tmp_rating = WebDriverWait(d, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 
        'score-average')
        )).text
        print('Before getting review')
        try:
            WebDriverWait(d, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 
            'item-content')
            ))
        except:
            continue
        print('Before copying reviews')
        tmp_review_list = d.find_elements(By.CLASS_NAME, 'item-content')
        if len(tmp_review_list) > 0:
            for j in tmp_review_list:
                tmp_review = j.text
                # print('tmp_link: ', tmp_link)
                # print('tmp_text: ', tmp_text)
                # print('tmp_rating: ', tmp_rating)
                # print('tmp_review: ', tmp_review)
                df = df.append({'Link': tmp_link, 'Product Title': tmp_text, 'Ratings': tmp_rating, 'Reviews':tmp_review}, ignore_index=True)
        print(cnt, ' done.')
        cnt = cnt + 1

    
    # print('1 done')
    




# import pandas as pd
# df = pd.DataFrame(columns=['Name', 'Weight', 'Sample'])
# for key in my_dict:
#   ...
#   #transform your dic in DataFrame
#   new_df = pd.DataFrame([row])
#   df = pd.concat([df, new_df], axis=0, ignore_index=True)



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
