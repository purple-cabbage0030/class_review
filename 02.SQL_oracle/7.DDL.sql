-- 7.DDL.sql
-- DDL(Data Definition Language): 데이터 정의 언어 - table 작성, 수정
-- table 생성(create)과 삭제(drop), table 구조 수정(alter)

/*
 [1] table 생성 명령어
    create table table명(
		칼럼명1 칼럼타입[(사이즈)] [제약조건(not null)] ,
		칼럼명2....
    ); 

[2] table 삭제 명령어
	drop table table명;

[3] table 구조 수정 명령어
	- 서비스 중에 table 구조 변경은 엄청난 일
	alter table table명;
*/

--1. table삭제 - 복원 불가
drop table test;

-- 불필요한 table 정리
purge recyclebin;


--2. table 생성  
-- name(varchar2(20byte)), age(number(2)) 칼럼 보유한 people table 생성
create table people(
	name varchar2(20),
	age number(2)
);




-- 3. 서브 쿼리 활용해서 emp01 table 생성(이미 존재하는 table기반으로 생성)
-- emp table의 모든 데이터로 emp01 생성
create table emp01 as select * from emp;
desc emp01;


-- 4. 서브쿼리 활용해서 특정 칼럼(empno)만으로 emp02 table 생성
create table emp02 as select empno from emp;



--5. deptno=10 조건문 반영해서 empno, ename, deptno로  emp03 table 생성
create table emp03 as select empno, ename, deptno 
from emp 
where deptno=10;



-- 6. 데이터 insert없이 table 구조로만 새로운 emp04 table생성 시 
-- 사용되는 조건식 : where=거짓(1=0)
create table emp04 as select * from emp where deptno=55;



-- emp01 table로 실습해 보기

--7. emp01 table에 job이라는 특정 칼럼 추가(job varchar2(10))
-- 이미 데이터를 보유한 table에 새로운 job칼럼 추가 가능 
-- add() : 컬럼 추가 함수
-- alter라는 명령어로 이미 존재하는 table의 구조를 조작

desc emp01;
drop table emp01;
create table emp01 as select empno, ename from emp;
desc emp01;

-- job 컬럼 추가 (add(컬럼명 타입(사이즈)))
alter table emp01 add (job varchar2(10));

desc emp01;
select * from emp01;


--8. 이미 존재하는 칼럼 사이즈 변경 시도해 보기
-- 데이터 미 존재 칼럼의 사이즈 크게 또는 작게 수정 가능하다.
-- modify(컬럼명 타입(사이즈))

desc emp01;
alter table emp01 modify(job varchar2(20));
desc emp01;

desc emp01;
alter table emp01 modify(job varchar2(10));
desc emp01;

--9. 이미 데이터가 존재할 경우 칼럼 사이즈가 큰 사이즈의 컬럼으로 변경 가능 
-- 혹 사이즈 감소시 주의사항 : 이미 존재하는 데이터보다 적은 사이즈로 변경 절대 불가
-- 데이터 크기보다 컬럼 사이즈를 적게 변경하려는 시도는 데이터 손실 위험
-- RDBMS는 이를 절대 허락하지 않음!!
drop table emp01;
create table emp01 as select empno, ename, job from emp;
select * from emp01;
desc emp01;

-- 기존 컬럼 사이즈보다 크게 수정 시도
alter table emp01 modify(job varchar2(20));
desc emp01;
select * from emp01;

-- 기존 컬럼 및 데이터 사이즈보다 작게 수정 시도 --> 실패
alter table emp01 modify(job varchar2(5));
desc emp01;
select * from emp01;


--10. job 칼럼 삭제 
-- 데이터 존재시에도 자동 삭제 
-- drop 시의 필요 정보: 컬럼명만 있으면 됨

alter table emp01 drop column job;
desc emp01;
select * from emp01;


--11. emp01을 test01로 table 이름 변경
rename emp01 to test01;
desc emp01;
desc test01;

--12. table의 순수 데이터만 완벽하게 삭제 및 복원하는 명령어 

delete from test01;
select * from test01;

-- 복원 명령어
-- rollback은 영구 저장된 시점이 있고, insert/update/delete에 한해서만 유효하다.
-- rollback 시 영구 저장된 시점으로 복구된다. (체크 포인트 같은)
-- 저 명령어들이 무효화되는?
rollback;
select * from test01;

-- table의 데이터만 완벽하게 삭제 (데이터 복원 절대 불가)
truncate table test01;
