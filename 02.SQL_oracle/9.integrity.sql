-- 9.integrity.sql
-- DB 자체적으로 강제적인 제약 사항 설정
-- 개발자 능력 + 시스템(HW/SW) 다 유기적으로 연계돼서 안정적인 데이터 관리 및 보존 보장
-- 설정은 개발자(db에 테이블 생성 및 관리할 수 있는 SQL 만드는 직무)의 책임

/*
1. table 생성시 제약조건을 설정하는 기법 

2. 제약 조건 종류
	emp와 dept의 관계
		- 주종관계/ 부모자식관계/ 상위table, 하위table, ...
		- emp의 deptno는 반드시 dept의 deptno 컬럼 값에 종속적으로 사용되는 컬럼
		- dept에서 제공하지 않는 데이터는 emp에서 사용 불가
		- dept가 데이터 제공해주는 테이블, demp는 dept를 사용/참조하는 table
		- dept는 주(부모) / emp는 종(자식)

	2-1. PK[primary key] - 기본키, 중복불가, null불가, 데이터들 구분을 위한 핵심 데이터
		: not null + unique
	2-2. not null - 반드시 데이터 존재
	2-3. unique - 중복 불가, NULL은 허용

	2-4. check 
		- table 생성시 규정한 범위의 데이터만 저장 가능 
		- 예시: sql 자체적으로 table 생성 시 m or f만 저장 가능하게
			그 이외 데이터로 insert or update 시 철저히 db자체적으로 차단

	2-5. default - insert시에 특별한 데이터 미저장시에도 자동 저장되는 기본 값
		- python 관점에는 멤버 변수 선언 후 객체 생성 직후 멤버 변수 기본값으로 초기화
	
	2-6. FK[foreign key] 
		- 외래키[참조키], 다른 table의 pk를 참조하는 데이터 
		- table간의 주종 관계가 형성
		- pk 보유 table이 부모, 참조하는 table이 자식
		- 부모의 미 존재하는 데이터를 자식에서 새로 생성가능? 불가 
		- 자식 table들이 존재할 경우 부모table만 삭제 가능? 불가
			- 해결책 : 관계를 해제도 가능하나 가급적 분석설계시 완벽하리만큼 고민후 설계
	

3. 제약 조건명 명시하는 방법
cf) (오라클 db 컬럼 타입 관련)문자열 데이터를 표현하는 단일 따옴표로 number 타입의 컬럼에도 값 저장 가능
	- number(2)
		정수 두자리까지만 허용 숫자 타입
	- 문자열 포맷으로 저장 시도 시 오라클 엔진이 number 포맷으로 자동 변환 및 반올림.

	3-1. oracle engine이 기본적으로 설정
		- 사용자가 제약 조건에 별도의 이름을 부여하지 않으면 오라클 자체적으로 SYS_시작하는 이름을 자동 부여
		- 명명규칙: SYS_Xxxx

	3-2. 사용자 정의하는 제약 조건에 제약 조건명 명시하는 방법
		sql개발자가 직접 설정
		- table명_컬럼명_제약조건명등 기술..단 순서는 임의 변경 가능
			: dept의 deptno이 제약조건명
				PK_DEPT
				pk_dept_deptno
		- 약어 사용도 가능[분석, 설계시 용어사전 제시후 작성 권장]
	
4. 제약조건 선언 위치
	4-1. 컬럼 레벨 단위
		- 컬럼선언 라인에 제약조건 설정 

	4-2. 테이블 레벨 단위 
		- 모든 컬럼 선언 직후 별도로 제약조건 설정 
	
5. 오라클 자체 특별한 table
	5-1. user_constraints
		- 딕셔너리 table
		- 제약조건 정보 보유 table
		- 개발자가 table의 데이터값 직접 수정 불가
		- select constraint_name, constraint_type, table_name 
			from user_constraints;

CONSTRAINT_NAME      CO TABLE_NAME
-------------------- -- --------------
PK_DEPT              P  DEPT
PK_EMP               P  EMP
FK_DEPTNO            R  EMP

dept의 제약 조건: deptno는 절대 중복 불가
emp의 제약 조건: deptno의 값은 dept table로부터 참조해서 사용
				emp는 절대 중복 불가
		
		- contraint_name: db 설계해서 sql문장 구성 시에 실제 db에 부여하는 사용자 정의 제약조건 명
			- pk_dept: dept table의 primary key - 기본키, 주키: 절대 중복 불가인 세팅
				실제 업계 권장 이름: PK_DEPT_DEPTNO
			- fk_deptno: foreign key - 외래키, 참조키, reference key: 다른 테이블의 고유한 값을 보유한 컬럼을 참조
				실제 업계 권장 이름: FK_DEPTNO_EMP / FK_DMP_DEPTNO
		- co: constraint 약어
			- P: primary key
			- R: reference


6. 이미 존재하는 table의 제약조건 수정(추가, 삭제)명령어
	6-1. 제약조건 추가
		alter table 테이블명 add constraint 제약조건명 제약조건(컬럼명);
		alter table dept01 add constraint dept01_deptno_pk primary key(deptno);
		
	6-2. 제약조건 삭제(drop)
		- table삭제 
		alter table 테이블명 cascade constraint;
		
		alter table 테이블명 drop 제약조건명;
		alter table dept01 drop primary key;
		
	6-3. 제약조건 임시 비활성화
		alter table emp01 disable constraint emp01_deptno_fk;

	6-4. 제약조건 활성화
		alter table emp01 enable constraint emp01_deptno_fk;

* tip
== 데이터베이스 모델링 -> 구축
	- 데이터베이스 모델링 tool 종류가 다양
		ERD라는 도식화된 그림으로 모델링 작업 수행
		ERD로 sql문장 자동 생성
			- 필수 사전 지식: DDL(create, drop, alter)
	tool들의 특징
		1) create 후에 alter 명령들로 제약조건 추가하는 게 보편적

*/

