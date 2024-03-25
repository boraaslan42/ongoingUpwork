def getGeneralCookies(i):
    print(i,2)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


options = Options()
options.add_argument("start-maximized")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service('C:\\BrowserDrivers\\chromedriver.exe')

driver = webdriver.Chrome(options=options)
# Selenium Stealth settings
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
url = 'https://www.indeed.com/q-usa-jobs.html?vjk=cb6f8784a20d240b'
driver.get(url)
cookies = driver.get_cookies()
cookie_str = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
print(cookie_str)

driver.quit()  # Close the browser

