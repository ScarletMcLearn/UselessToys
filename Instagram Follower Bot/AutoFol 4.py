lv = 0
master_count = 0


# from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random



from tqdm import tqdm

  
## define the countdown func.
#def countdown(t):
#    while t:
#        mins, secs = divmod(t, 60)
#        timer = 'Sleeping for: {:02d}:{:02d}'.format(mins, secs)
#        print(timer, end="\r")
#        time.sleep(1)
#        t -= 1

def tqdm_sleep(sec):
    for i in tqdm(range(sec)):
        time.sleep(1)

#
#d = webdriver.Firefox()
#
#d.maximize_window()
#
#print('\nLogging in')
#
#d.get('https://www.instagram.com')
#
#tqdm_sleep(5)
#
#username = d.find_element(By.NAME, 'username')
#
#username.clear()
#
#username.send_keys('ScarletMcLearn')
#
#password = d.find_element(By.NAME, 'password')
#
#password.send_keys('+9003517+')
#
#submit = d.find_element(By.XPATH, '//button[@type="submit"]')
#submit.click()
#
#tqdm_sleep(5)
#
#print('\nLogged in to Instagram')
#
random.seed(time.time())

def looper(d):
    global lv 
    global master_count
    print('\nGoing to Explore page')
    explore = d.find_element(By.CSS_SELECTOR, "svg[aria-label='Explore'")
    explore.click()
    tqdm_sleep(5)
    print('\nWaiting on Explore page')
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
    print('\nEP Sleeping for ', str(rand2), ' seconds')
    tqdm_sleep(rand2)
    accounts = d.find_elements(By.TAG_NAME, 'a')
    tmp = []
    print('\nProcessing accounts')
    for i in accounts:
        if i.get_attribute('href').startswith('https://www.instagram.com/p/'):
            tmp.append(i.get_attribute('href')[:i.get_attribute('href').rfind('/')])
    accounts = tmp
    tmp = None
    print('\nAccounts Processed')
    print('\nNumber of accounts: ', str(len(accounts)))
    count = 0
    while count < len(accounts):
    #    print('Preload')
        d.get(accounts[count])
    #    d.refresh()
        tqdm_sleep(5)
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
        print('\nPPSleeping for ', str(rand2), ' seconds')
        tqdm_sleep(rand2)
        print('\nFollowing Profile')
        # Define the text you want to find within the <div> element
        target_text = "Follow"
        #
        # Construct an XPath expression to locate the <div> element with the specified text
        xpath_expression = f"//div[text()='{target_text}']"
        #
        #
        # Find the <div> element using the constructed XPath expression
        try:
            follow_button = d.find_element(By.XPATH,  xpath_expression)
            follow_button.click()
        except:
            continue
        #
        #
#        btns = d.find_elements(By.CSS_SELECTOR, 'button')
#        #
#        for b in btns:
#            if b.text == 'Follow':
#                b.click()     
#                tqdm_sleep(10)
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
            print(
                # Fore.GREEN, 
            '\nFPSleeping for ', str(rand2), ' seconds')
            tqdm_sleep(rand2)
            # print(Style.RESET_ALL)
        #
        lv = lv + 1
        count = count + 1
        print(
            # Fore.GREEN, 
            '\nMaster Followed ', str(master_count+1), ' account(s)') 
        # print(Style.RESET_ALL)     
        master_count = master_count + 1
#        master_count = master_count + 1
    print('\nMaster count: ', str(master_count))
    return master_count


def runner(run_var=1200):
    while (lv <run_var):
        tmp_lv = looper(d)
        print('\nLooper count: ', str(tmp_lv))    
    print('\nDone!')



def loader():
#    d = webdriver.Firefox() # Need to change this to line below 
    d = webdriver.Firefox(service_log_path='/mount/Project/Project Files/PythonEnvs/AutomationEnv/AutoDriver/geckodriver.log')
    
    #
    d.maximize_window()
    #
    print('\nLogging in')
    #
    d.get('https://www.instagram.com')
    #
    tqdm_sleep(5)
    #
    username = d.find_element(By.NAME, 'username')
    #
    username.clear()
    #
    username.send_keys('')
    #
    password = d.find_element(By.NAME, 'password')
    #
    password.send_keys('')
    #
    submit = d.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()
    #
    print('Submitting form')
    tqdm_sleep(5)
    #
    print('\nLogged in to Instagram')
    #
    random.seed(time.time())
    return d




# Construct an XPath expression to locate the <div> element with the specified text
# Define the text you want to find within the <div> element
target_text = "Follow"

# Construct an XPath expression to locate the <div> element with the specified text
xpath_expression = f"//div[text()='{target_text}']"


# Find the <div> element using the constructed XPath expression
follow_button = d.find_element(By.XPATH,  xpath_expression)
follow_button.click()

d = loader()
runner()







lv = 0
master_count = 0

d = loader()
runner()





