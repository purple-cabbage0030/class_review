# https://titanic1997.tistory.com/45


html='''<!DOCTYPE html>
<html lang="ko">
<body>
  <div id="main-goods" role="page">
      <h1>과일과 야채</h1>
      <ul id="fr-list">
        <li class="red green" data-lo="ko">사과</li>
        <li class="purple" data-lo="us">포도</li>
        <li class="yellow" data-lo="us">레몬</li>
        <li class="yellow" data-lo="ko">오렌지</li>
      </ul>
      <ul id="ve-list">
        <li class="white green" data-lo="ko">무</li>
        <li class="red green" data-lo="us">파프리카</li>
        <li class="black" data-lo="ko">가지</li>
        <li class="black" data-lo="us">아보카도</li>
        <li class="white" data-lo="cn">연근</li>
      </ul>
    </div>
</body>
'''

'''
원하는 크롤링 결과

레몬
아보카도
파프리카
아보카도
아보카도
아보카도
'''
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

'''
print(soup.select_one("#fr-list > li.yellow[data-lo='us']").string)
print(soup.select_one("#ve-list > li.black[data-lo='us']").string)
print(soup.select_one("#ve-list > li[class='red green'][data-lo='us']").string)
print(soup.select_one("#ve-list > li.black[data-lo='us']").string)
print(soup.select_one("#ve-list > li.black[data-lo='us']").string)
print(soup.select_one("#ve-list > li.black[data-lo='us']").string)
'''
# step01 : css 선택자로 데이터 추출하기 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
print(soup.select_one("li:nth-of-type(3)").string)              # 레몬
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)   # 아보카도

# id가 ve-list 하위의 모든 li tag 중에서 속성명이 data-lo=us인 모든 tag를 리스트(배열)로 반환
# 배열/리스트로 반환되었으니 고유한 index로 구분해서 사용
print(soup.select("#ve-list > li[data-lo='us']")[0].string)     # 파프리카
print(soup.select("#ve-list > li.black")[1].string)             # 아보카도

# step02 : find() 함수로 추출하기
# 속성이 하나 이상인 경우 적용하는 기술 - 딕셔너리 형식으로 작업
attDatas = {"data-lo":"us", "class":"black"}
# 두 가지 속성을 보유하고 있는 li tag를 찾아달라는 요청
print(soup.find("li", attDatas).string) # 아보카도

# step03 : find() 함수로 연속적으로 추출하기
# 메소드 또는 함수의 체이닝 기술
print(soup.find(id="ve-list").find("li", attDatas).string)  #아보카도


