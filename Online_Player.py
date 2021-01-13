from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import datetime
user_id=input('itwill 아이디를 입력해주세요 : ')
user_password=input('itwill 비밀번호를 입력해주세요 : ')
print()
print()
print('혹시 도중에 멈추고 싶으시면 정지 버튼으로는 바로 안 멈추더라구요')
print('멈추시려면 아나콘다를 재실행 해주시는 게 제일 빨라요!')
print('무한 루프는 아니고 30번 넘기면 멈추게 설정되어있으니 그 부분은 걱정하지 않으셔도 됩니당')
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("https://itwill.step.or.kr/page/lms")
browser.maximize_window()
browser.find_element_by_xpath("//*[@class='btn_login show_when_not_logged_in menu_link']").click()
time.sleep(3)
browser.implicitly_wait(3)
browser.find_element_by_id('id_input').send_keys(user_id)
browser.find_element_by_id('pw_input').send_keys(user_password)
browser.find_element_by_xpath("//*[@class='login_button text_button']").click()
time.sleep(3)
browser.implicitly_wait(3)
browser.find_element_by_xpath("//*[@class='btn_normal fullBlue alert_confirm_button']").click()
time.sleep(5)
browser.implicitly_wait(5)
browser.find_element_by_xpath("//*[@class='left']").click()
time.sleep(5)
browser.implicitly_wait(5)
browser.find_element_by_xpath("//*[@class='right']").click()
cnt=-1
print()
print('-------------------------시작-------------------------')
while(True):
    cnt+=1
    print()
    print('---지금까지',cnt,'번 이동했습니다---')
    print()
    print('-5초 대기중-')
    print()
    time.sleep(5)
    browser.implicitly_wait(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    try:
        running=soup.find_all('div', class_ ='time_sub_menu on status2')[0]
    except:
        try:
            running=soup.find_all('div', class_ ='time_sub_menu on status1')[0]
        except:
            print('인증 창이 뜬 것 같습니다, 프로그램을 종료합니다')
            break
    try:
        t=running.find_all('div', class_='during_time')[0].get_text()
        print(t)
        now=str(datetime.datetime.now())
        min=int(t[3:5])*60
        sec=int(t[6:8])
        wait=min+sec+3
        print('현재 시간인',now[11:19],'에서 약',int(min/60),'분',int(sec+3),'초 후 넘어갑니다')
        time.sleep(wait)
        browser.implicitly_wait(wait)
        browser.find_element_by_xpath("//*[@class='right']").click()
    except:
        browser.find_element_by_xpath("//*[@class='right']").click()
        print('시간초가 없는 영상이므로 5초 후 넘어갑니다')
        time.sleep(5)
        browser.implicitly_wait(5)
    if cnt==30:
        break