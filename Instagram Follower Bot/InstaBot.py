from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



d = webdriver.Firefox()

d.get('https://www.instagram.com')

time.sleep(5)

username = d.find_element(By.NAME, 'username')

username.clear()

username.send_keys('ENTER USERNAME HERE')

password = d.find_element(By.NAME, 'password')

password.send_keys('ENTER PASSWORD HERE')

submit = d.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()

time.sleep(5)

print('Logged in to Instagram')

explore = d.find_element(By.CSS_SELECTOR, "svg[aria-label='Explore'")
explore.click()

time.sleep(5)

#accounts = d.find_elements(By.CSS_SELECTOR, 'div[class="_aagw"')

accounts = d.find_elements(By.TAG_NAME, 'a')

tmp = []

for i in accounts:
    if i.get_attribute('href').startswith('https://www.instagram.com/p/'):
        tmp.append(i.get_attribute('href'))

accounts = tmp

tmp = None



print('Number of accounts: ', str(len(accounts)))


count = 0

while count < len(accounts):
#    print('Preload')
    d.get(accounts[count])
#    d.refresh()
    time.sleep(5)
    #accounts = d.find_elements(By.CSS_SELECTOR, 'div[class="_aagw"')
    #accounts[0].click()
    ##
#    account = d.find_element(By.CSS_SELECTOR, 'div[class="_aagw"')
#    account.click()
    ##
#    time.sleep(3)
    #
    btns = d.find_elements(By.CSS_SELECTOR, 'button')
    #
    for b in btns:
        if b.text == 'Follow':
            b.click()
            print('Followed ', str(count+1), ' account(s)')      
#            d.back()
            time.sleep(10)
    #
    count = count + 1
    


        

print('Done!')

