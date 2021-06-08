--16.PLSqlFunction.sql
/*
함수 개발의 필요성
- 잘 만들어서 무수히 재사용 하겠다는 의미
- 개발 시간 단축, 비용 절감, 활용 쉽게 하는 기술

1. 저장 함수(function)
	- 오라클 사용자 정의 함수 
	- 오라클 함수 종류
		- 지원함수(count(??){ }, avg()...) + 사용자 정의 함수
2. 주의사항
	- 절대 기존 함수명들과 중복 불가
3. 프로시저와 다른 문법
	- plsql에서의 함수는 반드시 리턴값 있음
	- 리턴 타입 선언 + 리턴 값

4. oracle db 내에 구현하는 사용자 정의 함수 문법
	4-1. 함수 생성만
		create function 함수명()
		return 반환하는 타입
		is
			함수 내에서 사용될 변수 선언
		begin
			처리 로직
		end;
		/
	
	4-2. 함수 생성 또는 치환(기존 함수 갱신)
		create or replace function 함수명()
		return 반환하는 타입
		is
			함수 내에서 사용될 변수 선언
		begin
			처리 로직
		end;
		/
*/

--1. emp table의 사번으로 사원 이름
-- (리턴 값, 이름의 타입이 리턴타입) 검색 로직 함수 
create function user_fun(no number) -- 함수명, 파라미터 변수 및 타입 선언
return varchar2				 -- 리턴 타입 명시
is
	v_ename emp.ename%type;  --새로운 변수 선언
begin
	select ename	
		into v_ename
	from emp where empno=no;

	return v_ename;			-- 리턴 데이터
end;
/
select user_fun(7369) from dual;


-- 14단계 마지막 문제 함수로 구현
-- 함수명 = mystar

create or replace function mystar(no number)
return varchar2
is
	v_ename emp.ename%type;
	v_num number(3);
	v_star varchar2(10) := '';
begin
	select ename, length(ename)
		into v_ename, v_num
	from emp
	where empno=no;
	
	for i in 1..v_num loop
		v_star := v_star || '*';
	end loop;

	return v_star;
end;
/

select mystar(7369) from dual;

-- 함수 개선 refactoring
create or replace function mystar(v_empno emp.empno%type)
return varchar2
is
	v_ename emp.ename%type;
	v_num number(3);
	v_star varchar2(10) := '';
begin
	select ename, length(ename)
		into v_ename, v_num
	from emp
	where empno=v_empno;
	
	for i in 1..v_num loop
		v_star := v_star || '*';
	end loop;

	return v_star;
end;
/

select mystar(7369) from dual;


--2.? %type 사용해서 사원명으로 해당 사원의 직무(job) 반환하는 함수 
-- 함수명 : emp_job
-- %type 사용 적극 권장 !! 에러 날 확률 낮추기
create or replace function emp_job(v_ename emp.ename%type)
return emp.job%type
is
	v_job emp.job%type;
begin
	select job
		into v_job
	from emp
	where ename=v_ename;

	return v_job;
end;
/


select emp_job('SMITH') from dual;



--3.? 특별 보너스를 지급하기 위한 저장 함수
	-- 급여를 200% 인상해서 지급(sal*2)
-- 함수명 : cal_bonus
-- test sql문장
select empno, job, sal, cal_bonus(7369) from emp where empno=7369;


create or replace function cal_bonus(v_empno emp.empno%type)
return number
is
	v_sal emp.sal%type;
begin
	select sal
		into v_sal
	from emp
	where empno=v_empno;

	return v_sal*2;
end;
/


-- 4.? 부서 번호를 입력 받아 최고 급여액(max(sal))을 반환하는 함수
-- 사용자 정의 함수 구현시 oracle 자체 함수도 호출
-- 함수명 : s_max_sal

create or replace function s_max_sal(v_deptno emp.deptno%type)
return number
is
	max_sal emp.sal%type;
begin
	select max(sal)
		into max_sal
	from emp
	where deptno=v_deptno;

	return max_sal;
end;
/

select s_max_sal(10) from dual;
-- test를 듀얼에서 해야 하는... emp에서 검색하는 것은 논리적으로 부적합

--5. ? 부서 번호를 입력 받아 부서별 평균 급여를 구해주는 함수
-- 함수명 : avg_sal
-- 함수 내부에서 avg() 호출 가능
create or replace function avg_sal(v_deptno emp.deptno%type)
return number
is
	a_sal emp.sal%type;
begin
	select avg(sal)
		into a_sal
	from emp
	where deptno=v_deptno;

	return a_sal;
end;
/


create or replace function avg_sal(v_deptno emp.deptno%type)
return number
is
	a_sal emp.sal%type;
begin
	select round(avg(sal), 2)
		into a_sal
	from emp
	where deptno=v_deptno;

	return a_sal;
end;
/

select avg_sal(10) from dual;
-- select avg(sal) from emp where deptno=10;과 결과값이 다른 이유? 자동 반올림되는 이유?


-- 논리적으로 부적합
select distinct deptno, avg_sal(deptno) from emp;



--6. 존재하는 함수 삭제 명령어
drop function avg_sal;



-- 함수 내용 검색: 사전/딕셔너리 테이블 검색
desc user_source;
select text from user_source where type='FUNCTION';


--8. procedure 또는 function에 문제 발생시 show error로 메세지 출력하기
show error

