# SQL
: 관계형 DB에서 데이터 정의, 조작, 제어를 위해 사용하는 언어

### SQL의 분류
- DML(Data Manipulation Language) : SELECT, INSERT, UPDATE, DELETE 등 데이터 조작어
- DDL(Data Definition Language) : 테이블 생성, 수정, 삭제; CREATE, ALTER, DROP, RENAME 등 데이터 정의어
- DCL(Data Control Language) : GRANT, REVOKE 등 데이터 제어어
- TCL(Transaction Control Language) : COMMIT, ROLLBACK 등 트랜잭션 제어어

### 기본 핵심 용어
- **테이블** : 데이터를 저장하는 객체, 로우(가루, 행)와 칼럼(세로, 열)으로 구성
- **정규화** : 데이터의 정합성 확보와 데이터 입력/수정/삭제시 발생할 수 있는 이상현상을 방지하기 위함.
- **기본키(PRIMARY KEY)** : 테이블에 존재하는 각 행을 한 가지 의미로 특정할 수 있는 한 개 이상의 칼럼
- **외부키(FOREIGN KEY)** : 다른 테이블의 기본키로 사용되고 있는 관계를 연결하는 칼럼

***

### 데이터 유형
- CHAR(s) : 고정 길이 문자열 정보
- VARCHAR(s) : 가변 길이 문자열 정보
- NUMERIC : 정수, 실수 등 숫자 정보
- DATE : 날짜와 시각 정보

### 제약조건
- PRIMARY KEY(기본키)
- UNIQUE KEY(고유키)
- NOT NULL
- CHECK : 입력값 범위 제한
- FOREIGN KEY(외래키)

***

### DDL_SQL의 데이터 정의 기능
- 테아불 생성 : **CREATE TABLE**
- 테이블 변경 : **ALTER TABLE**
- 테이블 제거 : **DROP TABLE**
***
### DML_SQL의 데이터 조작 기능
- 데이터 검색 : **SELECT**
- 데이터 삽입 : **INSERT**
- 데이터 수정 : **UPDATE**
- 데이터 삭제 : **DELETE**<br>
~~DDL 명령어의 경우 실행시 AUTO COMMIT하지만 DML의 경우 COMMIT을 입력해야 함. (SQL Server의 경울 DML도 AUTO COMMIT)~~
***
### TCL_트랜잭션 제어어
트랜잭션(TRANSACTION) : DBMS에서 데이터를 다루는 밀접히 관련되어 분리될 수 없는 1개 이상의 DB 조작의 단위.
데이터베이스에서 트랜잭션을 정의하는 이유 : 회복(장애복구)의 단위, 동시성 제어
- COMMIT : 올바르게 반영된 데이터를 DB에 반영
- ROLLBACK : 트랜잭션 시작 이전의 상태로 되돌림
- SAVEPOINT : 저장 지점

* SAVEPOINT SVPT1; (Oracle)
* ROLLBACK TO SVPT1; (Oracle)
* SAVE TRAN SVPT1; (SQL Server)
* ROLLBACK TRAN SVPT1; (SQL Server)
* COMMIT;

### 트랜잭션의 특성
1. **원자성(Atomicity)** :트랜잭션에서 정의된 연산들은 모두 성공적으로 수행되거나 아니면 전부 수행되지 않아야 함. (all or nothing)
2. **일관성(Consistency)** : 트랜잭션 실행 전 db 내용이 잘못되지 않으면 실행 후도 잘못되지 않아야 함.
3. **고립성(Isolation)** : 수행 중인 트랜잭션에 다른 트랜잭션이 끼어들어 변경 중인 데이터 값을 훼손하는 일이 없어야 함.
4. **지속성(Durability)** : 트랜잭션이 성공적으로 수행되면 변경된 데이터는 영구히 저장됨.

***

### 연산자
- BETWEEN a AND b : a와 b 값 사이에 있으면 됨.
- IN (list) : 라스트에 있는 값 중 어느 하나라도 일치.
- NOT IN (list) : 리스트에 있는 값과 일치하지 않음.
- LIKE '비교문자열' : 비교문자열의 형태가 일치.
- IS NULL : NULL값인 경우.
- IS NOT NULL : NULL값을 갖지 않음.

  - **연산자 우선순위** : () -> NOT -> 비교연산자 -> AND -> OR
  - EX.<br>
SELECT PLAYER_NAME 선수명<br>
FROM PLAYER<br>
ex1)WHERE TEAM_ID = 'K2'; -> TEAM_ID가 'K2'인 사람<br>
ex2)WHERE TEAM_ID IN ('K2','K7'); -> TEAM_ID가 K2, K7 중 하나라도 일치하는 사람<br>
ex3)WHERE HEIGHT BETWEEN 170 AND 180; -> 키가 170~180인 사람  ex4)WHERE POSITION IS NULL; -> 포지션이 없는 사람

> NULL값과의 수치연산은 NULL값을 리턴한다.<br>
NULL값과의 비교연산은 FALSE를 리턴한다.

* ROWNUM : 원하는 만큼의 행을 가져올 때 사용 (= TOP : SQL Server)
  - WHERE ROWNUM = 1;
  - SELECT TOP(1) PLAYER_NAME  FROM PLAYER;

***

### 문자형 함수
- LOWER : 문자열을 소문자로
- UPPER : 문자열을 대문자로
- ASCII : 문자의 ASCII값 반환
- CHR/CHAR : ASCII값에 해당하는 문자 반환
- CONCAT : 문자열1,2를 연결
- SUBSTR/SUBSTRING : 문자열 중 m위치에서 n개의 문자 반환
- LENGTH/LEN : 문자열 길이를 숫자값으로 반환<br><br>
- CONCAT('RDBMS','SQL') -> 'RDBMS SQL'
- SUBSTR('SQL Expert',5,3) -> 'Exp'
- LTRIM('xxxYYZZxYZ','x') -> 'YYZZxYZ'
- RTRIM('XXYYzzXYzz','z') -> 'XXYYzzXY'
- TRIM('x' FROM 'xxYYZZxYZxx') -> 'YYZZxYZ'

### 숫자형 함수
- SIGN(n) : 숫자가 양수면 1, 음수면 -1, 0이면 0 반환
- MOD : 숫자 1을 숫자 2로 나누어 나머지 반환
- CEIL/CEILING(n) : 크거나 같은 최소 정수 반환
- FLOOR(n) : 작거나 같은 최대 정수 리턴
- ROUND(38.5235,3) -> 38.524(br)
  ROUND(38.5235) -> 39
- TRUNC(38.5235,3) -> 38.523(br)
  TRUNC(38.5235) -> 38
  
### 날짜형 함수
