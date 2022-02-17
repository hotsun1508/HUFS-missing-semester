#라이브러리 import 받기
import pyautogui
import requests
from bs4 import BeautifulSoup

#page 변수
pageNum = 1
#검색어 / page 입력받기
keyword = pyautogui.prompt("검색어를 입력하세요: ")
lastpage = pyautogui.prompt("몇 페이지까지 찾을까요?: ") #string > int로 바꿔주기

for i in range(1, int(lastpage)*10, 10):
    #현재 page 표시
    print()
    print(f"현재 {pageNum} 페이지 입니다.")
    print()
    #서버에 대화를 시도해보자.
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={pageNum}") #get("사용할 사이트 주소") 응답(response)에 넣어줌

    #서버에서 html을 불러오기
    html = response.text #text 메소드 설명

    #html 번역 선생님으로 수프를 만들기
    soup = BeautifulSoup(html, 'html.parser') #수프 만들어주기 

    #class= "logo_naver"인 놈을 찾아냄
    links = soup.select(".news_tit") #태그 선택 / soup.명령어 설명
    #개발자도구 - 돋보기로 탐색 - #id(고유한값) or .class (css 선택자 설명)
    #print(links)
    
    print("여기서부터 시작!=====")
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pageNum += 1
