--14.PLSqlSyntaxBasic.sql
/* 
개발 언어 특징
	- library + 사용자 정의 기능인 함수 + 클래스(변수, 메소드) ...

DB도 사용자 정의 함수 개발이 가능
	- 오라클의 경우 PLSQL이라고 함. Procedure Language SQL

* 프로시저 & 함수
	- 재사용을 위한 기능 구현
	- 기본 문법은 흡사
1. 프로시저
	- 호출 방법이 함수와 차이가 있음
2. 함수
	- oracle 함수 호출하듯 사용자 정의 함수 호출 가능

------
1. oracle db만의 프로그래밍 개발 방법
	1. 이름 없이 단순 개발
	2. 프로시저라는 타이틀로 개발 - 이름 부여(재사용)
	3. 함수라는 타이틀로 개발 - 이름 부여(재사용)

2. 장점
	- 단 한번의 실행 만으로 내장 함수처럼 만들어서 필요시 호출해서 실행 가능
	- 프로시저와 함수로 구현시 db내부에 pcode로 변환

3. test를 위한 필수 셋팅 
	- set serveroutput on 
	
4. 필수 암기 
	1. 할당(대입) 연산자  ':='
		- 파이썬에서 오른쪽에서 왼쪽으로 대입하는 연산자 표기법은 '='
	2. 선언, 시작, 끝 기본 syntax
		declare 
			변수 선언(반드시 타입과 함께?)
		begin
			로직 처리/로직 구현
		end;
		/
*/

--1. 실행 결과 확인을 위한 필수 설정 명령어
-- 생략할 경우 프로시저 실행 결과 확인 불가
set serveroutput on

--2. 연산을 통한 간단한 프로시저 문법 습득
declare
	no integer;
begin
	no := 10;    -- 10값을 no변수에 할당(대입, 초기화)
	dbms_output.put_line('결과 ' || no);   -- plsql 출력 및 new line반영 함수. ||==> 앞 뒤 데이터 결합하여 출력하도록 하는 연산자

	no := 10 / 5;
	dbms_output.put_line('결과 ' || no);
end;
/

-- 이름 값을 출력할 수 있는 프로시저를 구현
-- 전제 조건: name 변수 선언해서 활용(varchar2)
declare
	name varchar2(100);
begin
	name := '이름';
	dbms_output.put_line('이름은? ' || name);
end;
/

declare
	no1 number := 10;
begin
	dbms_output.put_line('결과 ' || no1);
end;
/


--3. 연산을 통한 간단한 문법 습득 + 예외 처리 문장
-- 혹여 문제가 생겨도 프로그램 종료가 아니라 유연하게 실행 유지

-- 예외처리시 실행 유지
-- 예외 미처리시 실행 강제 종료

-- 1단계) 문제 발생해서 중지 확인하는 test 코드
declare
	no integer;
begin
	no := 10 / 0;  -- 오류
	dbms_output.put_line('결과 ' || no);
	-- 중요 로직들이 구현되어 있는 경우
end;
/

-- 2단계) 프로그램 중지를 방지하기 위한 해결책: exception, 예외처리
declare
	no integer := 10;
begin
	no := 10 / 0;  -- 오류
	dbms_output.put_line('결과 ' || no);

	exception
		when others then
			dbms_output.put_line('예외 발생');

	dbms_output.put_line('결과 ' || no);
end;
/

--4. 중첩 block & 변수 선언 위치에 따른 구분
--5. step02 - 전역, 로컬 변수 선언 및 활용 범위 확인 
-- step01 - 전역(global), 로컬 변수 선언 및 활용
declare
	v_global varchar2(10):='g';     --글로벌 변수 선언
begin
	dbms_output.put_line(v_global); --글로벌 변수 활용
	declare
		v_local varchar2(10):='l';  --로컬 변수 선언
	begin
		dbms_output.put_line(v_global); --글로벌 변수 활용
		dbms_output.put_line(v_local); --로컬 변수 활용

	end;
	
	dbms_output.put_line(v_global); --글로벌 변수 활용
	dbms_output.put_line(v_local); --로컬 변수 활용

end;
/


--6. emp01 table의 컬럼 타입을 그대로 사용하고 싶다면?
	-- %type : db의 특정 컬럼의 타입 의미
drop table emp01;
create table emp01 as select * from emp;

-- 사번으로 이름 검색해서 출력하는 프로시저 개발
-- select ename from emp01 where empno=7369;
declare
	v_empno emp01.empno%type;
	v_ename emp01.ename%type;
begin
	select ename, empno
		into v_ename, v_empno
	from emp01
	where empno=7369;

	dbms_output.put_line(v_ename || ' ' || v_empno);
end;
/
-- 실행 순서: from - where - select - into

--7. 이미 존재하는 table의 record의 모든 컬럼 타입 활용 키워드 : %rowtype
/* 7369 사번으로 해당 사원의 모든 정보를 검색해서 사번, 이름만 착출해서 출력 
포함된 내용 (변수 등) 활용 시에는 .(dot 연산식 사용)*/
declare
	v_rows emp01%rowtype;
