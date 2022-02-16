"""
Webcrawling 실습에 오신 여러분 환영합니다! *^^*
아래와 같이 베이스라인 코드를 제공하오니, 
실습 후에는 실습 파일을 꼭 제출해주셔야 수료하실 수 있다는 점 유의해주세요.

- 실습 파일: 현재.py 파일 또는 저장 완료 후 .csv 파일
- 제출 이메일: wony4094@likelion.org / sunaslight1508@likelion.org
"""

#%%############################### 셀레니움 설치하기 #####################################
# (윈도우) $ pip install selenium
# (Mac) $ pip3 install selenium


#%%################################ 크롬 드라이버 설치하기 ####################################
# chromedriver.exe


#%%############################### 라이브러리 import 하기 #########################################
# 1. Selenium 
from selenium import webdriver

# 2. 키보드 엔터 key
from selenium.webdriver.common.keys import Keys

# 3. 로딩 시간 time.sleep()
import time 

# 4. csv 파일로 저장
import csv 

#%%################################### 브라우저 생성 ###############################################
## browser변수 안에 Chrome driver 생성하기 
# (윈도우) C 드라이브 
# (mac) Documents 

 # 경로 입력

#%%#################################### 웹사이트 열기 ###############################################
browser.get('https://www.naver.com')  # url 입력
browser.implicitly_wait(10) # 로딩 시간 주기

#%%#################################### 쇼핑 메뉴 클릭 ###############################################

## a 태그 > class명 "nav shop" 
## QUIZ. CSS 선택자로 태그를 선택하는 명령어 ??? 


# 클릭을 실행하는 명령어


# 로딩 시간을 주는 명령어


#%%################################# 선택자란 ????? ###############################################


#%%#################################### 검색창 클릭 ###############################################

search = browser.find_element_by_css_selector('')
search.click()


#%%############################### 검색어 입력 ###############################################

# 키 입력 명령어

# enter 치는 명령어

## search.send_keys 사용하기


## QUIZ? 스크롤 전 높이 'before height'는 ??? 
before_h = browser.execute_script("return window.scrollY")  # javascript의 명령어 실행할 수 있음



# 무한 스크롤 
## 무한 반복문 사용 !! 
while True: 
    # 맨 아래로 스크롤을 내린다. 
    ## 모든 웹사이트에 있는 body 태그 > END키로 스크롤 맨 아래로 내리기

    ## 스크롤 사이 페이지 로딩 시간 주기

    # 각자 인터넷 환경에 따라 조금씩 다르게 설정 가능

    # 스크롤 후 높이
    after_h = 

    ## 더이상 내려갈 곳이 없는 경우,
    # QUIZ. 무한 반복문 탈출하고 다음 명령어를 수행해라 ! 나타내는 단어는?? 
    if after_h == before_h:

    before_h = after_h  

#%%######################################### 파일 생성 ###############################################
## 인자: 경로 \data.csv, 쓰기 모드, 인코딩 - 안하면 깨짐, 윈도우 - 줄바꿈 방지
f = open(r"\data.csv", 'w', encoding='CP949', newline='')
csvwriter = csv.writer(f)


#%%######################################### 상품 정보 div ###############################################
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")  # elements: 여러개를 가지고 와서 list 형태로 반환 

for item in items:
    name = item.find_element_by_css_selector("").text
    try:
        price = item.find_element_by_css_selector("").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector("").get_attribute('href')
    print(name, price, link)
    # 데이터 쓰기
    csvwriter.writerow([name, price, link])

#%%################################## 파일 닫기 ###############################################
f.close()
# %%
