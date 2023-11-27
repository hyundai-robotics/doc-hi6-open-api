# 3.1.1 search

## 설명

`search`

- `GET` : 지정한 필터 조건으로 이벤트 이력(event log)를 열람합니다.  

## query-parameter

- `n_item` : 요청 event 개수 (default=100)
- `cat_p` : 요청 범주 필터 (category positive). 각 타입을 의미하는 글자를 쉼표(,)로 결합하여 지정합니다.
            (cat_p=E,W,N)
  - `E` : 에러 (Error)
  - `W` : 경고 (Warning)
  - `N` : 알림 (Notice)
  - `S` : 기동/정지 (Start/Stop)
  - `O` : 사용자 조작 (user's Operation)
  - `I` : I/O, 릴레이 값 (I/O, relay value)
  - `P` : 주기적 상태 기록 (Periodic state)
  - `H` : 실행 이력 (History)
  - `C` : 콘솔 출력 (Console out)
  - `M` : 기타 (Miscellany)
- `id_min` : 최소 id 필터. (optional)
  - 모든 이벤트는 유일한 이벤트 ID(eid)를 가지고 있습니다. (0~)  
    기존에 수신한 이벤트들의 id 중 최대값에 1을 더해 `id_min`에 지정하여 이력 요청을 하면,
    기존에 이미 수신한 이벤트들은 제외하고, 새로 발생한 이력만 얻을 수 있습니다.  
  - 단, 제어기 내의 이벤트 id는 최대값(0xffffffffffffffff)이 되면, 다시 0부터 생성됩니다.
    필터링은 이러한 상황까지 고려하여 적절히 적용됩니다.
    예를들어, id_min이 0xfffffffffffffffa 인 경우, 0, 1, 2 같은 id를 갖는 이벤트들을 필터 아웃되지 않고 응답에 포함됩니다.
- `id_max` : 최대 id 필터. (optional)
- `ts_min` : 최소 timestamp 필터. (optional)
  - 년/월/일 시:분:초.밀리초 형식. e.g. 2023/11/20 18:50:30.955
- `ts_max` : 최대 timestamp 필터. (optional)
  - 년/월/일 시:분:초.밀리초 형식. e.g. 2023/11/20 18:50:30.955

## response-body

- id : 이벤트 ID (event ID)
- ts : timestamp
- cat : 이벤트 범주 (event category)
- code : 이벤트 코드번호
- aux : 이벤트 보조정보 (event auxiliary info.). 최대 280자입니다.
  - 에러와 경고, 기동/정지의 경우에는 스냅샷(snapshot) 정보를 담습니다.
  - 


```json
{ "id" : 19964, "ts" : "2023/11/20 15:53:11.275", "cat" : "E", "code" : "11,0,0", "aux" : "{ 'pc' : '20/3/1', 'j1' : 18.525, 'j2' : 105.000, 'j3' : -2.577, 'j4' : -14.432, 'j5' : -0.776, 'j6' : 0.314, 'sin' : '00 01 00 00 00 00 00 00', 'sout' : '05 08 06 00 00 00 00 01', 'din' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0', 'dout' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0' }" }
{ "id" : 18314, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(    976)Power saving = on " }
{ "id" : 18313, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(=Stamp=)[2023/11/20 15:05:33](+299996445us) " }
{ "id" : 18312, "ts" : "2023/11/20 15:05:33.787", "cat" : "N", "code" : "5", "aux" : "{ 'pc' : '20/3/1' }" }
{ "id" : 18267, "ts" : "2023/11/20 15:00:33.791", "cat" : "H", "code" : "hist", "aux" : "(   2001)    .end ;(P20/S3/F1) " }
{ "id" : 18266, "ts" : "2023/11/20 15:00:33.789", "cat" : "H", "code" : "hist", "aux" : "( 738785)S3  .move P,spd=500mm/sec,accu=4,tool=0 " }
```
