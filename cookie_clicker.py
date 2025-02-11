from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

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
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Wait for the page to load (adjust if needed)
time.sleep(5)

# Find the cookie button
cookie = driver.find_element(By.ID, 'cookie')

start = time.perf_counter()
last_check = start  # Last time upgrades were checked
RUNTIME = 300  # 5 minutes (300 seconds)

while time.perf_counter() - start < RUNTIME:
    # Keep clicking the cookie
    cookie.click()

    # Check every 5 seconds which upgrade can be bought
    if time.perf_counter() - last_check >= 5:
        last_check = time.perf_counter()  # Reset timer
        
        # Get current cookie count
        cookie_count_text = driver.find_element(By.ID, 'money').text.replace(",", "")
        cookie_count = int(cookie_count_text) if cookie_count_text.isdigit() else 0  # Handle potential errors

        # Get all upgrade prices
        upgrades = {
            "Cursor": driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split()[-1].replace(",", ""),
            "Grandma": driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split()[-1].replace(",", ""),
            "Factory": driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split()[-1].replace(",", ""),
            "Mine": driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.split()[-1].replace(",", ""),
            "Shipment": driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.split()[-1].replace(",", ""),
            "Alchemy": driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split()[-1].replace(",", ""),
            "Portal": driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.split()[-1].replace(",", ""),
        }

        # Convert upgrade prices to integers
        upgrades = {k: int(v) for k, v in upgrades.items() if v.isdigit()}

        # Find the most expensive upgrade that can be afforded
        affordable_upgrades = {k: v for k, v in upgrades.items() if cookie_count >= v}

        if affordable_upgrades:
            best_upgrade = max(affordable_upgrades, key=affordable_upgrades.get)  # Get the most expensive one
            print(f"Buying: {best_upgrade} for {affordable_upgrades[best_upgrade]} cookies")

            # Click the upgrade
            driver.find_element(By.ID, f"buy{best_upgrade}").click()

cookie_per_sec = driver.find_element(By.ID, 'cps')
print(cookie_per_sec.text)

# Quit WebDriver after runtime ends
driver.quit()
