# cur_prog_cnt

## 설명
태스크의 현재 프로그램 카운터를 설정합니다.

## request body
|key|type|description|
|:---|:---|:---|
|pno|int|프로그램 번호 (-1이면 현재 번호 유지)|
|sno|int|스텝 번호 (-1이면 현재 번호 유지)|
|fno|int|펑션 번호 (-1이면 현재 번호 유지)|
|ext_sel|int|0 : 내부선택(원격모드에선 금지됨) <br> 1 : 외부선택(원격모드에서만 허용됨)|

## response body
|key|type|description|
|:---|:---|:---|
|sno_new|int|새로 이동한 스텝 번호|
|fno_new|int|새로 이동한 펑션 번호|
|ln_new|int|새로 이동한 라인번호 (프로그램 헤더가 0, 첫 명령문이 1)|