from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json


#set Headless mode to ensure that selenium will start Chrome in the "background" without any visual output or windows.
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)

url = "https://kidshealth.org/en/parents/nutrition-center/q-a/"

driver.get(url)

try:
    # Find some specific links on the main webpage
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"subcategory"))
    )
    subcategory_div = driver.find_element(By.CLASS_NAME,"subcategory")
    all_links = subcategory_div.find_elements(By.TAG_NAME, "a")

    links_to_extract = [(link.text, link.get_attribute("href")) for link in all_links if link.get_attribute("href")]
    print(len(links_to_extract))

    pages_content = []   # where we save the scraped content

    # Iterate through the links and extract their content
    for link_text, link_href in links_to_extract:
            
            # Switch to the new tab or window (if needed)
            driver.get(link_href)
            
            # Scrape content from the linked page
            linked_page_content = driver.find_element(By.XPATH,"/html/body").text
            
            # Print and store the content as needed
            print(f"Content from link '{link_text}' ({link_href}):\n")
            pages_content.append({"url":link_href, "text":linked_page_content})
            
            # Switch back to the main tab or window
            driver.get(url)

    with open("data/page_content.json", "w") as f:
        json.dump(pages_content, f)

except Exception as e:
    print(f"Status Failed On {str(e)}")

finally:
    driver.quit()