## Movie DataBase
### 1. Title이 “The Matrix”인 영화를 찾으시오.
```SQL
MATCH (m:Movie) WHERE m.title = “The Matrix” RETURN m
```
### 2. 영화 “The Matrix”에 출연한 모든 배우 찾기
```
MATCH (actors)-[:ACTED_IN]->(m1:Movie)
WHERE m.title = “The Matrix”
RETURN actors
```
### 3. “Tom Hanks”가 출연한 영화의 감독
```
MATCH (p:Person)-[:ACTED_IN]->(movie)<-[:DIRECTED]-(Director:Person)
WHERE p.name = “Tom Hanks”
RETURN Director
```
### 4. “Tom Hanks”가 출연한 영화에 함께 출연한 배우
```
MATCH (p:Person)-[:ACTED_IN]->(movie)<-[:ACTED_IN]-(actors:Person)
WHERE p.name = “Tom Hanks”
RETURN actors
```
### 5. “Tom Hanks”와 함께 출연한 영화가 없는 배우
```
MATCH (actors:Person)-[:ACTED_IN]->(movie), (hanks:Person{name:”Tom Hanks”})
WHERE NOT (hanks)-[:ACTED_IN]->(movie)
RETURN actors
```
### 6. “Kevin Bacon”과 4칸 거리에 있는 배우
```
MATCH (bacon:Person{name:”Kevin Bacon”})-[*4]-(actors:Person) 
WHERE (actors)-[:ACTED_IN]->()
RETURN actors
```
