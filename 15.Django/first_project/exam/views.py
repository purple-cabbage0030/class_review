from django.shortcuts import render
from django.http import HttpResponse, response
from datetime import datetime

# View 함수 작성
# View: 사용자 요청을 받아서 처리하는 함수

def hello(request):
    # 사용자 요청을 받아서 "인사와 현재 날짜/시간" 반환하는 view
    
    # 현재 날짜와 시간 조회
    curr = datetime.now()

    # 응답할 html text 생성
    txt = """
    <html>
        <body>
            안녕하세요. 반갑습니다. <br>
            현재 일시: {}
        </body>
    </html>
    """
    response_txt = txt.format(curr)

    # HttpResponse 생성
    response = HttpResponse(response_txt)
    return response
