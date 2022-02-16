## 셀레니움 설치하기
# $ pip install selenium
# $ pip3 install selenium


## 폴더 생성 후 Selenium 라이브러리 import 하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Enter
import time  # time.sleep()
import csv  # 파일로 저장하기

# 브라우저 생성
## browser변수 안에 Chrome driver 생성하기 
browser = webdriver.Chrome('C:/chromedriver.exe')  # 경로 입력
# mac의 경우 Documents폴더 아래 붙여넣기 --> /User/파일이름/Documents/chromedriver  (exe 없음)

# 웹사이트 열기 
## 웹 사이트 열고나서 f12(개발자 도구) 열기 
browser.get('https://www.naver.com')  # url 입력 -> 네이버를 열어라
## 로딩이 안돼서 클릭이 안되는 경우 방지를 위해 시간 할당
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
## 보기 버튼(네모 안에 커서 모양) 누른 후 쇼핑 클릭
### a 태그 > class명 "nav shop" : CSS 선택자 만들기 'a.nav.shop'
#### Finds an element by css selector.: CSS 선택자로 태그를 선택하는 명령어
browser.find_element_by_css_selector('a.nav.shop').click()  # 클릭을 실행하는 명령어
time.sleep(2)  # 로딩 시간 줌

## 선택자란 ????? 

# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

# 검색어 입력 
### -> 직접 입력 대신에 이렇게도 가능. 셀레니우믄 거의 만능!!
search.send_keys('아이폰 13')  # 키 입력 명령어
search.send_keys(Keys.ENTER)  # enter 치는 명령어

# 스크롤 전 높이: before height
## 접속하자마자는 스크롤 아래로 내리지 않았으니까 = 0
before_h = browser.execute_script("return window.scrollY")  # javascript의 명령어 실행할 수 있음


# 무한 스크롤 
## 무한 반복문 사용 !! 
while True: 
    # 맨 아래로 스크롤을 내린다. 
    browser.find_element_by_css_selector("body").send_keys(Keys.END)  # 모든 웹사이트에 있는 body 태그 > END키로 스크롤 맨 아래로 내리기

    # 스크롤 사이 페이지 로딩 시간 주기
    time.sleep(1)  # 각자 인터넷 환경에 따라 조금씩 다르게 설정 가능

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:  # 더이상 내려갈 곳이 없음. -> 마지막 부분에 도달함.
        break  # 같으면 무한 반복문 탈출하고 다음 명령어를 수행해라
    before_h = after_h  

# 파일 생성
## 인자: 경로 \data.csv, 쓰기 모드, 인코딩 - 안하면 깨짐, 윈도우 - 줄바꿈 방지
f = open(r"C:\Users\민용진\Desktop\멋쟁이사자처럼\10기 운영진\HUFS Missing Semester\Naver_shopping.py\data.csv", 'w', encoding='CP949', newline='')
csvwriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")  # elements: 여러개를 가지고 와서 list 형태로 반환해줌 

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
    # 데이터 쓰기
    csvwriter.writerow([name, price, link])

# 파일 닫기
f.close()