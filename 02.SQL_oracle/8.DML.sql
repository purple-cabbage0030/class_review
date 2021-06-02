--8.DML.sql
/* 
- DML : Data Mainpulation Language
            데이터 조작 언어
	   (select/insert/update/delete 모두 다 DML)
	   - 이미 존재하는 table에 데이터 저장, 수정, 삭제, 검색 
- transaction 관점에서의 차이점 (ex. 은행 출금)
	DML과 DDL은 다름
	DML은 commit과 rollback이 유효한 명령어(특정 시점(커밋된 시점)으로의 데이터 복원이 가능)
	DDL(create/drop/alter)은 commit과 rollback이 무효한 명령어

1. insert sql문법
	1-1. 모든 칼럼에 데이터 저장 시 
		- table 구조상의 컬럼 순서에 맞게 모든 데이터 저장시 사용하는 문법
		- 컬럼명 명시 생략 
		insert into table명 values(컬럼 순서에 맞는 데이터값, ... , ...)

		> insert into people values('가나다', 10);

	1-2.  특정 칼럼에만 데이터 저장시,
		명확하게 칼럼명 기술해야 할 경우 
		insert into table명 (칼럼명1, ...) values(칼럼과매핑될데이터1...)

		> insert into people (age) values(10);

	1-3. 하나의 sql문장으로 다수의 table에 데이터 입력 방법
		insert all 
			into table명 [(칼럼명,...)] values(데이터,,,)		
		select 검색칼럼 from....;
		존재하는 테이블로부터 검색된 데이터를 입력

		> insert all
			into people values('바나나', 12)
			into people values('사과', 3)
		select * from dual;

2. update 
	2-1. 모든 table(다수의 row)의 데이터 한번에 수정
		- where조건문 없는 문장
		- update table명 set 칼럼명=수정데이타;

	2-2. 특정 row값만 수정하는 방법
		- where조건문으로 처리하는 문장
		- update table명 set 칼럼명=수정데이타 where 조건sql;

3. delete
	3-1. table의 모든 데이터 삭제
		delete from tabel명;
		delete table명;
	
	3-2. 조건에 부합하는 데이터만 삭제
		delete from tabel명 where 조건식;
		delete table명 where 조건식;

4. merge
	다수의 테이블 데이터를 하나로 병합하는 구조
	4-1. syntax
		merge into 병합받을table명 별칭
		using 이미 데이터를 보유한 table
		on (조건식: 병합받을테이블.기준컬럼 = 데이터를제공하는테이블.컬럼)
		when matched then
			조건식이 true인 경우 실행 (주로 update)
		when not matched then
			조건식이 false인 경우 실행 (주로 insert);
		
*/

drop table people;

-- table은 입력 데이터의 타입과 크기만 제한이 있다
-- null 값도 저장 가능한 구조
create table people(
	name varchar2(10),
	age number(3)
);

desc people;


-- *** insert ****
--1. 칼럼명 기술없이 데이터 입력
-- table에 존재하는 모든 컬럼에 값 저장 의미
-- 주의 사항: desc table 명으로 검색된 컬럼 순서에 맞게 데이터 세팅
insert into people values('이홍주', 26);
select * from people;


--2. 칼럼명 기술후 데이터 입력
-- 컬럼명을 명시하기 때문에 데이터 저장 순서는 insert 작업하는 사람이 편집 가능
insert into people (name, age) values ('Lee', 5);
insert into people (age, name) values (77, 'Hey');

select * from people;

insert into people (name, age) values ('abcdefghijklmnopqrstuvwxyz', 77);


--3. 다중 table에 한번에 데이터 insert하기 
drop table emp01;
drop table emp02;
create table emp01 as select empno, ename, deptno from emp where 1=0;
create table emp02 as select empno, ename, deptno from emp where 1=0;
select * from emp01;
select * from emp02;

-- table은 존재하나 데이터가 없는 상태. 데이터 insert
insert all
	into emp01 values(empno, ename, deptno)
	into emp02 values(empno, ename, deptno)
select empno, ename, deptno from emp;

select * from emp01;
select * from emp02;

-- 컬럼명 명시/기술해서 작성한 문장
insert all
	into emp01 (empno, ename, deptno) values(empno, ename, deptno)
	into emp02 (empno, ename, deptno) values(empno, ename, deptno)
select empno, ename, deptno from emp;

select * from emp01;
select * from emp02;

--4. ? 부서 번호가 10인 데이터는 emp01에 저장, 
-- 부서 번호가 20 or 30인 데이터는 emp02에 저장
-- 조건 표현 : when 조건식 then 조건식이TRUE일때실행되는식
drop table emp01;
drop table emp02;
create table emp01 as select empno, ename, deptno from emp where 1=0;
create table emp02 as select empno, ename, deptno from emp where 1=0;

insert all
	when deptno=10 then
		into emp01 values(empno, ename, deptno)
	when deptno=20 or deptno=30 then
		into emp02 values(empno, ename, deptno)
select empno, ename, deptno from emp;


-- 오늘 같은 소회의실 팀원들 정보를 저장해보기
-- empno와 deptno는 임시로 설정, ename은 동기 이름으로 저장
insert all
	into emp01 values(1, '이홍주', 1)
	into emp01 values(2, '하예진', 2)
	into emp01 values(3, '김수연', 3)
select * from dual;

select * from emp01;

-- 데이터만 삭제 - rollback으로 복구 불가능한 데이터 삭제 명령어
truncate table emp01;
truncate table emp02;

