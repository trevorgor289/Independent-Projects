service = Service("/Users/fengchen/Development/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(5)

driver.get("https://tinder.com/")


time.sleep(5)
agreement = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
agreement.click()

log_in = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()

time.sleep(5)
facebook_login = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div')
facebook_login.click()

time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(5)
fb_email = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
fb_email.send_keys("tgordon289098@gmail.com")
time.sleep(5)
password = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys("barcelona@289")
password.send_keys(Keys.ENTER)

#revert back to the base_window and verify by printing the title

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(20)
location = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()
time.sleep(5)
notification = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
notification.click()
time.sleep(5)



fullscreen = driver.find_element(By.XPATH, value='/html/body')

x = 0
while True:

    try:
        fullscreen.send_keys(Keys.ARROW_RIGHT)

        print(x)




    except ElementClickInterceptedException:
        try:
            fullscreen.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)