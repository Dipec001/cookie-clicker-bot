from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Define ChromeDriver path
driver_path = r"C:\development\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Initialize ChromeDriver service correctly
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize browser window
driver.maximize_window()

# Open Wikipedia
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_input = driver.find_element(By.NAME, 'fName')
fname_input.send_keys('divine')
lname_input = driver.find_element(By.NAME, 'lName')
lname_input.send_keys('chukwu')
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('hello@gmail.com')
sign_up_button = driver.find_element(By.CSS_SELECTOR, '.form-signin button')
sign_up_button.click()


# Quit the driver after loading the page
driver.quit()
