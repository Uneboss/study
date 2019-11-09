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
- ROUND(38.5235,3) -> 38.524<br>
  ROUND(38.5235) -> 39
- TRUNC(38.5235,3) -> 38.523<br>
  TRUNC(38.5235) -> 38
  
### 날짜형 함수
- SYSDATE/GETDATE() : 현재날짜와 시각 출력
- EXTRACT/DATEPART : 날짜에서 데이터 출력
- TO_NUMBER(TO_CHAR(d,'YYYY'))/YEAR(d)<br>
Ex.<br>
SELECT ENAME,<br>
       CASE WHEN SAL >= 3000 THEN 'HIGH'<br>
            WHEN SAL >= 1000 THEN 'MID'<br>
            ELSE 'LOW'<br>
       END AS SALARY_GRADE<br>
FROM EMP;

### NULL 관련 함수
- NVL(식1,식2)/ISNULL(식1,식2) : 식1의 값이 NULL이면 식2
- NULLIF(식1,식2) : 식1이 식2와 같으면 NULL을 아니면 식1을 출력
- COALESCE(식1,식2) : 임의의 개수표현식에서 NULL이 아닌 최초의 표현식, 모두 NULL이면 NULL 반환<br>
ex. COALESCE(NULL,NULL,'abc') -> 'abc'

***

### 집계 함수
1. 여러 행들의 그룹이 모여서 그룹당 단 하나의 결과를 돌려주는 함수이다.
2. GROUP BY 절은  행들을 소그룹화한다.
3. SELECT, HAVING, ORDER BY 절에 사용 가능
- ALL : Default 옵션
- DISTINCT : 같은 값을 하나의 데이터로 간주 옵션
- COUNT( * ) : NULL 포함 행의 수
- COUNT(표현식) : NULL 제외 행의 수
- SUM, AVG : NULL 제외 합계, 평균 연산
- STDDEV : 표준편차
- VARIAN : 분산
- MAX, MIN : 최대값, 최소값

### GROUP BY, HAVING 절의 특징
1. GROUP BY 절을 통을 통해 소그룹별 기준을 정한 후, SELECT 절에 집계 함수를 사용한다.
2. 집계 함수의 통계 정보는 NULL 값을 가진 행을 제외하고 수행한다.
3. GROUP BY 절에서는 ALIAS 사용 불가하다.
4. 집계 함수는 WHERE 절에 올 수 없다.
5. HAVING 절에는 집계 함수를 이용하여 조건 표시할 수 있다.
6. HAVING 절은 일반적으로 GROUP BY 뒤에 위치한다.

### SEARCHED_CASE_EXPRESSION
CASE WHEN LOC = 'a' THEN 'b'
### SIMPLE_CASE_EXPRESSEION
CASE LOC WHEN 'a' THEN 'b'<br>
위 두 명령문은 같은 의미이다.

***

### ORDER BY 특징
1. SQL 문장으로 조회된 데이터들을 다양한 목적에 맞게 특정한 칼럼을 기준으로 정렬하여 출력하는데 사용한다.
2. ORDER BY 절에 칼럼명 대신 ALIAS 명이나 칼럼 순서를 나타내는 정수도 사용 가능하다.
3. DEFAULT 값으로 오름차순(ASC)이 적용되며 DESC 옵션을 통해 내림차순으로 정렬이 가능하다.
4. SQL 문장의 제일 마지막에 위치한다.
5. SELECT 절에서 정의하지 않은 칼럼 사용 가능<br>
 ~~Oracle에서는 NULL을 가장 큰 값으로 취급하며 SQL Server에서는 NULL을 가장 작은 값으로 취급한다.~~

### SELECT 문장 실행 순서
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY <br>
<br>
Ex)<br>
SELECT TOP(2) WITH TIES ENAME, SAL
FROM EMP
ORDER BY SAL DESC;<br>
위는 급여가 높은 2명을 내림차순으로 출력하는데 같은 급여를 받는 사원은 같이 출력한다. (WITH TIES)
;;
***

### JOIN
: 두 개 이상의 테이블들을 연결 또는 결합하여 데이터를 출력하는 것.<br>
일반적으로 행들은 PK나 FK 값의 연관에 의해 JOIN 이 성립된다. 어떤 경우에는 PK, FK 관계가 없어도 논리적인 값들의 연관만으로 JOIN 이 성립가능하다.
<br>
5가지 테이블을 JOIN 하기 위해서는 최소 4번의 JOIN 과정이 필요하다. (N-1)

