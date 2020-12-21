from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  urllib.request
import time
f=open('c:\\data\\gimo.txt','w',encoding='UTF-16')
binary = 'C:\chromedriver\chromedriver.exe'    # 크롬 드라이버 사용
browser = webdriver.Chrome(binary)    # 브라우져를 인스턴스화
browser.get("https://play.google.com/store/apps/details?id=com.appsphere.innisfreeapp&showAllReviews=true")
browser.maximize_window()
browser.implicitly_wait(3)
t=0
while(True):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    try:
        ele=browser.find_element_by_xpath('//div[@class="U26fgb O0WRkf oG5Srb C0oVfc n9lfJ"]')
        if (ele is not None):
            ele.click()
            break
    except Exception:
        t+=1
        print(t)
browser.implicitly_wait(10)
suc=0
err=0
while(suc<3 and err<20):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    try:
        ele=browser.find_element_by_xpath('//div[@class="U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d"]')
        if (ele is not None):
            ele.click()
            suc+=1
            err=0
            print(suc)
    except Exception:
        err+=1

browser.implicitly_wait(10)
html = browser.page_source
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정
#print(soup)
#result1=soup.find_all('div',class_ ='UD7Dzf')
#print(result1)
result1=soup.find_all('span',jsname='bN97Pc')
params=[]
for i in result1:
    params.append(i.get_text())
print(len(params))
print(params)
for i in params:
    f.write(i+'\n')