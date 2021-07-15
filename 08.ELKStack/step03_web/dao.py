from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch()

def put():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])

def get():
    res = es.get(index="test-index", id=1)
    print(res['_source'])

# es.indices.refresh(index="test-index")

def match_all():
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])

    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

def kbcus_all():
    res = es.search(index="bank", body={"query": {"match": {"bank": "국민은행"}}, "size": 0, "aggs": {"kb_cus": {"sum": {"field": "customers"}}}})
    print("총 이용객 수 = %d" % res['aggregations']['kb_cus']['value'])

def kb_per_loc():
    res = es.search(index="bank", body={"query": {"match": {"bank": "국민은행"}}, "size": 0, "aggs": {"loc_count": {"terms": {"field": "location.keyword"}}}})
    return res['aggregations']['loc_count']['buckets']
    # [{'key': '불광', 'doc_count': 3}, {'key': '강남', 'doc_count': 2}, {'key': '신촌', 'doc_count': 2}, {'key': '양재', 'doc_count': 2}]


# if __name__ == '__main__':
    # get()
    # put()
    # match_all()
    # kbcus_all()
    # kb_per_loc()