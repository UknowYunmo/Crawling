from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("https://www.youtube.com/watch?v=CLR9dytvnmM&list=RDCLR9dytvnmM&start_radio=1")
browser.maximize_window()
time.sleep(2)
browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
num=soup.find_all('yt-formatted-string', class_ ='count-text style-scope ytd-comments-header-renderer')
print(num[0].get_text()) # 댓글 665개
comment_num=int(num[0].get_text()[3:-1]) # 665
#print(comment_num)
comment_list=[]
last_page_height = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = browser.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height
time.sleep(2)
html=browser.page_source
soup = BeautifulSoup(html, "lxml")
comment=soup.find_all('yt-formatted-string',class_ ='style-scope ytd-comment-renderer')
for i in comment:
    if i.get_text()!='''\n''':
        comment_list.append(i.get_text())
print(comment_list)
print(len(comment_list)) # 461