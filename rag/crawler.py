from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests 
class GoogleCrawler:
    def __init__(self):
        # 웹 드라이버 설정
        self.__driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        # 구글 검색 페이지 열기
        self.__driver.get("https://www.google.co.kr/")
        
        time.sleep(2)

    def search_urls(self, query = "충남대학교 전과"):
        # 검색어 창을 찾아 search 변수에 저장 
        search_box = self.__driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
        
        # 검색 결과가 로드될 때까지 대기
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@jsname="UWckNb"]'))
        )
        
        # <a> 태그에서 href 속성 추출
        link_element = self.__driver.find_elements(By.XPATH, '//a[@jsname="UWckNb"]')
        hrefs = list()
        
        for element in link_element:
            hrefs.append(element.get_attribute('href'))
        
        print(hrefs)
        return hrefs
    
    def beautifulize(self, result):
        pass
    
    def test_pipeline(self, query = "충남대학교 전과"):
        urls = google_crawler.search_urls(query)
        
        for url in urls:
            if ".pdf" in url:
                body = requests.get(url=url)
                text = body.content.decode('euc-kr')
                print(text[:1000])
        
        return
        

google_crawler = GoogleCrawler()
google_crawler.test_pipeline()