select * from emp01;


select * from emp01;






-- *** update ***
--1. 테이블의 모든 행 변경
drop table emp01;
create table emp01 as select * from emp;
select deptno from emp01;

-- 모든 deptno를 99로 수정
-- 어떤 table의 어떤 컬럼을 어떤 데이터로 바꿀 것인지.
update emp01 set deptno=99;


select deptno from emp01;

-- 이전의 데이터로 복원
rollback;
 


--2. ? emp01 table의 모든 사원의 급여를 10%(sal*1.1) 인상하기
--? emp table로 부터 empno, sal, hiredate, ename 순으로 table 생성
drop table emp01;
create table emp01 as select empno, sal, hiredate, ename from emp;
select * from emp01;

update emp01 set sal=sal*1.1;

select * from emp01;


--3. emp01의 모든 사원의 입사일을 오늘(sysdate)로 바꿔주세요
update emp01 set hiredate=sysdate;
select * from emp01;


-- 4. 급여가 3000이상(where sal >= 3000)인 사원의 급여만 10%인상
update emp01 set sal=sal*1.1 where sal>=3000;
select * from emp01;



--5. ?emp01 table 사원의 급여가 1000이상인 사원들의 급여만 500원씩 삭감 
-- insert/update/delete 문장에 한해서만 commit과 rollback 영향을 받음
update emp01 set sal=sal-500 where sal>=1000;
select * from emp01;


--6. emp01 table에 DALLAS(dept의 loc)에 위치한 부서의 소속 사원들의 급여를 1000인상
-- 서브쿼리 사용
drop table emp01;
create table emp01 as select * from emp;
select * from emp01;

update emp01 set sal=sal+1000
where deptno=(
	select deptno from dept where loc='DALLAS'
);

select * from emp01;



--7. emp01 table의 SMITH 사원의 부서 번호를 30으로, 직급은 MANAGER 수정
-- 두개 이상의 칼럼값 동시 수정
select deptno, job from emp01 where ename='SMITH';

update emp01 
set deptno=30, job='MANAGER' 
where ename='SMITH';

select deptno, job from emp01 where ename='SMITH';



-- *** delete ***
--8. 하나의 table의 모든 데이터 삭제
-- delete [from] 테이블명;
select * from emp01;

delete from emp01;
select * from emp01;
rollback;
select * from emp01;

delete emp01;
select * from emp01;


--9. 특정 row 삭제(where 조건식 기준)
delete from emp01 where deptno=30;
select * from emp01;

rollback;

--10. emp01 table에서 comm 존재 자체가 없는(null) 사원 모두 삭제
delete from emp01 where comm is null;
select * from emp01;

--11. emp01 table에서 comm이 null이 아닌 사원 모두 삭제
delete from emp01 where comm is not null;
select * from emp01;

--12. emp01 table에서 부서명이 RESEARCH 부서에 소속된 사원 삭제 
-- 서브쿼리 활용
select * from emp01;

delete from emp01 
where deptno=(
	select deptno from dept where dname='RESEARCH'
);

select * from emp01;

--13. table내용 삭제
delete from emp01;
rollback;
truncate table emp01;



-- *** merge[병합] ***
--14. 병합을 위한 test table생성 및 데이터 insert
/*
produce01과 02는 새로 개발한 제품들 관리 table
produce_total은 재고 관리 table

제품이 새로 생산되면 01과 02에는 없는 데이터 insert
produce_total에 새로운 데이터 유입은 insert, 이미 존재하는 데이터는 update.
*/


-- 판매 관련 table들
drop table produce01;
drop table produce02;
drop table produce_total;

create table produce01(
	판매번호 varchar2(5), 
	제품번호 char(4),
	수량 number(3),
	금액 number(5)
);
create table produce02(
	판매번호 varchar2(5), 
	제품번호 char(4),
	수량 number(3),
	금액 number(5)
);
create table produce_total(
	판매번호 varchar2(5), 
	제품번호 char(4),
	수량 number(3),
	금액 number(5)
);

-- test용 데이터 insert
insert all
	into produce01 values('101', '1001', 1, 500)
	into produce01 values('102', '1002', 1, 400)
	into produce01 values('103', '1003', 1, 300)
	into produce02 values('201', '1004', 1, 500)
	into produce02 values('202', '1005', 1, 600)
	into produce02 values('203', '1006', 1, 700)
select * from dual;

commit; -- 영구 저장. 이 직후에 rollback해도 여기가 체크포인트라서 insert된 데이터 삭제 불가

select * from produce01;
select * from produce02;
select * from produce_total;


-- merge 작업 : produce01과 produce_total 병합
-- ? 문법 이해를 위한 문제 분석해 보기 
select * from produce_total;

-- table명 별칭 부여
merge into produce_total t
using produce01 p1
on (t.판매번호 = p1.판매번호)
when matched then
	update set t.수량 = t.수량+p1.수량
when not matched then 
	insert values(p1.판매번호, p1.제품번호, p1.수량, p1.금액);

-- 실행 결과 확인
select * from produce_total;



--? produce02 table과 produce_total table 병합 
select * from produce_total;

merge into produce_total t
using produce02 p2
on (t.판매번호 = p2.판매번호)
when matched then
	update set t.수량 = t.수량+p2.수량
when not matched then 
	insert values(p2.판매번호, p2.제품번호, p2.수량, p2.금액);


select * from produce_total;

