from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Add custom headers
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36')
# chrome_options.add_argument('accept-language=en-US,en;q=0.9')

class PythonOrg:
    def __init__(self, url, driver_path, timeout=10):
        self.url = url
        self.driver_path = driver_path
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
    
    def scrape_events(self):
        self.driver.get(self.url)
        anchors = self.driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery .menu li a')
        dates = self.driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery .menu li time')

        events_dict = {}

        print("Upcoming Python Events:")
        for index, (a, d) in enumerate(zip(anchors, dates)):
            events_dict[index] = {'time': d.text, 'event': a.text}
        
        print(events_dict)

        self.driver.quit()

if __name__ == "__main__":
    driver_path = r"C:\development\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    url = "https://www.python.org/"
    
    scraper = PythonOrg(url, driver_path)
    scraper.scrape_events()
    print("ChromeDriver is working!")
