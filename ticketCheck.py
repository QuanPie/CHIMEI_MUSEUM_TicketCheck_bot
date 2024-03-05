from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime


def is_ticket_soldable():
    # 設定 webdriver 並讓他不顯示
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # 設定網址並載入網頁
    url = "https://chimeimuseum.fonticket.com/ticket/earlybird"
    driver.get(url)
    # 等待最多十秒，直到xpath '//*[@id="purchaseBtnDiv"]/p/span' 出現
    wait = WebDriverWait(driver, 10)  # 最多等待 10 秒
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="purchaseBtnDiv"]/p/span')))
    # 回傳 售完狀態
    return element.text

def main(wait_time = 1):
    # 檢查間隔時間（秒）
    time.sleep(wait_time)
    # 售票狀態
    stock_state = is_ticket_soldable()
    # 當下時間
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 組合字串
    message = stock_state, now
    if stock_state == 'Soldout':
        return (0, *message)
    else :
        return (1, *message)


if __name__ == "__main__":
    main()