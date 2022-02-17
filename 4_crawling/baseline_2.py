'''
안녕하세요! 멋쟁이사자처럼 10기 운영진 crawling 강의를 맡은 정지원입니다. 
Webcrawling 
뉴스 헤더라인 & 링크 가져오기 실습입니다! :)

완성 파일은 이름_학번.py 형식으로 2/20까지 제출해주시면 됩니다.
제출 이메일: wony4094@likelion.org / sunaslight1508@likelion.org
'''
#pip install requests , beautifulsoup 
#라이브러리 import 
import requests
from bs4 import BeautifulSoup
#pyautogui 라이브러리 설치하기 (pip install pyautogui)
import pyautogui

#page 초기값
pageNum = 1

#검색어, page 입력받기
key = pyautogui.prompt("검색어를 입력하세요: ")
lastpage = pyautogui.prompt("몇 페이지까지 볼까요?: ") #string
#requests, 서버에 말 걸어보기

for j in range(1, int(lastpage)*10, 10):
    print(f"현재 페이지는 {pageNum}입니다.======================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={key}&start={lastpage}") #GET, POST 

    #html 불러오기
    html = response.text
    #Beautifulsoup으로 수프 만들기!
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit") # #id, .class

    for i in links:
        title = i.text
        url = i.attrs['href']
        print(title, url)
    pageNum+=1