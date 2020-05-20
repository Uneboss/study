## 지리정보 데이터베이스

### 데이터베이스 생성
Point – 반포초등학교, 반포중학교, 세화여자고등학교
LineString – 지하철 9호선, 4호선
Ploygon – 주공아파트단지, 현충원, 이수번화가

### import
```
daebagsangkom-i:data une$ mongoimport -d geoDB --collection geometry geometry.json
```

### 2dsphere index 생성
```
db.banpoIsu.createIndex({loc: "2dsphere"})
```

### index 확인
```
db.banpoIsu.getIndexes()
```

### Query

#### 주공아파트단지 내 학교 (주공아파트단지 내에 있는 모든 것)
```
db.banpoIsu.find( {loc: {$geoWithin: {$geometry: {"type":"Polygon", "coordinates":[[[126.980648, 37.503960], [126.987207, 37.498678], [126.995447, 37.501816], [126.991722, 37.506104], [126.980648, 37.503960]]]}}}})
```
{ "_id" : "PG1", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.980648, 37.50396 ], [ 126.987207, 37.498678 ], [ 126.995447, 37.501816 ], [ 126.991722, 37.506104 ], [ 126.980648, 37.50396 ] ] ] }, "pos_name" : { "name" : "주공아파트단지" } }
{ "_id" : "P2", "loc" : { "type" : "Point", "coordinates" : [ 126.991042, 37.503013 ] }, "sname" : { "name" : "반포초등학교" } }
{ "_id" : "P1", "loc" : { "type" : "Point", "coordinates" : [ 126.993271, 37.502325 ] }, "sname" : { "name" : "세화여자고등학교" } }
{ "_id" : "P3", "loc" : { "type" : "Point", "coordinates" : [ 126.992056, 37.502933 ] }, "sname" : { "name" : "반포중학교" } }

#### 주공아파트단지와 교차되는 것들
```
 db.banpoIsu.find( {loc: {$geoIntersects: {$geometry: {"type":"Polygon", "coordinates":[[[126.980648, 37.503960], [126.987207, 37.498678], [126.995447, 37.501816], [126.991722, 37.506104], [126.980648, 37.503960]]]}}}})
```
{ "_id" : "PG1", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.980648, 37.50396 ], [ 126.987207, 37.498678 ], [ 126.995447, 37.501816 ], [ 126.991722, 37.506104 ], [ 126.980648, 37.50396 ] ] ] }, "pos_name" : { "name" : "주공아파트단지" } }<br>
{ "_id" : "L1", "loc" : { "type" : "LineString", "coordinates" : [ [ 126.976027, 37.50315 ], [ 126.987243, 37.501348 ], [ 126.995946, 37.503433 ] ] }, "pos_name" : [ { "station1" : "동작역 9호선" }, { "station2" : "구반포역" }, { "station3" : "신반포역" } ] }<br>
{ "_id" : "P2", "loc" : { "type" : "Point", "coordinates" : [ 126.991042, 37.503013 ] }, "sname" : { "name" : "반포초등학교" } }<br> 
{ "_id" : "P1", "loc" : { "type" : "Point", "coordinates" : [ 126.993271, 37.502325 ] }, "sname" : { "name" : "세화여자고등학교" } }<br>
{ "_id" : "P3", "loc" : { "type" : "Point", "coordinates" : [ 126.992056, 37.502933 ] }, "sname" : { "name" : "반포중학교" } }

#### 현충원을 지나는 지하철 (현충원과 교차되는 모든 것)
```
db.banpoIsu.find( {loc: {$geoIntersects: {$geometry: {"type":"Polygon", "coordinates":[[[ 126.972799, 37.505547 ], [ 126.982321, 37.500664 ], [ 126.97258, 37.493246 ], [ 126.963012, 37.493222 ], [ 126.959634, 37.498386 ], [ 126.972799, 37.505547 ]]]}}}})
```
{ "_id" : "PG2", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.972799, 37.505547 ], [ 126.982321, 37.500664 ], [ 126.97258, 37.493246 ], [ 126.963012, 37.493222 ], [ 126.959634, 37.498386 ], [ 126.972799, 37.505547 ] ] ] }, "pos_name" : { "name" : "현충원" } }<br>
{ "_id" : "L1", "loc" : { "type" : "LineString", "coordinates" : [ [ 126.976027, 37.50315 ], [ 126.987243, 37.501348 ], [ 126.995946, 37.503433 ] ] }, "pos_name" : [ { "station1" : "동작역 9호선" }, { "station2" : "구반포역" }, { "station3" : "신반포역" } ] }<br>
{ "_id" : "L2", "loc" : { "type" : "LineString", "coordinates" : [ [ 126.981697, 37.477007 ], [ 126.98223, 37.4875 ], [ 126.980368, 37.502891 ] ] }, "pos_name" : [ { "station1" : "사당역" }, { "station2" : "이수역" }, { "station3" : "동작역 4호선" } ] }