begin
	select *
		into v_rows
	from emp
	where empno=7369;

	dbms_output.put_line(v_rows.ename);
end;
/


--8. ???
-- emp05라는 table을 데이터 없이 emp table로 부터 생성하기
-- %rowtype을 사용하셔서 emp의 사번이 7369인 사원 정보 검색해서 
-- emp05 table에 insert
-- 힌트 : begin 부분엔 다수의 sql문장 작성 가능, into 절
drop table emp05;
create table emp05 as select * from emp where 1=0;

declare
	v_row emp05%rowtype;
begin
	select *
		into v_row
	from emp
	where empno=7369;

	insert into emp05 values v_row;
end;
/

select * from emp05;


--9. 조건식
/*  1. 단일 조건식
	if(조건) then
		
	end if;
	
   2. 다중 조건
	if(조건1) then
		조건1이 true인 경우 실행되는 블록 
	elsif(조건2) then
		조건2가 true인 경우 실행되는 블록
	end if; 
*/

-- allen 사원의 연봉 합을 계산하는 procedure 개발[comm이 null인 직원들은 0으로 치환]
declare
	v_emp emp%rowtype;
	total_sal number(7, 2);
begin
	select empno, ename, sal, comm
		into v_emp.empno, v_emp.ename, v_emp.sal, v_emp.comm
	from emp
	where ename='ALLEN';

	if v_emp.comm is null then
		v_emp.comm := 0;
	end if;

	total_sal := v_emp.sal*12+v_emp.comm;
	dbms_output.put_line(total_sal);
end;
/



select empno, ename, sal, comm 
from emp 
where ename='SMITH';


-- 존재하는 테이블의 특정 컬럼 타입 하나 의미하는 표현식: %type
-- 모든 컬럼: %rowtype



-- 10.??? 실행시 가변적인 데이터 적용해 보기
-- 실행시마다 가변적인 데이터(동적 데이터) 반영하는 문법 : 변수 선언시 "&변수명"

-- emp table의 deptno=10 : ACCOUNT 출력, 
-- deptno=20 이라면 RESEARCH 출력
-- test data는 emp table의 각 사원의 사번(empno)

-- 차후에는 프로시저에 이름 적용
-- 이름이 있다는 것은 필요 시 호출해 재사용성을 고려한 구조
-- 실행마다 새로운 데이터 입력받는 동적 변수 할당 문법 &v (v말고 다른 변수명 가능)
declare
	ck_empno emp.empno%type := &v;
	v_empno emp.empno%type;
	v_deptno emp.deptno%type;
	v_dname varchar2(10);
begin
	select empno, deptno
		into v_empno, v_deptno
	from emp
	where empno=ck_empno;
	if (v_deptno=10) then	
		dbms_output.put_line('ACCOUNT');
	elsif (v_deptno=20) then	
		dbms_output.put_line('RESEARCH');
	else
		dbms_output.put_line('None');
	end if;
end;
/

--11. 반복문
-- 조건에 부합되는 상황에서만 반복
-- 증가치와 조건식이 필요
-- 조건식은 어떤 영역에 반영해서 반복 중지할 것인지
/* 
1. 기본
	loop 
		ps/sql 문장들 + 조건에 사용될 업데이트
		exit 조건;
	end loop;

2. while 기본문법
	 while 조건식 loop
		plsql 문장;
	 end loop;

3. for 기본 문법
	for 변수 in [reverse] start ..end loop
		plsql문장
	end loop;

	* 적재시킬 변수는 반복문 바깥에서 선언해야 함
*/
-- loop 
declare
	num number(2) := 0;
begin
	loop
		dbms_output.put_line(num);
		num := num+1;
		exit when num > 5;   -- 조건식
	end loop;
end;
/


declare
	num number(2) := 1;
begin
	loop
		dbms_output.put_line(num);
		num := num+1;
		exit when num >= 5;
	end loop;
end;
/



-- while
declare
	num number(2) := 0;
begin
	while num < 5 loop
	dbms_output.put_line(num);
	num := num + 1;
	end loop;
end;
/


-- for (많이 씀)
-- 오름차순
-- declare 변수 선언 꼭 안 해도 됨
declare
begin
	for num in 0..4 loop
		dbms_output.put_line(num);
	end loop;
end;
/


-- 내림차순
declare
begin
	for num in reverse 0..4 loop
		dbms_output.put_line(num);
	end loop;
end;
/


--12.? emp table 직원들의 사번을 입력받아서(동적데이터) 해당하는 
-- 사원의 이름 철자 수 만큼 * 표 찍기 -- 반복문, 적재/누적: 결합연산자 || 이용
-- length()

declare
	v_ename emp.ename%type;
	v_empno emp.empno%type := &no;
	v_num number(3);
	v_star varchar2(10);
begin
	select empno, ename
		into v_empno, v_ename
	from emp
	where empno=v_empno;
	if empno = v_empno then
	for in length(v_ename) loop
	dbms_output.put_line(v_star);
	end if;
end;
/

declare
	v_ename emp.ename%type;
	v_empno emp.empno%type := &no;
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

	dbms_output.put_line(v_ename || '사원의 이름 -' || v_star);
end;
/
