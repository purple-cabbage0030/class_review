-- 1.select.sql
--: oracle db에서의 주석 표기
/*블록주석
존재하는 데이터를 검색하는 명령어 학습

1. 기본 syntax (called select절, from절)
select 검색하고자 하는 컬럼명
from table명;

실행 순서: from (테이블 존재 확인) -> select

*********************************************

2. 정렬 syntax
-- order by, asc(오름차순)/desc(내림차순)
select 검색하고자 하는 컬럼명
from table명
order by 정렬기준컬럼명 asc/desc;

실행 순서: from -> select -> order

********************************************

3. 조건절 syntax
- where 조건식
select절
from절
where절 ;

실행 순서: from -> where -> select

********************************************

4. 조건절 & 정렬 syntax
- where 조건식
select절
from절
where절
ordre by 절 ;

실행 순서: from -> where -> select -> 검색 결과를 최종 정렬하는 order by
*/

--1. sqlplus창 보기 화면 여백 조절 편집 명령어
	-- 단순 sqlplus tool만의 편집 명령어
	-- 영구 저장 안됨. sqlplus 실행시마다 해 줘야 함
set linesize 200
set pagesize 200
 

--2. 해당 계정의 모든 table 목록 검색
select * from tab;


--3. emp table의 모든 정보 검색
select * from emp;


--4. emp table의 구조 검색[묘사]
desc emp;
/* 
	NUMBER(4): 정수 4자리
	VARCHAR2(10): 철자 10개까지 허용하는 문자열
	NUMBER(7,2): 실수, 전체 자릿수 7자리 단 소수점 이하 2자리
*/


--5. emp table의 사번(empno)과 이름(ename)만 검색
select empno, ename from emp;

--6. emp table의 입사일(hiredate) 검색
select hiredate from emp;
	
--7. emp table의 검색시 칼럼명 empno를 사번이란 별칭으로 검색 
-- 검색 시에 컬럼 명에 별칭 부여 가능
select empno as 사번 from emp;

--8. emp table에서 부서번호(deptno) 검색시 중복 데이터 제거 후 검색 
select deptno from emp;

-- distinct: 중복 데이터를 제거하는 기능의 sql 키워드
select distinct deptno from emp;


--9. 데이터를 오름차순(asc)으로 검색하기(순서 정렬)

select distinct deptno 
from emp 
order by deptno asc;

-- ? 사번을 오름차순으로 정렬 해서 사번만 검색
select empno from emp order by empno asc;


-- 10.emp table 에서 deptno 내림차순(desc) 정렬 적용해서 ename과 deptno 검색하기
select ename, deptno from emp order by deptno desc;


--? empno와 deptno를 검색하되 단 deptno는 오름차순 검색
select empno, deptno from emp order by deptno asc;


-- 11. 입사일(date 타입의 hiredate) 검색, date 타입은 정렬가능 따라서 경력자(입사일이 오래된 직원)부터 검색(asc)
select hiredate from emp order by hiredate asc;



/* dummy table - dual이라는 table
잉여 테이블
임시 테이블로 가령 syntax 문법 오류 방지용으로 주로 사용
SQL> select * from dual;

DU
--
X

select sysdate from dual;

SYSDATE
--------
21/05/28

SQL> select 3+5 from dual;

       3+5
----------
         8

*/


-- *** 연산식 ***
--12. emp table의 모든 직원명(ename), 월급여(sal), 연봉(sal*12) 검색
-- 단 sal 컬럼값은 comm을 제외한 sal만으로 연봉 검색
select sal*12 from emp;
select sal, sal*12 from emp;

select ename as 사원명, sal as 월급여, sal*12 as 연봉 from emp;

-- 13. 모든 직원의 연봉 검색(sal *12 + comm) 검색
-- comm 존재 또는 미존재(0이 아님. null 값. 존재 자체가 없다는 의미)
-- 데이터가 null인 경우 연산 자체가 무효화. 모두가 null로 일괄 처리
-- 해결책: null 값을 0으로 치환해서 연산.
-- null 값을 다른 값으로 치환하는 함수: nvl(null보유컬럼, 변경할값) --중요 !!

select sal, comm, nvl(comm, 0) from emp;
select sal, comm, sal*12+nvl(comm, 0) as 연봉 from emp;





