from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import choice
import _config
import util
import time
import sheets

subs = [
    'gaming',
    'csgo',
    'memes',
    'tf2',
    'askreddit',
    'abruptchaos',
    'perfectlycutscreams',
    'askouija',
    'apple',
    'linux',
    'pcmasterrace',
    'clashroyale',
    'minecraft',
    'cursed_comments',
    'cringetopia',
    'shitposting',
    'rocketleague',
    'playboicarti',
    'dankmemes',
    'gtaonline',
    'soccer',
    'soccercirclejerk',
    'skateboarding'
]

username = util.random_alphanumeric()

while True:
    try:
        # new account credentials
        email = _config.config['account-maker-email']
        if _config.config['account-maker-username'] != '':
            username = _config.config['account-maker-username']
        password = util.random_string()

        options = webdriver.ChromeOptions()
        #options.headless = True        # disable this to test or if you want to see the as it does its thing browser
        options.add_extension('extension_1_3_1_0.crx')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0')

        # use specific chromedriver version (from https://chromedriver.storage.googleapis.com)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager(version="114.0.5735.90").install(), options=options)

        def send_keys_better(element, text):  # to avoid automation detection. if you type it instantly, recaptcha detects it.
            for t in text:
                element.send_keys(t)
                # time interval between each keypress
                time.sleep(0.1)

        driver.implicitly_wait(20)
        driver.get('https://accounts.reddit.com/account/register/')
        
        # email
        email_input = driver.find_element_by_id('regEmail')
        send_keys_better(email_input, email)
        time.sleep(0.5)
        email_input.submit()
        time.sleep(1)

        # username
        username_input = driver.find_element_by_id('regUsername')
        send_keys_better(username_input, username)
        time.sleep(1)

        # password
        password_input = driver.find_element_by_id('regPassword')
        send_keys_better(password_input, password)
        time.sleep(2)

        # click sign up button to spawn captcha checkbox
        driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[3]/button').click()

        # recaptcha
        driver.switch_to_frame(driver.find_element_by_css_selector('iframe[src^="https://www.google.com/recaptcha/api2/anchor?"]'))
        driver.find_element_by_xpath('//span[@id="recaptcha-anchor"]').click()
        driver.switch_to.parent_frame()
        driver.switch_to_frame(driver.find_element_by_css_selector('iframe[src^="https://www.google.com/recaptcha/api2/bframe?"]'))
        driver.find_element_by_xpath('//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
        time.sleep(10)
        driver.switch_to.parent_frame()

        # click sign up button
        driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[3]/button').click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[3]/button').click()
        except:
            pass
        time.sleep(5)


        # join random sub
        driver.get(f'https://www.reddit.com/r/{choice(subs)}')
        driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/button').click()
        time.sleep(5)
        driver.quit()
        
        # add new account info to accounts.json
        account_dict = {
                "username": username,
                'password': password,
                'email': email
            }
        sheets.add_account(account_dict)

        break
    except KeyboardInterrupt:
        break
    except Exception:
        driver.quit()
        continue