#### 이수번화가 내 카페 (이수번화가 내에 있는 모든 것)
```
db.banpoIsu.find( {loc: {$geoWithin: {$geometry: {"type":"Polygon", "coordinates" : [[[126.983082, 37.487922], [126.979808, 37.488147], [126.980003, 37.487476], [126.980456, 37.487427], [126.980457, 37.486703], [126.982998, 37.486419], [126.983082, 37.487922]]]}}}})
```
{ "_id" : "P4", "loc" : { "type" : "Point", "coordinates" : [ 126.98188, 37.487569 ] }, "cname" : { "name" : "할리스커피" } }<br>
{ "_id" : "P5", "loc" : { "type" : "Point", "coordinates" : [ 126.980208, 37.487616 ] }, "cname" : { "name" : "카페베네" } }<br>
{ "_id" : "PG3", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.983082, 37.487922 ], [ 126.979808, 37.488147 ], [ 126.980003, 37.487476 ], [ 126.980456, 37.487427 ], [ 126.980457, 37.486703 ], [ 126.982998, 37.486419 ], [ 126.983082, 37.487922 ] ] ] }, "pos_name" : { "name" : "이수번화가" } }<br>

#### 4호선과 교차되는 것들
```
 db.banpoIsu.find( {loc: {$geoIntersects: {$geometry: {"type":"LineString", "coordinates":[[ 126.981697, 37.477007 ], [ 126.98223, 37.4875 ], [ 126.980368, 37.502891 ]]}}}})
```
{ "_id" : "L2", "loc" : { "type" : "LineString", "coordinates" : [ [ 126.981697, 37.477007 ], [ 126.98223, 37.4875 ], [ 126.980368, 37.502891 ] ] }, "pos_name" : [ { "station1" : "사당역" }, { "station2" : "이수역" }, { "station3" : "동작역 4호선" } ] }<br>
{ "_id" : "PG2", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.972799, 37.505547 ], [ 126.982321, 37.500664 ], [ 126.97258, 37.493246 ], [ 126.963012, 37.493222 ], [ 126.959634, 37.498386 ], [ 126.972799, 37.505547 ] ] ] }, "pos_name" : { "name" : "현충원" } }<br>
{ "_id" : "L1", "loc" : { "type" : "LineString", "coordinates" : [ [ 126.976027, 37.50315 ], [ 126.987243, 37.501348 ], [ 126.995946, 37.503433 ] ] }, "pos_name" : [ { "station1" : "동작역 9호선" }, { "station2" : "구반포역" }, { "station3" : "신반포역" } ] }<br>
{ "_id" : "PG3", "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.983082, 37.487922 ], [ 126.979808, 37.488147 ], [ 126.980003, 37.487476 ], [ 126.980456, 37.487427 ], [ 126.980457, 37.486703 ], [ 126.982998, 37.486419 ], [ 126.983082, 37.487922 ] ] ] }, "pos_name" : { "name" : "이수번화가" } }<br>

#### 태평백화점(=insert하지 않은 Point) 500m 내에 있는 것들
```
 db.banpoIsu.find({loc: {$nearSphere: {$geometry: {"type":"Point", "coordinates":[126.981666, 37.486825]}, $maxDistance:500}}})
```
{ "_id" : ObjectId("5ec40566603ce975c7114268"), "loc" : { "type" : "Polygon", "coordinates" : [ [ [ 126.983082, 37.487922 ], [ 126.979808, 37.488147 ], [ 126.980003, 37.487476 ], [ 126.980456, 37.487427 ], [ 126.980457, 37.486703 ], [ 126.982998, 37.486419 ], [ 126.983082, 37.487922 ] ] ] }, "pos_name" : { "name" : "이수번화가" } }<br>
{ "_id" : ObjectId("5ec37e18af65617bb132d80f"), "loc" : { "type" : "LineString", "coordinates" : [ [ 126.981697, 37.477007 ], [ 126.98223, 37.4875 ], [ 126.980368, 37.502891 ] ] }, "pos_name" : [ { "station1" : "사당역" }, { "station2" : "이수역" }, { "station3" : "동작역 4호선" } ] }<br>
{ "_id" : ObjectId("5ec37e18af65617bb132d80c"), "loc" : { "type" : "Point", "coordinates" : [ 126.98188, 37.487569 ] }, "cname" : { "name" : "할리스커피" } }<br>
{ "_id" : ObjectId("5ec37e18af65617bb132d80e"), "loc" : { "type" : "Point", "coordinates" : [ 126.980208, 37.487616 ] }, "cname" : { "name" : "카페베네" } }<br>