### tangiWEB

The scripts do the following


- Programmatically enable the chrome extension in the `webdriver.Chrome()` instance. You need to provide the path to the .crx bundle of the extension like so: `chrome_options.add_extension('path/to/.crx')`
- Take screenshot of web page using Selenium (Python) while the extension is enabled. You can set the url in `screenshot.py`. 
- Save that image to `in/` directory
- Use `skimage` and `color.label2rgb` to average the saved screenshots in a 24 * 16 matrix