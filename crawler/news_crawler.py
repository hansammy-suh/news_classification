import requests

"""
청와대: https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=264&sid1=100&date=20200303&page=4


8개 카테고리, 각 카테고리 별 세부 6, 8, 10, 11, 5, 8, 1, 1 카테고리
목표 수집량 50만 개 기사
1개 카테고리 당 62,500개 기사
정치: 10,417개 기사
경제: 7,813개 기사
사회: 6,250개 기사
생활/문화: 5,682개 기사
세계: 12,500개 기사
IT/과학: 7,813개 기사
연예: 62,500개 기사
날씨: 62,500개 기사

정치 ~ IT/과학 각 페이지 당 기사 수 20

20 * 365(매년 36.5일 랜덤하게 뽑아 10년 간 데이터) * 페이지 수 = 10,417
정치 카테고리 내 각 세부 카테고리의 1일 할당 페이지 수 = 1.42



1. 큰 카테고리 내 각 세부 카테고리의 general 페이지 들어가기
2. 해당 페이지 내 뉴스 링크 20개 가져오기
3. 1, 2를 반복하여 62500개 기사의 링크 가져오기
4. 3의 과정을 마치면 62500개의 링크가 리스트에 담겨있게 됨
5. 해당 리스트를 타겟으로 뉴스 기사 저장하기
6. 1 ~ 5를 반복하면 8개 카테고리에 대한 총 50만 개의 기사가 저장됨

1. 카테고리 별 기사 링크 저장하는 스크립트
2. 카테고리 별 기사 다운로드하는 스크립트

"""

num_of_news = 500000
num_of_news_per_category = 62500


num_of_news_of_politics = 10417
num_of_news_of_economy = 7813
num_of_news_of_social = 6250
num_of_news_of_living_culture = 5682
num_of_news_of_world = 12500
num_of_news_of_tech_science = 7813
num_of_news_of_entertainment = 62500
num_of_news_of_weather = 62500

num_of_news_per_page_of_group_1 = 20
num_of_news_per_page_of_group_2 = 30
num_of_news_per_page_of_group_3 = 18



target_url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=264&sid1=100&date=20200304&page=7'

response = requests.get(target_url)

body = response.text


from bs4 import BeautifulSoup

soup = BeautifulSoup(body, 'lxml')

list = soup.find('div', class_='newsflash_body')

hrefs= []




#print(list)

for a in list.find_all('a', href=True):
	hrefs.append(a['href'])



#print(hrefs)
#print(len(hrefs))


qq = [x for i, x in enumerate(hrefs) if x not in hrefs[:i]]

print(qq)
print(len(qq))