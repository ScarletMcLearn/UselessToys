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

def scroll(d):
    total_page_height = d.execute_script("return document.body.scrollHeight") + 10
    browser_window_height = d.get_window_size(windowHandle='current')['height']
    current_position = d.execute_script('return window.pageYOffset')
    while (total_page_height - current_position > browser_window_height):
        d.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        current_position = d.execute_script('return window.pageYOffset')
        time.sleep(1)  # It is necessary here to give it some time to load the content

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


cnt = 0
for i in range(len(global_prods_df)):
    tmp_link = global_prods_df.iloc[i]['Link']
    # tmp_text = i.text
    d.get(tmp_link)
    # tqdm_sleep(10)
    time.sleep(10)
    tmp_html = d.page_source
    tmp_html = BeautifulSoup(tmp_html, 'html.parser')
    tmp_text = tmp_html.find_all('div', class_='pdp-mod-product-badge-wrapper')[0].text
    d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # tmp_rating = d.find_element(By.CLASS_NAME, 'score-average').text
    tmp_rating = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 
    'score-average')
    )).text
    tmp_html.find_all('div', class_='score-average')[0].text
    WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 
    'item-content')
    ))
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