-- 1.  딕셔너리 table 검색
select * from user_constraints;
desc user_constraints;



--2. 사용자 정의 제약 조건명 명시하기
drop table emp02;

-- constraint emp02_empno_nn not null
-- constraint: 제약조건 설정함을 의미하는 oracle 키워드
-- emp02_empno_nn: 사용자가 설정한 이름
-- not null: null 불허의 제약 조건 의미
-- cf) not null만 있는 제약조건 설정 시에는 이름을 부여하지는 않음
create  table emp02(
	empno number(4) constraint emp02_empno_nn not null,
	ename varchar2(10)
);

-- 테이블 생성 시에 이름을 소문자로 생성했지만
-- 관리를 위한 딕셔너리 테이블에는 대문자로 저장되어있음.
select constraint_name, constraint_type, table_name
from user_constraints where table_name='EMP02';

-- 그래서 이렇게 실행 안 됨!!
select constraint_name, constraint_type, table_name
from user_constraints where table_name='emp02';


--3. 사용자 정의 제약조건명 설정 후 위배시 출력되는 메세지에 사용자정의 제약조건명
	-- 확인 가능 : not null을 제외한 제약조건명은 에러 발생시 가시적인 확인 가능
drop table emp02;

create  table emp02(
	empno number(4) not null,
	ename varchar2(10)
);


insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'tester');
insert into emp02 (empno) values(1);
-- insert into emp02 (ename) values('m');
-- cannot insert NULL into ("SCOTT"."EMP02"."EMPNO")


-- 4-1. 제약조건명을 오라클 엔진이 자동적으로 지정
	-- 에러 발생시 SYS_xxxx로 출력됨 
drop table emp02;
create table emp02(
	empno number(4)  unique,
	ename varchar2(10)
);

select constraint_name, constraint_type, table_name
from user_constraints where table_name='EMP02';

insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'master');
-- unique constraint (SCOTT.SYS_C007008) violated

select * from emp02;

-- 4-2. 사용자가 설정하는 제약 조건명 확인

drop table emp02;
create table emp02(
	empno number(4) constraint emp02_empno_u unique,
	ename varchar2(10)
);

select constraint_name, constraint_type, table_name
from user_constraints where table_name='EMP02';

insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'master');
-- unique constraint (SCOTT.EMP02_EMPNO_U) violated

select * from emp02;




-- 5-1. pk설정 : 선언 위치에 따른 구분 학습
-- 제약 조건 명시 권장

-- 단순 테스트: pk 오류 시 primary key에 해당하는 오류인지 아닌지는 모르고
-- 그냥 unique constraint라고만 나와서 상세 정보 부족
drop table emp02;

create table emp02(
	empno number(4) primary key,
	ename varchar2(20) not null
);

insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'tester2');
-- unique constraint (SCOTT.SYS_C007011) violated

select * from emp02;

-- 5-2. 제약 조건 설정을 컬럼 선언 시에 함께 작업(컬럼 레벨 단위)
drop table emp02;

create table emp02(
	empno number(4) constraint pk_emp02_empno primary key,
	ename varchar2(20) not null
);

insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'tester2');
-- unique constraint (SCOTT.PK_EMP02_EMPNO) violated

select * from emp02;

-- 5-3. 테이블 레벨 단위로 작업
-- 제약조건 마지막단에 소괄호 안에 해당하는 컬럼명 명시
drop table emp02;

create table emp02(
	empno number(4),
	ename varchar2(20) not null,
	constraint pk_emp02_empno primary key (empno)
);

insert into emp02 values(1, 'tester');
insert into emp02 values(1, 'tester2');
-- unique constraint (SCOTT.PK_EMP02_EMPNO) violated

select * from emp02;

--6. 외래키[참조키]
-- 이미 제약 조건이 설정된 dept table의 pk컬럼인 deptno값을 기준으로 
-- emp02의 deptno에서 dept의 deptno를 참조/반영(참조키, 외래키, fk)
-- 부모컬럼의 타입과 똑같이 해야 함
drop table emp02;

create table emp02(
	empno number(4) constraint pk_emp02_empno primary key,
	ename varchar2(20) not null,
	deptno number(2) constraint fk_emp02_deptno references dept(deptno)
);

insert into emp02 values(1, 'tester', 10);
insert into emp02 values(2, 'tester', 90);
-- integrity constraint (SCOTT.FK_EMP02_DEPTNO) violated - parent key not found

select * from emp02;


--7. 6번의 내용을 table 레벨 단위로 설정해 보기 (이게 선호하는 방법?)
drop table emp02;

create table emp02(
	empno number(4),
	ename varchar2(20) not null,
	deptno number(2),
	constraint pk_emp02_empno primary key (empno),
	constraint fk_emp02_deptno foreign key (deptno) references dept(deptno)
);

insert into emp02 values(1, 'tester', 10);
insert into emp02 values(2, 'tester', 90);
-- integrity constraint (SCOTT.FK_EMP02_DEPTNO) violated - parent key not found

select * from emp02;


--8. emp01과 dept01 table 생성
-- create와 as select로 복제되는 table은 원본 테이블의 데이터와 table 구조는 복제가 되나
-- 제약 조건은 복제되지 않는다.

drop table dept01;
drop table emp01;
create table dept01 as select * from dept;
create table emp01 as select * from emp;

select table_name, constraint_type, constraint_name
from user_constraints 
where table_name='DEPT01';
-- no rows selected. 제약 조건 복제 안 됨

select table_name, constraint_type, constraint_name
from user_constraints 
where table_name='DEPT';

--9. 이미 존재하는 table에 제약조건 추가하는 명령어 
-- dept01에 dept처럼 deptno를 pk로 설정 -> 이미 테이블 만들어져 있어서 alter 이용 !!
alter table dept01 add constraint pk_dept01_deptno primary key (deptno);

