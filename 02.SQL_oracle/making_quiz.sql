-- 0528 making quiz by. 이진영, 이홍주, 장수정, 최한승

.header on
.mode column

CREATE TABLE mountains (
  name TEXT,
  height_meters INTEGER,
  first_ascent DATE,
  first_hiker TEXT
);

INSERT INTO mountains VALUES
  ('Mount Everest', 8848, '1953-05-29', 'Amy'),
  ('Kilimanjaro', 5895, '1889-10-06', 'James'),
  ('Denali', 6190, '1913-06-07', 'Poppy'),
  ('Chimborazo', 6263, '1880-01-04', 'Amy'),
  ('K2', 8611, '1954-07-31', 'John'),
  ('Piz Palü', 3900, '1835-08-12', 'Sandy'),
  ('Cho Oyu', 8188, '1954-10-19', 'Sandy');

.print 'average mountain height'
SELECT avg(height_meters) AS avg_height
FROM mountains;

.print
.print 'number of ascents per century'
SELECT
  strftime(
    '%Y',
    date(first_ascent)
  ) / 100 + 1 AS century,
  count(*) AS ascents
FROM mountains
GROUP BY century;


-- 1.'P'가 한 번 이상 들어가는 산을 출력하시오
select name
from mountains
where name like '%P%';

-- 2. 1950년대에 처음 등반된 산 이름과 등반 date 시간 순(오름차순)으로 출력
select name, first_ascent
from mountains
where first_ascent between '1950-01-01' and '1959-12-31'
order by first_ascent asc;

-- 3.해발고도가 낮은 산부터(오름차순) 정리하는데 이름도 같이 출력하시오.
select name, height_meters
from mountains
order by height_meters asc;

-- 4. 1950년대 첫 등반을 성공한 산들의 모든 정보를 높이 기준 내림차순으로 정렬하세요.
select *
from mountains
where first_ascent like '195%'
order by height_meters desc;

-- 5. 고도 5000 이상 등반한 사람 이름 중복 없이 이름 오름차순으로 출력
select distinct first_hiker
from mountains
where height_meters >= 5000
order by first_hiker asc;

