'''
제공 후 분석 및 이해하기

절대 경로와 상대 경로 url 관리하는 연습
'''

#urllib - package명
#parse - 파일명(모듈명)
#urljoin - parse.py 내부에 내장된 urljoin 함수
#syntax: urljoin(절대url, 상대url)

from urllib.parse import urljoin

# 절대 url
base = "http://example.com/html/a.html"

# b.html은 a.html와 같은 폴더에 저장되어 있다고 가정
# a.html 대신 b.html로 자동 변환
print(urljoin(base, "b.html")) #http://example.com/html/b.html

# pdf p29~30 참고
# authority : 뒤에 나오는 일반적인 호스트 이름 , 사용자이름 , 비밀번호 , 포트 번호 등을 포함
# 슬래쉬 하나 표기는 authority 부분까지만 유효하게 인식
print(urljoin(base, "/b.html")) #http://example.com/b.html

# ../ : 현 위치에서 상위 디렉토리
# a.html 위치에서 상위 위치는 html의 위치
print(urljoin(base, "../b.html")) #http://example.com/b.html

print(urljoin(base, "../img/b.html")) #http://example.com/img/b.html

print(urljoin(base, "../css/cssView.css")) #http://example.com/css/cssView.css

# 문법 오류는 없으나 표현은 논리적으로 부적합
print(urljoin(base, "../../css/cssView.css")) #http://example.com/css/cssView.css

print(urljoin(base, "/../../css/cssView.css"))  #http://example.com/css/cssView.css  