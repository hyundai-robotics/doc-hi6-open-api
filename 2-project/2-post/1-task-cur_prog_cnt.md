# 2.2.1 task/cur_prog_cnt

## 설명

cur_prog_cnt (current program counter)

- POST : 태스크의 현재 프로그램 카운터를 설정합니다.

## method path

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

## request-body

- pno : 프로그램 번호 (-1이면 현재 번호 유지)
- sno : 스텝 번호 (-1이면 현재 번호 유지)
- fno : 펑션 번호 (-1이면 현재 번호 유지)
- ext_sel :
  - 0 : 내부선택(원격모드에선 금지됨)
  - 1 : 외부선택(원격모드에서만 허용됨)

## response-body

- sno_new : 새로 이동한 스텝 번호
- fno_new : 새로 이동한 펑션 번호
- ln_new : 새로 이동한 라인번호 (프로그램 헤더가 0, 첫 명령문이 1)