select table_name, constraint_type, constraint_name
from user_constraints 
where table_name='DEPT01';



-- ? emp01에 제약조건 추가해 보기
alter table emp01 add constraint pk_emp01_empno primary key (empno);
alter table emp01 add constraint fk_emp01_deptno foreign key (deptno) references dept01(deptno);

select table_name, constraint_type, constraint_name
from user_constraints 
where table_name='EMP01';

select table_name, constraint_type, constraint_name
from user_constraints 
where table_name='EMP';

-- dept01은 emp01의 부모(주), emp01은 dept01의 자식(종)


--10. 참조 당하는 key의 컬럼이라 하더라도 자식 table에서 미 사용되는 데이터에 한해서는
	-- 삭제 가능  
-- emp01이 이미 참조하는 데이터가 있는 dept01 table의 데이터 삭제해보기 
delete from dept01 where deptno=30;
-- integrity constraint (SCOTT.FK_EMP01_DEPTNO) violated - child record found

delete from dept01 where deptno=40;
-- 삭제됨

--11.참조되는 컬럼 데이터라 하더라도 삭제 가능한 명령어
	-- *** 현업에선 부득이하게 이미 개발중에 table 구조를 변경해야 할 경우가 간혹 발생
	-- 자식 존재 유무 완전 무시하고 부모 table삭제 

drop table dept01;
-- unique/primary keys in table referenced by foreign keys

drop table dept01 cascade constraint;		
	
--12. check : if 조건식처럼 저장 직전의 데이터의 유효 유무 검증하는 제약조건 
-- age값이 1~100까지만 DB에 저장
drop table emp01;

create table emp01(
	name varchar2(10) not null,
	age number(3) constraint ck_emp01_age check (age between 1 and 100)
);


insert into emp01 values('master', 10);
-- 에러 발생 : 1~100까지만 유효 
insert into emp01 values('master', 102);
-- check constraint (SCOTT.CK_EMP01_AGE) violated


select * from emp01;
select table_name, constraint_type, constraint_name
from user_constraints where table_name='EMP01';

-- 딕셔너리 table은 원본 테이블 삭제되면 함께 삭제됨(오라클 엔진 기능)
-- 딕셔너리 table은 직접 수정 불가

-- 13.? gender라는 컬럼에는 데이터가 M 또는(or) F만 저장되어야 함
/* 오라클 db 타입

1. varchar2(n)
	- n은 최대 문자열 허용 개수
	- 가변적인 문자열 타입
	- 3byte의 데이터만 저장했을 경우 실제 사용 메모리도 10byte가 아닌 3byte만 소진

2. char(10)
	- 고정 문자열 타입
	- 3byte의 데이터만 저장해도 실제 사용 메모리는 10byte

=== 결론 ===
문자열 데이터의 length가 실시간 가변적인 데이터들을 저장하는 컬럼이라면 varchar2 타입 선호
고정된 문자열 데이터를 저장하는 컬럼이라면 char

*/
drop table emp01;

create table emp01(
	name varchar2(10) not null,
	gender char(1) constraint ck_emp01_gen check (gender in ('F', 'M', 'N'))
);
-- in 괄호 안에 쉼표는 2개 이상도 가능


select table_name, constraint_type, constraint_name
from user_constraints where table_name='EMP01';


insert into emp01 values('master', 'F');
-- 오류 : insert into emp01 values('master', 'T'); 
-- check constraint (SCOTT.CK_EMP01_GEN) violated
select * from emp01;


--14. default : insert시에 데이터를 생략해도 자동으로 db에 저장되는 기본값 
drop table emp01;

create table emp01(
	id varchar2(10) primary key,
	gender char(1) default 'F'
);

insert into emp01 (id) values('master');
insert into emp01 values('tester', 'M');
select * from emp01;







