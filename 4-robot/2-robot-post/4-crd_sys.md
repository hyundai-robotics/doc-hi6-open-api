# 4.2.4 crd_sys

## 설명

- POST : 현재 조그(jog) 좌표계를 설정합니다.

## path-parameter

```python
POST /project/robot/crd_sys
```

## request-body

- val : 조그 좌표계
  - -1 : 다음 좌표계로 전환. 가령 현재가 1(직교)이면 2(사용자)로 변경됨.
  - 0 : 축
  - 1 : 직교
  - 2 : 사용자
  - 3 : 툴
