import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

executable_path = "./chromedriver"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('/Users/Kallirroi/Desktop/tangiweb.crx')
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

driver.get("http://bbc.com")
print('getting driver')
driver.maximize_window()

# should have a scrolling and screenshoting loop here
print('taking screenshot')
driver.save_screenshot('in/screenshot.png')
print('saving screenshot')
driver.quit()