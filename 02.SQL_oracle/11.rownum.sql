--11.rownum.sql

-- *** rownum
-- oracle 자체적으로 제공하는 컬럼
-- table 당 무조건 자동 생성
-- 검색시 검색된 데이터 순서대로 rownum값 자동 반영(1부터 시작)

-- *** 인라인 뷰
	-- 검색시 빈번히 활용되는 스펙
	-- 다수의 글들이 있는 게시판에 필수로 사용(paging 처리)
	-- 서브쿼리의 일종으로 from절에 위치하여 테이블처럼 사용
	-- 원리 : sql문 내부에 view를 정의하고 이를 테이블처럼 사용 

select rownum, empno from emp;
select rownum, deptno from dept;


-- 코드만으로 rownum 탐색하기
-- 실행순서: from -> select -> where
-- 암기 사항: rownum은 검색 시에 검색된 결과에 자동 index를 부여, 1부터 활용해야 함.
-- 시작점이 1이 아닌 경우 논리적으로 1부터 시작을 안 했기 때문에 무효화함.
select rownum, deptno from dept where rownum<4;

select rownum, deptno
from (select rownum, deptno
	from dept
	where rownum<4);
-- 데이터가 조건에 맞게 검색됨
/* 
== inline view 방식 ==
인라인 구조: from절에 select문장으로 검색된 데이터가 반영되는 구조.
-- 검색된 데이터는 임시로 생성된 table, 즉 물리적으로 존재하지 않는 table로 간주.
-- 논리적인 table은 view!!

-- syntax 분석
select 검색 컬럼
from 존재하는 table 또는 검색된 데이터(임시 table)
*/

select rownum, deptno from dept where rownum>2;
-- no rows selected

-- 1. ? dept의 deptno를 내림차순(desc)으로 검색, rownum
select rownum, deptno
from dept
order by deptno desc;


-- 2. ? deptno의 값이 오름차순으로 정렬해서 30번 까지만 검색, rownum 포함해서 검색
select rownum, deptno
from dept
where rownum<4
order by deptno asc;


-- 3. ? deptno의 값이 오름차순으로 정렬해서 상위 3개의 데이터만 검색, rownum 포함해서 검색
select rownum, deptno
from dept
where rownum<4
order by deptno asc;

-- deptno 내림차순
select rownum, deptno
from dept
where rownum<4
order by deptno desc;

-- 4.  인라인 뷰를 사용하여 급여를 많이 받는 순서대로 3명만 이름과 급여 검색 
select rownum, ename, sal from emp order by sal desc;
-- from -> select (rownum) -> order by sal: rownum은 이미 검색 돼서 순서가 흐트러짐



select rownum, ename, sal
from (select rownum, ename, sal
	from emp
	order by sal desc)
where rownum<4;

-- 최종 서비스에선 from절 안의 inline view에서 rownum 삭제
select rownum, ename, sal
from (select ename, sal
	from emp
	order by sal desc)
where rownum<4;

/*
select ename, sal
from (select ename, sal
	from emp
	order by sal desc)
where rownum<4;
 
select ename, sal
from (select rownum, ename, sal
	from emp
	order by sal desc)
where rownum<4;
*/

-- emp의 deptno 값이 오름차순으로 정렬된 상태로 상위 3개 데이터 검색
select rownum, deptno
from (select deptno
	from emp
	order by deptno asc)
where rownum<4;
