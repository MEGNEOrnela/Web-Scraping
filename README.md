# 🕸️ Web Scraping using Selenium


This work aims to extract content from a dynamic web page using the Selenium tool with Python. 
The `main.py` file contains code  to extract specific links' content from a given website. 
To execute the file, please consider the steps outlined below.

1. Download the appropriate WebDriver corresponding to your browser. Ensure that the WebDriver version matches your browser version. In this case, we are using Google Chrome, where the corresponding WebDriver can be download [here](https://sites.google.com/chromium.org/driver/).."

2. After obtaining the webdriver, run the below command and relocate the chrome driver file to the /usr/local/bin directory:
```bash
sudo mv chromedriver /usr/local/bin
```
you can check or find the chrome driver binary path by  running the following command in the terminal: 
```bash
which chromedriver
```

3.  create an activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
   ```
4. Install the requirements
```bash
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
   ```
5. Run the `main.py` file
```bash
python3  main.py
```
