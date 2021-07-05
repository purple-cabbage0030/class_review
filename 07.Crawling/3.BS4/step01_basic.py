'''
html 문서의 tree 구조로 특정 tag 및 text data를 찾아가는 형식은 DOM 기반
- DOM: Document Object Model
    html의 모든 요소(tag, 속성, text)를 객체로 관리
    실시간 가변적인 동적 화면 구성에 필수 핵심 기술 / 해킹 필수 기술
    화면을 변경시키는 기술 셋
    스펙: w3c에서 제시, dom 기술을 지원하는 개발 언어들은 모든 언어가 지원
    수업 시간에는 js 기반의 dom 처리 학습 중
    - id로 특정 tag 검색해서 착출: document.getElementById("고유한 id")
    - next_sibling: 현 위치 상에서 다음 동생 검색


html의 필수 표현법
    . : class 속성
    # : id 속성
    name : tag 명

'''



html='''
<html>
    <body>
        <h1>스크래핑이란?</h1>
        <h1>hello?</h1>
        <p id="one">웹페이지 1</p>
        <p id="two">웹페이지 2</p>
        <span class="redColor">
            <p>웹페이지3</p>
        </span>
        <ul>
            <li><a href="www.daum.net">다음</a></li>
            <li><a href="www.naver.com">네이버</a></li>
        </ul>        
    </body>
</html>
'''


# bs4: html 문서를 tag, 속성, css 등으로 섬세하게 관리 가능한 API
from bs4 import BeautifulSoup

# 크롤링 대상의 데이터와 구문 해석, 문법 체킹, 변환 가능한 parser 설정
soup = BeautifulSoup(html, 'html.parser')

print('--- 2: find() 함수 ---')
print(soup.find(id='one'))   # <p id="one">웹페이지 1</p>
print(soup.find(id='one').string)   # 웹페이지 1

'''
html 문서 상에서 css는 중복 표현이 가능: 이름이 동일하게 적용해서 공통 ui 설계함
.redColor: 클래스 속성이 redColor인 것들을 찾음
    반환값이 하나 이상일 가능성이 있으므로 리스트로 반환함.

.redColor p: 여백을 기준으로 p는 클래스 속성값이 redColor인 tag의 자식인 p 태그를 찾는 표현
    하위 태그가 여러 개 존재할 가능성이 있으므로 리스트 타입으로 반환

('.redColor p')[0]: 리스트 내 첫 번째에 해당하는 p 태그 반환

하위 text 데이터 출력을 위해 .string 또는 get_text() 이용 가능 (text인 경우에만 데이터 착출)
'''
print(soup.select('.redColor'))   # [<span class="redColor"><p>웹페이지3</p></span>]
print(soup.select('.redColor p'))   # [<p>웹페이지3</p>]
print(soup.select('.redColor p')[0])   # <p>웹페이지3</p>
print(soup.select('.redColor p')[0].string)   # 웹페이지3




print('--- 1 ---')
print(soup.html.h1)   # <h1>스크래핑이란?</h1>
print(type(soup.html.p))   # <class 'bs4.element.Tag'> 'tag' 속성의 객체
print(soup.html.p)   # <p id="one">웹페이지 1</p>

# html(xml) 문서는 족보 구조 = tree 구조
# .next_sibling: 현 위치 상에서 다음 내 형제를 의미
# html 상에서 new line(br tag)은 text 자식으로 간주
print(soup.html.p.next_sibling)   # 엔터 쳐서 나오는 빈 공간(new line)도 자식으로 간주
print(soup.html.p.next_sibling.next_sibling)   # <p id="two">웹페이지 2</p>
print(soup.html.p.next_sibling.next_sibling.next_sibling)
print(soup.html.p.next_sibling.next_sibling.next_sibling.next_sibling)   # <span class="redColor"><p>웹페이지3</p></span>

print(soup.html.span.p)    # <p>웹페이지3</p>

# text 데이터들은 string과 get_text() 함수로 가져올 수 있다
print(soup.html.span.p.string)   # 웹페이지3
print(soup.html.span.p.get_text())    # 웹페이지3