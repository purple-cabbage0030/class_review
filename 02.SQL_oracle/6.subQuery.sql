-- 6.subQuery.sql
-- select문 내에 포함된 또 다른 select문 작성 방법
-- 참고 : join 또는 subquery로 동일한 결과값 검색, 상황에 따라 어떤 문장으로 검색할지 달라짐.

-- 문법 : 비교 연산자(대소비교, 동등비교) 오른쪽에 () 안에 select문 작성 
--	   : create 및 insert 에도 사용 가능
--	   : tip - 개발시 다수의 test 위해서 원본이 아닌 복사본 table활용 권장 (수업시간에 적용)
--       >create table emp01 as select * from emp;
-- 실행순서 : sub query가 main 쿼리 이전에 실행

/*
테이블 구조 설계

여러 개의 테이블을 만들어서 join or subquery 필수
실행 속도 테스트해서 튜닝 후에 sql을 결정해야 함
*/


--1. SMITH라는 직원 부서명 검색
select dname
from emp, dept
where ename='SMITH' and emp.deptno=dept.deptno;

-- sub query 이용법
-- SMITH의 부서 번호 검색 후 부서 테이블에서 해당 번호와 일치되는 부서명 검색하는 로직
-- 바깥에 있는 게 main query, 괄호 안이 sub query
select dname
from dept
where deptno=(
	select deptno from emp where ename='SMITH' 
);


--2. SMITH와 동일한 직급(job)을 가진 사원들의 모든 정보 검색(SMITH 포함)
select *
from emp
where job=(
	select job from emp where ename='SMITH'
);

-- smith 제외
select *
from emp
where job=(
	select job from emp where ename='SMITH'
) and ename!='SMITH';

--3. SMITH와 급여가 동일하거나 더 많은(>=) 사원명과 급여 검색
-- SMITH 제외해서 검색하기
select ename, sal
from emp
where sal>=(
	select sal from emp where ename='SMITH'
) and ename!='SMITH';


--4. DALLAS에 근무하는 사원의 이름, 부서 번호 검색
select ename, deptno
from emp
where deptno=(
	select deptno from dept where loc='DALLAS'
);


--5. 평균 급여보다 더 많이 받는(>) 사원만 검색
select ename, sal
from emp
where sal>(
	select avg(sal) from emp
);


-- 1~5번까지는 sub query의 결과가 단일행/ 단일 검색 결과 row



-- 다중행 서브 쿼리(sub query의 결과값이 둘 이상)
-- 6.급여가 3000이상 사원이 소속된 부서에 속한  사원이름, 급여 검색
	--급여가 3000이상 사원의 부서 번호
	-- in

select ename, sal
from emp
where deptno in (
	select deptno
	from emp
	where sal>=3000
);


--7. in 연산자를 이용하여 부서별(group by)로 가장 급여를 많이 받는 사원의 정보(사번, 사원명, 급여, 부서번호) 검색
select empno, ename, sal, deptno
from emp
where sal in (
	select max(sal)
	from emp
	group by deptno
);

select empno, ename, sal, deptno
from emp
where (deptno, sal) in (
	select deptno, max(sal)
	from emp
	group by deptno
);
	
--8. 직급(job)이 MANAGER인 사람이 속한 부서의 부서 번호와 부서명(dname)과 지역검색(loc)
select deptno, dname, loc
from dept
where deptno in (
	select deptno 
	from emp 
	where job='MANAGER'
)
order by deptno asc;
