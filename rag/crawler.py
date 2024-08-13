from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class GoogleCrawler:
    def __init__(self):
        # 웹 드라이버 설정
        self.__driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        # 구글 검색 페이지 열기
        self.__driver.get("https://www.google.com")

    def search(self, query = "충남대학교"):
        search_box = self.__driver.find_element(By.NAME, "q")
        search_box.send_keys(query)

        result = search_box.submit()
        return result


google_crawler = GoogleCrawler()