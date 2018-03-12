### tangiWEB


- `screenshot.py` programmatically enable the chrome extension in the `webdriver.Chrome()` instance. You need to provide the path to the .crx bundle of the extension like so: `chrome_options.add_extension('path/to/.crx')`. You also need to have downloaded the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- It then takes screenshot of web page using Selenium (Python) while the extension is enabled. You can set the url in `screenshot.py`. 
- It scrolls along the full length of the page and saves the interim screenshots in `temp/` folder.
- `pixelate.py` pixelizes the long screenshot in 16 left-to-right squares, and saves it.
- `invert.py` grays and saves the final output.
- `ocamyGO.py` loads the final output from above (which by now is pixelated, in grayscale and inverted), and creates a 16 * 24 matrix out of it. Since the image is gray, all the rgb values are equal, and we don't need to average them separately.
- it saves the matrix into a file `output.txt` which then gets sent to the `room:lobby` channel using the `ws://dlevs.me:4000/socket` socket.

All of the above can be used independently to test the system.

Useful links
- [https://hexdocs.pm/phoenix/overview.html](https://hexdocs.pm/phoenix/overview.html)
- [https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome](https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome)
- [https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium](https://stackoverflow.com/questions/30141847/how-to-select-chrome-extensions-to-enable-when-using-selenium)
- [https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/](https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/taking-screenshot-of-a-page/)
- [https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/](https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/)
- [https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html)

![process](https://github.com/Kallirroi/tangiweb/blob/master/process.gif)
