### tangiWEB


![process][https://github.com/Kallirroi/tangiweb/blob/master/process.gif]

`run.sh` does the following:


- Programmatically enable the chrome extension in the `webdriver.Chrome()` instance. You need to provide the path to the .crx bundle of the extension like so: `chrome_options.add_extension('path/to/.crx')`. You also need to have downloaded the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Take screenshot of web page using Selenium (Python) while the extension is enabled. You can set the url in `screenshot.py`. 
- Scroll along the length of the page so that it can screenshot it entirely. Save this in `temp/` folder.
- Pixelize it in 16 left-to-right squares. Saves that image.
- Grays and saves the final output.


Useful links
- [https://hexdocs.pm/phoenix/overview.html](https://hexdocs.pm/phoenix/overview.html)
- [https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome](https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome)
- [https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium](https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium)
- [https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/](https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/)
- [https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/](https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/)
- [https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html)
