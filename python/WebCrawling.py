from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# 절차 :
# - selenium 버전에 맞는 driver 설치
# - 드라이버 인스턴스화
# - get 통해 사이트 접속
# - WebDriverWait 통해 HTML 요소 받아오기
#

DRIVER_PATH = "./chromedriver.exe"
s = Service(DRIVER_PATH)

# 자동 종료 방지 옵션 설정
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=s, options=options)
driver.get("https://map.naver.com/")

search_box = WebDriverWait(driver, timeout=3).until(
    lambda d: d.find_element(By.ID, "search_box_id"))
search_box.send_keys("some_key_word")
search_box.send_keys(Keys.ENTER)
