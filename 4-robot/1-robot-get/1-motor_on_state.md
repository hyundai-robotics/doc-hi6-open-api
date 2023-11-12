# 3.1 motor_on_state

## 설명

motor_on_state

- GET : 모터 온 상태를 얻습니다.

## method path

```python
GET /project/robot/motor_on_state
```

## response-body

- val :
  - 0 : on
  - 1 : busy (상태 전환 중)
  - 2 : off
