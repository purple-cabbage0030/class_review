import re

from urllib.request import urlopen
from html import unescape

def main():
    pass

#로직 - 완성
def main():

    html = crawl('https://brunch.co.kr/')
    # print(html)

    kwords = scrape(html)
    # print(kwords)



def crawl(url):  
    f = urlopen(url)
    
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)

    return html

    

def scrape(html):

    kwords = []

    '''
    <a class="keyword_item brunch_keyword_item" href="/keyword/시사·이슈?q=g" target="_blank" style="left: 240px; top: 0px;"><span class="keyword_item_txt">시사·이슈</span><span class="ico_brunch"></span></a>
    <button type="button" data-id="28" class="keyword_item popular-keyword #home_writers_top_keywords on">스타트업</button>
    '''

    for data in re.findall(r'<a class=.*?</a>', html):
        print(data)
        print('실패')

    #     # kwords.append(data)
    
    # return kwords


if __name__ == "__main__":
    main()



