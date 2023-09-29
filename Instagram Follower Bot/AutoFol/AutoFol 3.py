lv = 0
master_count = 0


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random



# import the time module
import time
  
# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = 'Sleeping for: {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1



d = webdriver.Firefox()

d.maximize_window()

print('Logging in')

d.get('https://www.instagram.com')

time.sleep(5)

username = d.find_element(By.NAME, 'username')

username.clear()

username.send_keys('ScarletMcLearn')

password = d.find_element(By.NAME, 'password')

password.send_keys('+9003517+')

submit = d.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()

time.sleep(5)

print('Logged in to Instagram')

random.seed(time.time())

def looper(d):
    global lv 
    global master_count
    print('Going to Explore page')
    explore = d.find_element(By.CSS_SELECTOR, "svg[aria-label='Explore'")
    explore.click()
    time.sleep(5)
    print('Waiting on Explore page')
    random.seed(time.time())
    rand1 = random.randint(1, 3)
    rand2 = 0
    if rand1 == 1:
        random.seed(time.time())
        rand2 = random.randint(5,10)
    elif rand1 == 2:
        random.seed(time.time())
        rand2 = random.randint(11, 20)
    else:
        random.seed(time.time())
        rand2 = random.randint(21, 30)
    print('Sleeping for ', str(rand2), ' seconds')
    time.sleep(rand2)
    accounts = d.find_elements(By.TAG_NAME, 'a')
    tmp = []
    print('Processing accounts')
    for i in accounts:
        if i.get_attribute('href').startswith('https://www.instagram.com/p/'):
            tmp.append(i.get_attribute('href')[:i.get_attribute('href').rfind('/')])
    accounts = tmp
    tmp = None
    print('Accounts Processed')
    print('Number of accounts: ', str(len(accounts)))
    count = 0
    while count < len(accounts):
    #    print('Preload')
        d.get(accounts[count])
    #    d.refresh()
        time.sleep(5)
#        time.sleep(60)
#        print('Generating Random Numbers')
        random.seed(time.time())
        rand1 = random.randint(1, 3)
        if rand1 == 1:
            random.seed(time.time())
            rand2 = random.randint(5,10)
        elif rand1 == 2:
            random.seed(time.time())
            rand2 = random.randint(11, 20)
        else:
            random.seed(time.time())
            rand2 = random.randint(21, 30)
        print('Sleeping for ', str(rand2), ' seconds')
        time.sleep(rand2)
        print('Following Profile')
        #
        btns = d.find_elements(By.CSS_SELECTOR, 'button')
        #
        for b in btns:
            if b.text == 'Follow':
                b.click()     
                time.sleep(10)
#                time.sleep(60)
#                print('Generating Random Numbers')
                random.seed(time.time())
                rand1 = random.randint(1, 3)
                if rand1 == 1:
                    random.seed(time.time())
                    rand2 = random.randint(5,10)
                elif rand1 == 2:
                    random.seed(time.time())
                    rand2 = random.randint(11, 20)
                else:
                    random.seed(time.time())
                    rand2 = random.randint(21, 30)
            #    time.sleep(60)
#                print('Rand 1: ', str(rand1), ', Rand 2: ', str(rand2))
                print('Sleeping for ', str(rand2), ' seconds')
                time.sleep(rand2)
        #
        lv = lv + 1
        count = count + 1
        print('Master Followed ', str(master_count+1), ' account(s)')      
        master_count = master_count + 1
#        master_count = master_count + 1
    print('Master count: ', str(master_count))
    return master_count


while (lv <1200):
    tmp_lv = looper(d)
#    lv = tmp_lv + lv 
    print('Looper count: ', str(tmp_lv))   

print('Done!')





