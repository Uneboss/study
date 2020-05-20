## employees.json 파일을 import하고 다음 SQL로 찾을 수 있는 것과 동등한 mongoDB 질의를 작성하여 실행한 후, 결과 화면을 캡쳐하여 제출하시오.
### (1)  Select * from emplyees where empno=7369
```
db.employees.find({empno:7369})
```
{ "_id" : "E1", "empno" : 7369, "ename" : "SMITH", "job" : "CLERK", "hiredate" : "17-12-1980", "sal" : 800, "deptno" : 20 }

### (2) Select ename from emlpoyees where empno=7900
```
db.employees.find({empno:7900}, {ename:1})
```
{ "_id" : "E2", "ename" : "JAMES" }

### (3)  Select empno, ename from employees where empno > 7500 and empno <=7600
```
db.employees.find({empno:{$gt:7500, $lte:7600}}, {empno:1, ename:1, _id:0})
```
{ "empno" : 7566, "ename" : "JONES" }<br>
{ "empno" : 7521, "ename" : "WARD" }

### (4)  Select empno from employees where empno = 7782 or empno=7844
```
db.employees.find($or:[{empno:7782}, {empno:7844}]}, {empno:1, _id:0})
```
{ "empno" : 7782 }<br>
{ "empno" : 7844 }

### (5)  Select count(*) from employees
```
db.employees.count()
```
14

### (6)  Select count(*) from employees where empno > 7900
방법1
```
db.employees.find({empno:{$gt:7900}}).count()
```
2
방법2
```
db.employees.count({empno:{$gt:7900}})
```
2

### (7)  Select distinct deptno from employees
```
db.employees.distinct("deptno")
```
[ 10, 20, 30 ]

### (8)  Select ename, job from employees where deptno=10 prder by ename desc
```
db.employees.find({deptno:10}, {ename:1, job:1, _id:0}).sort({ename:-1})
```
{ "ename" : "PRESIDENT", "job" : "CEO" }<br>
{ "ename" : "CLERK", "job" : "CLERK" }<br>
{ "ename" : "CLARK", "job" : "MANAGER" }

### (9) Select sum(salary) from employees
```
db.employees.aggregate([ $group: {_id:null, total_salary: {$sum: "$sal"}}}])
```
{ "_id" : null, "total_salary" : 29025 }

### (10) Select deptno, avg(salary) from employees group by deptno order by deptno
```
db.employees.aggregate([{ $group: {_id: "$deptno", avg_sal: {$avg:"$sal"}}}, {$sort: {_id:1}}])
```
{ "_id" : 10, "avg_sal" : 2916.6666666666665 }<br>
{ "_id" : 10, "avg_sal" : 2175 }<br>
{ "_id" : 10, "avg_sal" : 1566.6666666666667 }
