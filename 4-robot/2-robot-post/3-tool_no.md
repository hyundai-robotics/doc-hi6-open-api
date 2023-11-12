# 3.4 tool_no

## 설명

- POST : 현재 툴 번호를 설정합니다.

## method path

```python
POST /project/robot/tool_no
```

## request-body

- val : 툴 번호
  - 로봇 툴이면, 0~31
  - 정치 툴이면, 0~3
