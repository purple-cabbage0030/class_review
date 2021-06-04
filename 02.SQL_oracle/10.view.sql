--10.view.sql
/*
* view 사용을 위한 필수 선행 설정
	1단계 : admin 계정으로 접속
	2단계 : view 생성해도 되는 사용자 계정에게 생성 권한 부여
		> connect system/manager
		> grant create view to SCOTT;
		> conn SCOTT/TIGER

1. view 에 대한 학습
	- 물리적으로는 미 존재, 단 논리적으로 존재
	- 물리적(create table)
	- 논리적(존재하는 table들에 종속적인 가상 table)

2. 개념
	- 보안을 고려해야 하는 table의 특정 컬럼값 은닉하고자 할 때
	또는 여러개의 table의 조인된 데이터를 다수 활용을 해야 할 경우
	특정 컬럼 은닉, 다수 table 조인된 결과의 새로운 테이블 자체를 
	가상으로 db내에 생성시킬수 있는 기법 

	예시 - RDBMS는 필요하기 때문에 해결책으로 view를 제공
	1. emp의 comm 컬럼은 영업부 사원에게만 몰래 있는 구조(은닉구조)
		타 직무들은 존재 자체를 모르는 경우
	
	2. 외부 개발자에게 부득이하게 정보 오픈해야 할 경우
		특정 컬럼은 은닉해서 동일한 구조의 table 형식을 제공

3. 문법
	- create와 drop : create view/drop view
	- crud는 table과 동일

4. view 기반으로 crud 반영시 실제 원본 table에도 반영이 된다.

5. 종류
	5-1. 단일 view : 별도의 조인 없이 하나의 table로 부터 파생된 view
	5-2. 복합 view : 다수의 table에 조인 작업의 결과값을 보유하는 view
	5-3. 인라인 view : sql의 from 절에 view 문장  

6. 실습 table
	-dept01 table생성 -> dept01_v view 를 생성 -> crud -> view select/dept01 select 
*/
--1. test table생성

create table dept01 as select * from dept;


--2. dept01 table상의 view를 생성
-- SCOTT 계정으로 view 생성 권한 받은 직후에만 가능 (grant create view to SCOTT;)

create view dept01_v as select * from dept01;
desc dept01_v;
select * from dept01_v;

--3. ? emp table에서 ename, empno, sal컬럼 사용한 emp01_v 라는 view 생성

create view emp01_v as select ename, empno, sal
from emp;


--4. dept01_v에 crud : dep01_v와 dept01 table 변화 동시 검색
select * from dept01_v;
insert into dept01_v values(50, '교육부', '홍대');
select * from dept01_v;
select * from dept01;
-- view에 insert하면 원본에도 들어감.

update dept01_v set loc='마포' where deptno=50;
select * from dept01_v;
select * from dept01;
-- view에 crud 작업 하면 원본에 다 적용됨 ~

delete from dept01_v where deptno=50;
select * from dept01_v;
select * from dept01; 


--5. 모든 end user가 빈번히 사용하는 sql문장으로 "해당 직원의 모든 정보 검색(empno, ename, deptno, loc)"하기
/* 개발 방법
- 두개의 join 필수 (emp와 dept테이블 복제하여 실습)
방법1 : 필요시 늘 join하는 sql문장 실행
방법2 : 이미 조인된 구조의 view를 생성 해 놓고, 필요시 view만 select */
drop table emp01;
drop table dept01;

create table emp01 as select empno, ename, deptno, sal from emp;
create table dept01 as select * from dept;

-- 빈번히 사용되는 join인 경우 별도의 view 생성해서 검색에 사용하기도 함
create view emp01_dept01_v
as
select empno, ename, d.deptno, loc
from emp01 e, dept01 d
where e.deptno(+)=d.deptno;

select * from emp01_dept01_v;


--6. 논리적인 가상의 table이 어떤 구조로 되어 있는지 확인 가능한 oracle  자체 table
	-- view는 text 기반으로 명령어가 저장 
	-- oracle 자체적인 사전 table
select * from user_views;
desc user_views;


--7. view 삭제 후 사전 table 재확인
-- view 삭제 시 사전 table에서도 자동 삭제됨
drop view emp01_dept01_v;
select * from user_views;


/*
1. java 개발 및 실행 단계
	개발 -> 컴파일(문법 검증) -> 실행 
	컴파일언어
		Test.java -> >javac Test.java 명령어로 컴파일 ->  >java Test
​
		Test.java 개발 : 개발자가 구현 및 이해 가능한 구조
		-> 변환(컴파일) Test.class : 기계가 인식 즉 실행 가능한 구조 변경
		-> 실행(running) Test.class만으로 실행 
		: 서버에 서비스를 위해서 배포시에는 Test.class 파일만 셋팅해서 서비스 
​
​
2. python 
	개발 -> 실행 
	인터프리터 언어 
		Test.py 개발 : 개발자가 구현 및 이해 가능한 구조
		>python Test.py 실행
​
3. sql
	개발 -> 실행 
		oracle 엔진
			sql문장을 받음 -> 문법 체킹(컴파일) -> 실행
		view는 이미 문법 검증이 완료된 실행만 하면 되는 구조
		실시간 sql문장 새로 유입되서 컴파일 후 실행 하는 과정과 달리 이미 컴파일 되어 있는 상태로 실행만 
		하기 때문에 performance 관점에선 good
*/

-- inline view: inline에서 검색하지 않은 컬럼은 절대 main에서 쓸 수 없다.
--8. emp, dept table에서 검색(최종적으로). 각 부서별 지역명과 근무하는 사원?
select loc, ename
from (select loc, ename
	from emp e, dept d
	where e.deptno=d.deptno);

-- inline 미사용 시에도 검색 결과는 동일하다.
select loc, ename
from emp e, dept d
where e.deptno=d.deptno;