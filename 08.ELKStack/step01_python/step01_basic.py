from datetime import datetime
from elasticsearch import Elasticsearch

# ES를 사용 가능한 python 객체 생성. crud 기능을 보유한 객체
# 이 소스가 실행 중인 시스템(해당 ip)에서 실행되는 ES에 자동 접속
es = Elasticsearch()

def put():
    '''
    doc라는 변수에 3개의 field 선언해서 값 설정
    python 자체적으로는 dict 타입
    es 관점에서는 field와 value
    datetime.now(): 현 날짜, 시간 표현하는 함수
    '''
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }

    # 'test-index'에 id가 1인 doc 저장, 결과 정보 출력
    # index(): ES가 보유한 index 생성 함수
    # body: 저장될 데이터 지정
    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])   # created or updated

def get():
    # 'test-index'에서 id가 1인 문서 검색, 저장 데이터 출력
    res = es.get(index="test-index", id=1)
    print(res['_source'])

# es.indices.refresh(index="test-index")

def match_all():
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])

    # "%(키)s %(키2)s" % dict 구조의 데이터 ==> 해당 key와 일치되는 value를 문자열 포맷에 자동 적용
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

def kbcus_all():
    res = es.search(index="bank", body={"query": {"match": {"bank": "국민은행"}}, "size": 0, "aggs": {"kb_cus": {"sum": {"field": "customers"}}}})
    print("총 이용객 수 = %d" % res['aggregations']['kb_cus']['value'])

def kb_per_loc():
    # 국민 은행 지역별 지점 개수
    res = es.search(index="bank", body={"query": {"match": {"bank": "국민은행"}}, "size": 0, "aggs": {"loc_count": {"terms": {"field": "location.keyword"}}}})
    for key in res['aggregations']['loc_count']['buckets']:
        # print(key['key'])    # 불광 강남 신촌 양재
        print("지역명: %(key)s, 지점 개수: %(doc_count)d개" % key)


if __name__ == '__main__':
    # get()
    # put()
    # match_all()
    # kbcus_all()
    # kb_per_loc()

    pass