### EQUI JOIN
: 2개의 테이블 간에 칼럼값들이 서로 정확하게 일치하는 경우에 사용. 대부분 PK, FK의 관계를 기반으로 한다.

### NON EQUI JOIN
: 2개의 체이블 간에 칼럼값들이 서로 정확하게 일치하지 않는 경우에 사용.<br>
'=' 연산자가 아닌 BETWEEN, >, <= 등의 연산자 사용.<br>
<br> 
Ex.<br>
SELECT E.ENAME, E.JOB, E.SAL, S.GRADE
FROM EMP E, SALARY S
WHERE E.SAL BETWEEN S.LOSAL AND S.HSAL;<br>
위는 E의 SAL의 값을 S의 LOSAL과 HSAL 범위에서 찾는 것이다.

***

### 집합연산자
: 두 개 이상의 테이블에서 조인을 사용하지 않고 연관된 데이터를 조회할 때 사용.<br>
SELECT 절의 칼럼 수가 동일하고 SELECT 절의 동일 위치에 존재하는 칼럼의 데이터 타입이 상호 호환 가능할 때 사용 가능.

### 일반 집합 연산자
1. UNION : 합집합(중복 행은 1개로 처리)
2. UNION ALL : 합집합(중복 행도 표시)
3. INTERSECT : 교집합(INTERSECTION)
4. EXCEPT, MINUS : 차집합(DIFFERENCE)
5. CROSS JOIN : 곱집합(PRODUCT)

### 순수 관계 연산자
: 관계형 DB를 새롭게 구현
1. SELECT -> WHERE
2. PROJECT -> SELECT
3. NATURAL JOIN -> 다양한 JOIN
4. DIVIDE -> 사용X

### FROM 절 JOIN 형태
1. INNER JOIN
2. NATURAL JOIN
3. USING 조건절
4. ON 조건절
5. CROSS JOIN
6. OUTER JOIN

#### INNER JOIN
: JOIN 조건에서 동일한 값이 있는 행만 반환. USING이나 ON 절을 필수적으로 사용.
#### NATURAL JOIN
: 두 테이블 간의 동일한 이름을 갖는 모든 칼럼들에 대해 EQUI JOIN 수행. NATURAL JOIN이 명시되면 추가로 USING, ON, WHERE 절에서 JOIN 조건을 정의할 수 없다. (SQL Server 미지원)
#### USING 조건절
: 같은 이름을 가진 칼럼들 중에서 원하는 칼럼에 대해서만 선택적으로 EQUI JOIN을 할 수 있다. JOIN 칼럼에 대해서 ALIAS난 테이블 이름과 같은 접두사를 붙일 수 있다. (SQL Server 미지원)
#### ON 조건절
: ON 조건절과 WHERE 조건절을 분리하여 이해가 쉬우며, 칼럼명이 다르더라도 JOIN 조건을 사용할 수 있는 장점이 있다. ALIAS나 테이블명 반드시 사용.
#### CROSS JOIN
: 양쪽 집합의 M * N 건의 데이터 조합이 발생한다.
#### OUTER JOIN
: JOIN 조건에서 동일한 값이 없는 행도 반환 가능하다. USING이나 ON 조건절 반드시 사용해야 함.
#### LEFT OUTER JOIN
: 조인 수행시 먼저 표기된 좌측 테이블에 해당하는 데이터를 읽은 후, 나중 표기된 우측 테이블에서 JOIN 대상 데이터를 읽어온다. 우측 값에서 같은 값이 없는 경우 NULL 값으로 채운다.
#### RIGHT OUTER JOIN
: 조인 수행시 먼저 표기된 우측 테이블에 해당하는 데이터를 읽은 후, 나중 표기된 좌측 테이블에서 JOIN 대상 데이터를 읽어온다. 좌측 값에서 같은 값이 없는 경우 NULL 값으로 채운다.
#### FULL OUTER JOIN
: 조인 수행시 좌측, 우측 테이블의 모든 데이터를 읽어 JOIN하여 결과를 생성한다. 중복 데이터는 삭제한다.

***
