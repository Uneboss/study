## Basic Query

### 1. rating 점수가 5점인 게임과 해당 점수를 준 사람을 구하시오.
```
MATCH (u:User)-[r:PLAY]->(g:Game)
WHERE r.rating = 5
RETURN g, u
```
평가 점수가 5점인 게임 : “The Forest”, “Don’t Starve”, “Stardew Valley”, “Battle Ground”, “Day by Daylight”<br>
5점을 준 사람 : “Skunk”, “Frog”, “Giraffe”, “Pig”, “Dog”, “Fox”, “Turtle”

### 2. 장르가 “Survival” 인 게임과 이를 스트리밍한 스트리머를 구하시오.
```
MATCH (s:Streamer)-[:STREAMING]->(g:Game)-[:HAS_GENRE]->(ge:Genre)
WHERE ge.name = “Survival”
RETURN s, g
```
장르가 “Survival”인 게임 : “Don’t Starve”, “The Forest”, “Day by Daylight”, “Battle Ground”<br>
이를 스트리밍한 스트리머 : “Sky”, “Wind”, “Stone”, “Moon”, “Flower”, “Star”, “Sand”, “Sun”

### 3. 스트리머 “Ocean” 이 스트리밍한 게임과 이를 플레이한 유저를 구하시오.
```
MATCH (u:User)-[:PLAY]->(g:Game), (s:Streamer{stagename:”Ocean”})
WHERE (s)-[:STREAMING]->(g)
RETURN u, g
```
“Ocean”이 스트리밍한 게임 : “iRacing”, “Football Manager”<br>
이를 플레이한 유저 : “Elephant”, “Skunk”, “Duck”

### 4. 게임 “Battle Ground” 를 플레이한 유저와 유저의 플레이 시간을 플레이 시간이 큰 순서로 구하시오.
```
MATCH (u:User)-[r:PLAY]->(g:Game)
WHERE g.title=”Battle Ground”
RETURN u.name AS Users, r.playtime AS `Playtime of Battle Ground`
ORDER BY r.playtime DESC
```

### 5. “adventure” 장르를 가지는 게임 중 가장 평가점수가 좋은 게임과 해당 게임의 점수의 평균을 구하시오.
```
MATCH (u:User)-[r:PLAY]->(g:Game)-[:HAS_GENRE]->(ge:Genre{name:"Adventure"})
WITH avg(r.rating) AS rate_average, g
RETURN g.title AS Game, rate_average
ORDER BY rate_average DESC
LIMIT 1
```
“Don’t Starve”, 4.5

## Recommendation System

### 1. Turtle과 유사성이 높은 사람 5명를 찾고 그들이 점수를 많이 준 게임을 추천하기
#### Turtle과 같은 게임을 플레이한 사람들과 Turtle 사이의 코사인 유사도 구하기
```
MATCH (u1:User{name:"Turtle"})-[x:PLAY]->(g:Game)<-[y:PLAY]-(u2:User)
WITH SUM(x.rating*y.rating) AS xyDotProduct,
	SQRT(REDUCE(xDot=0.0, a IN COLLECT(x.rating)|xDot + a^2)) AS xLength,
    SQRT(REDUCE(yDot=0.0, b IN COLLECT(y.rating)|yDot + b^2)) AS yLength,
    u1, u2
MERGE (u1)-[s:SIMILARITY]-(u2)
SET s.similarity = xyDotProduct / (xLength * yLength)
RETURN s.similarity
```
#### Turtle과 유사성이 높은 사람 5명 찾기
```
MATCH (u1:User{name:"Turtle"})-[s:SIMILARITY]-(u2:User)
WITH u2, s.similarity AS sim
ORDER BY sim DESC
LIMIT 5
RETURN u2.name AS Neighbor, sim AS Similarity
```
“Squirrel”, “Fox”, “Giraffe”, “Skunk”, “Cat” 순으로 “Turtle”과 유사성이 높음.
#### “Turtle”에게 유사성이 높은 사람들이 점수를 많이 준 게임을 추천
```
MATCH (u:User)-[r:PLAY]->(g:Game), (u)-[s:SIMILARITY]-(fox:User{name:"Fox"})
WHERE NOT ((fox)-[:PLAY]->(g))
WITH g, s.similarity AS similarity, r.rating AS rating
ORDER BY g.title, similarity DESC
WITH g.title AS game, COLLECT(rating)[0..3] AS ratings
WITH game, REDUCE(s = 0, i IN ratings | s + i) AS reco
ORDER BY reco DESC
RETURN game AS Game, reco AS Recommandation
```
Turtle에게 “Battle Ground”, “Super Animal Royale”, “Stardew Valley”, “Football Manager”=”Rusty Lake”, “To The. Moon” 순으로 게임을 추천

### 2. “Fox”가 구독하는 스트리머가 가장 많이 스트리밍한 게임순으로 추천 
```
MATCH (fox:User{name:"Fox"})-[r1:SUBSCRIBE]->(s:Streamer)-[r2:STREAMING]->(g:Game)
WHERE NOT ((fox)-[:PLAY]->(g))
WITH g, count(g) AS game_count
ORDER BY game_count DESC
RETURN g.title AS Game, game_count AS `Recommendation by Streamer`
```
“Fox”에게 “Battle Ground”, “Don’t Starve”, “Stardew Valley” 순으로 게임을 추천

### 3. “Frog”와 같은 게임을 플레이한 사람들이 플레이한 게임들을 플레이시간의 평균이 가장 높은 순으로 추천
```
MATCH (u1:User)-[r:PLAY]->(g:Game), (frog:User{name:"Frog"})
WHERE NOT (frog)-[:PLAY]->(g)
RETURN g.title AS Game, avg(r.playtime) AS `Recommendation by Playtime`
ORDER BY avg(r.playtime) DESC
```
“Frog”에게 “Border Land”, “Football Manager”, “Stardew Valley”, “Super Animal Royale”, “To The Moon”, “Asphalt”, “iRacing”, “Rusty Lake” 순으로 게임을 추천
