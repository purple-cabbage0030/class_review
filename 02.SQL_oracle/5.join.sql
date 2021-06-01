-- 5.join.sql

/*
1. 조인이란?
	다수의 table간에  공통된 데이터를 기준으로 검색하는 명령어
	다수의 table이란?
		동일한 table을 논리적으로 다수의 table로 간주
			- self join
		물리적으로 다른 table간의 조인

2. 사용 table 
	1. emp & dept 
	  : deptno 컬럼을 기준으로 연관되어 있음

	 2. emp & salgrade(급여 등급 정보)
	  : sal 컬럼을 기준으로 연관되어 있음

  
3. table에 별칭 사용 
	검색시 다중 table의 컬럼명이 다를 경우 table별칭 사용 불필요, 
	서로 다른 table간의 컬럼명이 중복된 경우,
	컬럼 구분을 위해 오라클 엔진에게 정확한 table 소속명을 알려줘야 함
	- table명 또는 table별칭
	- 주의사항 : 컬럼별칭 as[옵션], table별칭에는 as 키워드 사용 불가


4. 조인 종류 
	1. 동등 조인
		 = 동등비교 연산자 사용
		 : 사용 빈도 가장 높음
		 : 테이블에서 같은 조건이 존재할 경우의 값 검색 

	2. not-equi 조인
		: 100% 일치하지 않고 특정 범위내의 데이터 조인시에 사용
		: between ~ and(비교 연산자)

	3. self 조인 
		: 동일 테이블 내에서 진행되는 조인
		: 동일 테이블 내에서 상이한 칼럼 참조
			emp의 empno[사번]과 mgr[사번] 관계

	4. outer 조인 
		: 두개 이상의 테이블이 조인될때 특정 데이터가 모든 테이블에 존재하지 않고 컬럼은 존재하나 null값을 보유한 경우
		  검색되지 않는 문제를 해결하기 위해 사용되는 조인
		  null 값이기 때문에 배제된 행을 결과에 포함 할 수 있드며 (+) 기호를 조인 조건에서 정보가 부족한 컬럼쪽에 적용
		
		: oracle DB의 sql인 경우 데이터가 null 쪽 table 에 + 기호 표기 */

-- 1. dept table의 구조 검색
desc dept;
-- dept, emp, salgrade table의 모든 데이터 검색
select * from dept;
select * from emp;
select * from salgrade;


 



--*** 1. 동등 조인 ***
-- = 동등 비교
-- 2. SMITH 의 이름(ename), 사번(empno), 근무지역(부서위치)(loc) 정보를 검색
select ename, empno, loc
from emp, dept
where ename='SMITH';
-- 문법은 맞는데 논리가 틀렸다

-- ORA-00918: column ambiguously defined
-- deptno는 두 개의 table에 존재하기 때문에 어떤 table의 컬럼을 검색하는지 불명확한 코드
-- select ename, empno, loc, deptno
-- from emp, dept
-- where ename='SMITH';

select ename, empno, loc, emp.deptno
from emp, dept
where ename='SMITH';

select ename, empno, loc
from emp, dept
where ename='SMITH' and emp.deptno=dept.deptno;

-- 3. deptno가 동일한 모든 데이터(*) 검색
-- emp & dept 
select *
from emp, dept
where emp.deptno=dept.deptno;


-- 4. 2+3 번 항목 결합해서 SMITH에 대한 모든 정보(ename, empno, sal, comm, deptno, loc) 검색하기
select ename, empno, loc
from emp, dept
where ename='SMITH' and emp.deptno=dept.deptno;


-- 5.  SMITH에 대한 이름(ename)과 부서번호(deptno), 부서명(dept의 dname) 검색하기
select ename, emp.deptno, dname
from emp, dept
where ename='SMITH' and emp.deptno=dept.deptno;

-- 테이블명 별칭 부여할 때 as 안 씀
select ename, empno, loc
from emp e, dept
where ename='SMITH' and e.deptno=dept.deptno;

-- 6. 조인을 사용해서 뉴욕에 근무하는 사원의 이름과 급여를 검색 
-- loc='NEW YORK', ename, sal
select ename, sal
from emp, dept
where loc='NEW YORK' and emp.deptno=dept.deptno;
-- 어떤 게 먼저 와야 효율적인 코드인지 생각해보기

-- 7. 조인 사용해서 ACCOUNTING 부서(dname)에 소속된 사원의 이름과 입사일 검색
select ename, hiredate
from emp, dept
where dname='ACCOUNTING' and emp.deptno=dept.deptno;



-- 8. 직급이 MANAGER인 사원의 이름, 부서명 검색
select ename, dname
from emp, dept
where job='MANAGER' and emp.deptno=dept.deptno;


-- *** 2. not-equi 조인 ***

-- salgrade table(급여 등급 관련 table)
-- 9. 사원의 급여가 몇 등급인지 검색
-- between ~ and : 포함 
select ename, sal, grade
from emp, salgrade
where sal between losal and hisal;


-- 10. 사원(emp) 테이블의 부서 번호(deptno)로 부서 테이블을 참조하여
-- 사원명, 부서번호, 부서의 이름(dname) 검색
-- 동등조인 문제
select ename, emp.deptno, dname
from emp, dept
where emp.deptno=dept.deptno;

