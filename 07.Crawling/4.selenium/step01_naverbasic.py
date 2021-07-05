# pip install selenium & chrome driver 세팅

from selenium import webdriver
import time   # 실행을 잠시 중지 (sleep(초단위))

# step01 : 네이버(크롬 브라우저) 실행
driver = webdriver.Chrome("c:/driver/chromedriver")

# http의 문서를 획득(브라우저에 실행시킬 사이트 url값을 직접 요청하는 가본 방식 즉 get방식으로 제공)
driver.get("https://www.naver.com/")

# tag 검색
'''
<input id="query" name="query" type="text" title="검색어 입력" maxlength="255" class="input_text" tabindex="1" accesskey="s" 
style="ime-mode:active;" autocomplete="off" placeholder="검색어를 입력해 주세요." 
onclick="document.getElementById('fbm').value=1;" value="" data-atcmp-element="">
'''
tag = driver.find_element_by_name("query")

# 검색한 input tag의 내용 삭제
tag.clear()  # 검색 입력창 clear

# input tag에 데이터 입력 = 키보드로 입력하는 것과 동일
tag.send_keys("AI")  # 입력

# 전송(검색) 버튼 클릭(사용자 엔터 입력과 동일한 action) -> 데이터 검색된 화면으로 이동
tag.submit()

time.sleep(20)    # 실행 중인 프로그램 설정된 초만큼 중지
driver.quit()     # 자원 반환 측면에서 driver도 중지 필수
