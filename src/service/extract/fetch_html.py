import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_html(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    scroll_position = 0
    scroll_increment = 250 
    
    driver.execute_script("document.body.style.zoom='50%'")
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        scroll_position += scroll_increment
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.2)
        if scroll_position >= new_height:
            break

    return driver.page_source
    
    