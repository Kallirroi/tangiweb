### tangiWEB

The scripts do the following


- Programmatically enable the chrome extension in the `webdriver.Chrome()` instance. You need to provide the path to the .crx bundle of the extension like so: `chrome_options.add_extension('path/to/.crx')`. You also need to have downloaded the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Take screenshot of web page using Selenium (Python) while the extension is enabled. You can set the url in `screenshot.py`. 
- Save that image to `in/` directory
- Use `skimage` and `color.label2rgb` to average the saved screenshots in a 24 * 16 matrix


Useful links
- [https://hexdocs.pm/phoenix/overview.html](https://hexdocs.pm/phoenix/overview.html)
- [https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome](https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome)
- [https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium](https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium)
- [https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/](https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/)
