import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from cStringIO import StringIO

executable_path = "./chromedriver"
os.environ["webdriver.chrome.driver"] = executable_path


# extension = sys.argv[1]
extension = "everything"

chrome_options = Options()
chrome_options.add_extension('/Users/Kallirroi/Desktop/tangiWeb/extensions/'+str(extension)+'/'+str(extension)+'.crx')
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

url = "https://cnn.com"
print(url)
driver.get(url)
print('getting driver')
driver.maximize_window()

# should have a scrolling and screenshoting loop here
print('taking screenshot')
js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
scrollheight = driver.execute_script(js)

slices = []
offset = 0
counter= 0
while offset < scrollheight:
    driver.execute_script("window.scrollTo(0, %s);" % offset)
	# (2400, 5477)
    screenshot = Image.new('RGB', (2400, scrollheight))
    img = Image.open(StringIO(driver.get_screenshot_as_png()))
    screenshot.paste(img, (0, offset))
    offset += img.size[1] / 10
    slices.append(img)
    counter += 1
    screenshot.save('/Users/Kallirroi/Desktop/temp/tangiWEB/screen_'+str(counter)+'.png')
    # driver.get_screenshot_as_file('%s/screen_%s.png' % ('/Users/Kallirroi/Desktop/temp/tangiWEB/', counter))

screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
offset = 0
for img in slices:
    screenshot.paste(img, (0, offset))
    offset += img.size[1]

screenshot.save('tests/semantic/'+str(extension)+'/screenshot.png')
print('saving screenshot')
driver.quit()