#SQL
:관계형 DB에서 데이터 정의, 조작, 제어를 위해 사용하는 언어

##SQL의 분류
-DML(Data Manipulation Language) : SELECT, INSERT, UPDATE, DELETE 등 데이터 조작어
-DDL(Data Definition Language) : 테이블 생성, 수정, 삭제; CREATE, ALTER, DROP, RENAME 등 데이터 정의어
-DCL(Data Control Language) : GRANT, REVOKE 등 데이터 제어어
-TCL(Transaction Control Language) : COMMIT, ROLLBACK 등 트랜잭션 제어어

###데이터 유형
-CHAR(s) : 고정 길이 문자열 정보
-VARCHAR(s) : 가변 길이 문자열 정보
-NUMERIC : 정수, 실수 등 숫자 정보
-DATE : 날짜와 시각 정보

**테이블** : 데이터를 저장하는 객체, 로우(가루, 행)와 칼럼(세로, 열)으로 구성
**정규화** : 데이터의 정합성 확보와 데이터 입력/수정/삭제시 발생할 수 있는 이상현상을 방지하기 위함.
**기본키(PRIMARY KEY)** : 테이블에 존재하는 각 행을 한 가지 의미로 특정할 수 있는 한 개 이상의 칼럼
**외부키(FOREIGN KEY)** : 다른 테이블의 기본키로 사용되고 있는 관계를 연결하는 칼럼


###제약조건
-PRIMARY KEY(기본키)
-UNIQUE KEY(고유키)
-NOT NULL
-CHECK : 입력값 범위 제한
-FOREIGN KEY(외래키)

###DDL_SQL의 데이터 정의 기능
-테아불 생성 : **CREATE TABLE**
-테이블 변경 : **ALTER TABLE**
-테이블 제거 : **DROP TABLE**

###DML_SQL의 데이터 조작 기능
-데이터 검색 : **SELECT**
-데이터 삽입 : **INSERT**
-데이터 수정 : **UPDATE**
-데이터 삭제 : **DELETE**
~~DDL 명령어의 경우 실행시 AUTO COMMIT하지만 DML의 경우 COMMIT을 입력해야 함. (SQL Server의 경울 DML도 AUTO COMMIT)~~

###TCL_트랜잭션 제어어
트랜잭션(TRANSACTION) : DBMS에서 데이터를 다루는 밀접히 관련되어 분리될 수 없는 1개 이상의 DB 조작의 단위.
데이터베이스에서 트랜잭션을 정의하는 이유 : 회복(장애복구)의 단위, 동시성 제어
-**COMMIT** : 올바르게 반영된 데이터를 DB에 반영
-**ROLLBACK** : 트랜잭션 시작 이전의 상태로 되돌림
-**SAVEPOINT** : 저장 지점

SAVEPOINT SVPT1; (Oracle)
ROLLBACK TO SVPT1; (Oracle)
SAVE TRAN SVPT1; (SQL Server)
ROLLBACK TRAN SVPT1; (SQL Server)
COMMIT;

###트랜잭션의 특성
1.**원자성(Atomicity)** :트랜잭션에서 정의된 연산들은 모두 성공적으로 수행되거나 아니면 전부 수행되지 않아야 함. (all or nothing)
2.**일관성(Consistency)** : 트랜잭션 실행 전 db 내용이 잘못되지 않으면 실행 후도 잘못되지 않아야 함.
3.**고립성(Isolation)** : 수행 중인 트랜잭션에 다른 트랜잭션이 끼어들어 변경 중인 데이터 값을 훼손하는 일이 없어야 함.
4.**지속성(Durability)** : 트랜잭션이 성공적으로 수행되면 변경된 데이터는 영구히 저장됨.