-- *** 조건식 ***
--14. comm이 null인 사원에 대한 검색(ename, comm)
select ename, comm from emp;

select ename, comm
from emp
where comm is null;

	
--15. comm이 null이 아닌(not) 사원에 대한 검색(ename, comm)
select ename, comm
from emp
where comm is not null;

--15번 결과치 오름차순 정렬
select ename, comm from emp where comm is not null order by comm asc;
-- 실행 순서에 따라, order by절이 가장 마지막에 와야 함.

--16. ename, 전체연봉... comm 포함 연봉 검색
select ename, sal*12+nvl(comm, 0) as 전체연봉 from emp;

--17. emp table에서 deptno 값이 20인(조건식 where, deptno=20인 동등비교) 직원 정보 모두(*) 출력하기  : = [sql 동등비교 연산자]
select * from emp where deptno=20;

--? 검색된 데이터의 sal 값이 내림차순(desc)으로 정렬 검색 
select empno, sal from emp order by sal desc;

--18. emp table에서 ename이 smith(SMITH. 대소문자 구분 중요... 함수로 옵션 변경 가능)에 해당하는 deptno값 검색
-- sql 상에서 문자열 데이터 표기 = ' ' (단일따옴표)

select ename from emp;

select ename, deptno from emp where ename='SMITH';
select ename, deptno from emp where ename='smith';

--19. sal가 900이상(>=)인 직원들의 이름(ename), sal 검색
select ename, sal from emp where sal>=900;

--20. deptno가 10이고(and) job이 메니저인 사원이름 검색
-- 조건식이 하나 이상인 경우
-- 모든 조건이 true여야 하는지 하나만 true여도 되는지 파악
select ename, deptno, job from emp; 
select ename from emp where deptno=10 and job='MANAGER';

-- 21. ?deptno가 10이거나(or) job이 메니저(MANAGER)인 사원이름(ename) 검색
select ename from emp where deptno=10 or job='MANAGER';

-- 22. deptno가 10이 아닌 모든 사원명(ename) 검색
-- 부정연산자 != / <> / not 3가지.
select ename from emp where deptno!=10;
select ename from emp where deptno<>10;
select ename from emp where not deptno=10;

-- application에서 sql 문장 사용 시 권장 형식 (대문자 포맷)
SELECT ename, deptno
FROM emp
WHERE deptno!=10;

--23. sal이 2000 이하(sal<=2000)이거나(or) 3000이상인(sal>=3000) 사원명(ename) 검색
select ename from emp where sal<=2000 or sal>=3000;

--24. comm이 300 or 500 or 1400인 사원명, comm 검색
select ename, comm from emp where comm = 300 or comm = 500 or comm = 1400;

select ename, comm from emp where comm in (300, 500, 1400);
	

--25. ?comm이 300 or 500 or 1400이 아닌(not) 사원명, comm 검색
select ename, comm from emp where not comm in (300, 500, 1400);
select ename, comm from emp where comm not in (300, 500, 1400);

-- 26. 81년도에 입사(hiredate)한 사원 이름(ename) 검색
-- DATE type도 비교 연산이 가능한지?
select ename, hiredate from emp;

-- 동등 비교 가능 확인
select ename from emp where hiredate = '81/11/17';

-- 81년도 표현? 
	-- 범위 1981/01/01 ~ 1981/12/31
	-- 81이라는 표현과 일치되는 방법? date에서 yy만 도출해서 비교하는 방법?

-- 범위로 비교하는 연산식: between A and B
select ename, hiredate from emp where hiredate between '81/01/01' and '81/12/31';

-- 27. ename이 M으로 시작되는 모든 사원번호(empno), 이름(ename) 검색  
-- 연산자 like : 한 철자 _ , 철자 개수 무관하게 검색할 경우 %
select ename, empno
from emp
where ename like 'M%';

-- 28. ename이 M으로 시작되는 전체 자리수가 두 철자의 사원번호, 이름 검색
select ename, empno
from emp
where ename like 'M_';

-- 29. 두번째 음절의 단어가 M인 모든 사원명 검색 
select empno, ename from emp where ename like '_M%';

-- 30. 단어가 M을 포함한 모든 사원명 검색 
select empno, ename from emp where ename like '%M%';


