
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json

class Crawling():
    def getsandle():
        main_url = "https://search.musinsa.com/category/005004"

        driver = webdriver.Chrome("C:/driver/chromedriver")
        driver.get(main_url)

        driver.implicitly_wait(3)

        infos = []

        try:
            for page in range(1, 3):

                driver.execute_script("listSwitchPage(document.f1,{}); return false;".format(page))
                driver.implicitly_wait(10)

                soup = BeautifulSoup(driver.page_source, "lxml")

                goods_list = soup.select("#searchList > .li_box")

                for goods in goods_list:

                    img_src = goods.find(class_='lazyload lazy')['data-original']
                    link = goods.find(class_='img-block')['href']
                    brdname = goods.find("p", {"class": "item_title"}).text
                    goname = goods.find(class_='img-block')['title']

                    price = goods.select(".price")[0].text
                    # price = price.replace.re(r"<del>.*?</del>", "")  if문 활용
                    price = price.replace("\n", "")

                    infos.append({"1. 썸네일":img_src, "2. 링크":link, "3. 브랜드명":brdname, "4. 상품명":goname, "5. 가격":price})
                    # print(infos)


        except Exception as e:
            print("페이지 파싱 에러", e)
        finally:
            time.sleep(3)
            driver.quit()

        return infos
