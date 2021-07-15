import csv, requests
import pandas as pd
import schedule
import time
# https://lemontia.tistory.com/508
 
def cc():
    CSV_URL = 'http://raw.githubusercontent.com/jooeungen/coronaboard_kr/master/kr_regional_daily.csv'

    # 확진, 사망, 격리해제
    yesterday_data = {}
    yesterday_data['서울'] = [0, 0, 0]
    yesterday_data['부산'] = [0, 0, 0]
    yesterday_data['대구'] = [0, 0, 0]
    yesterday_data['인천'] = [0, 0, 0]
    yesterday_data['광주'] = [0, 0, 0]
    yesterday_data['대전'] = [0, 0, 0]
    yesterday_data['울산'] = [0, 0, 0]
    yesterday_data['세종'] = [0, 0, 0]
    yesterday_data['경기'] = [0, 0, 0]
    yesterday_data['강원'] = [0, 0, 0]
    yesterday_data['충북'] = [0, 0, 0]
    yesterday_data['충남'] = [0, 0, 0]
    yesterday_data['전북'] = [0, 0, 0]
    yesterday_data['전남'] = [0, 0, 0]
    yesterday_data['경북'] = [0, 0, 0]
    yesterday_data['경남'] = [0, 0, 0]
    yesterday_data['제주'] = [0, 0, 0]
    yesterday_data['검역'] = [0, 0, 0]

    flag = False
    csv_data = []

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            # 날짜가 같으면 pass
            if row[0] == 'date':
                continue

            # 다음부터 과거 데이터의 차이만 다시 저장
            row[2] = int(row[2]) - int(yesterday_data[row[1]][0])
            row[3] = int(row[3]) - int(yesterday_data[row[1]][1])
            row[4] = int(row[4]) - int(yesterday_data[row[1]][2])

            # 누적 데이터 저장
            yesterday_data[row[1]][0] += row[2]
            yesterday_data[row[1]][1] += row[3]
            yesterday_data[row[1]][2] += row[4]

            csv_data.append(row)

    df = pd.DataFrame(csv_data)


    file_name = 'covid19_ko_' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.csv'
    df.to_csv(file_name, index=False, header=False, encoding='utf8')
    print('완료1')

# 매일 오후 11시 크롤링 수행
schedule.every().day.at("23:00").do(cc)
print('완료2')

while True:
    schedule.run_pending()
    time.sleep(1000)