-- 81년 4월 1일 이후에 입사한 사원들이 가장 많은 부서의 부서명
-- dname의 개수를 카운트해서 max 최대값

-- 생각 중...
select dname, count(*)
from emp, dept
where hiredate >= '81/04/01' and emp.deptno=dept.deptno
group by dname;

select max(dname)
from emp, dept
where hiredate >= '81/04/01' and emp.deptno=dept.deptno;

select min(dname)
from emp, dept
where hiredate >= '81/04/01' and emp.deptno=dept.deptno;
-- 아스키코드





-- *** 3. self 조인: 하나의 테이블에서 연관된 컬럼들로 다수의 테이블인 듯 작업하는 것 ***
-- 11. SMITH 직원(사원)의 매니저(smith의 상사) 이름 검색
-- 사원 테이블의 별칭 = e, 매니저 테이블의 별칭 = m (마치 테이블이 두 개인 듯 가정)
select m.ename
from emp e, emp m
where e.ename='SMITH' and e.mgr=m.empno;



-- 12. 메니저 이름이 KING(m ename='KING')인 사원들의 이름(e ename)과 직무(e job) 검색
-- 사원 테이블의 별칭 = e, 매니저 테이블의 별칭 = m
select e.ename, e.job, m.ename
from emp e, emp m
where m.ename='KING' and e.mgr=m.empno;

-- 13. SMITH와 동일한 근무지에서 근무하는 사원의 이름 검색

-- SMTIH라는 이름까지 검색되는 이슈 발생
select l.ename
from emp e, emp l
where e.ename='SMITH' and e.deptno=l.deptno;

-- SMITH를 검색에서 제외
select l.ename
from emp e, emp l
where e.ename='SMITH' 
	and e.deptno=l.deptno
	and l.ename!='SMITH';

select l.ename
from emp e, emp l
where e.ename='SMITH' 
	and e.deptno=l.deptno
	and not l.ename='SMITH';

--*** 4. outer join : 중요 ~~***
/* RDBMS에 종속적이지 않은 표준 SQL 문장 학습할 필요 있음 (ANSI sql)
cf) 
	https://www.w3schools.com/sql/sql_join.asp
	https://velog.io/@gillog/ANSI-SQL%EC%9D%B4%EB%9E%80
*/




-- dept의 deptno에 40번 부서 존재, emp에는 40번 부서에 소속된 직원 없음
-- emp의 'KING'의 mgr은 존재하지 않음(null)


-- 14. 모든 사원명, 메니저 명 검색, 단 메니저가 없는 사원도 검색되어야 함
select e.ename 사원명, m.ename 매니저명
from emp e, emp m
where e.mgr=m.empno;
-- 얘는 'KING'이 검색되지 않음


-- + 기호를 적용한 쪽이 null, 즉 데이터가 없는 쪽 ==> outer join
-- 데이터 표현이 부족한 쪽에 + 기호를 준다.
-- king 검색됨.
select e.ename 사원명, m.ename 매니저명
from emp e, emp m
where e.mgr=m.empno(+);

/* 
사원명               매니저명
-------------------- --------------------
FORD                 JONES
JAMES                BLAKE
TURNER               BLAKE
MARTIN               BLAKE
WARD                 BLAKE
ALLEN                BLAKE
MILLER               CLARK
CLARK                KING
BLAKE                KING
JONES                KING
SMITH                FORD
KING
*/

/*
논리적인 오류 있는 코드
select e.ename 사원명, m.ename 매니저명
from emp e, emp m
where e.mgr(+)=m.empno;
*/


-- 15. 모든 직원명(ename), 부서번호(deptno), 부서명(dname) 검색
-- 부서 테이블의 40번 부서와 조인할 사원 테이블의 부서 번호가 없지만,
-- outer join이용해서 40번 부서의 부서 이름도 검색하기 
select ename, d.deptno, dname
from emp e, dept d
where e.deptno(+)=d.deptno;

-- *** hr/hr 계정에서 test 
--16. 직원의 이름(first_name)과 직책(job_title)을 출력(검색)
-- 단, 사용되지 않는 직책이 있다면 그 직책의 정보도 검색에 포함

	-- 검색 정보 이름(2개)들과 job_title(직책) 

	-- 문제 풀이를 위한 table의 컬럼값들 확인해 보기

select first_name, last_name, job_title
from employees e, jobs j
where e.job_id(+)=j.job_id;



-- outer join 문제
--17. 직원들의 이름(first_name), 입사일(hire_date in employees), 부서명(department_name in departments) 검색하기
select first_name, hire_date, department_name
from employees e, departments d
where e.department_id=d.department_id;



-- 단, 부서가 없는 직원이 있다면 그 직원 정보도 검색에 포함시키기
-- 경우의 수1) 사원이 소속된 부서가 없을 경우
select first_name, hire_date, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id(+);



-- 경우의 수2) 부서에 소속된 사원이 없을 경우
select * from departments;

select distinct department_id from employees;

select first_name, hire_date, e.department_id, department_name
from employees e, departments d
where e.department_id(+)=d.department_id;


-- 문제만들기
-- 모든 직원의 이름과 부서 이름과 근무 도시를 검색하세요.

select first_name, department_name, city
from employees e, departments d, locations l
where e.department_id=d.department_id(+) and d.location_id=l.location_id(+);

