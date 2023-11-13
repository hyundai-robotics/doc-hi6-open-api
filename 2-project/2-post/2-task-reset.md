# 2.2.2 task/reset

## 설명

- POST : 태스크에 대해 리셋을 수행합니다. (R.. 0 ENTER 와 같은 동작)

## method path

```python
POST /project/context/tasks/reset  ; 모든 태스크에 대해 리셋을 수행.
POST /project/context/tasks[{task번호}]/reset  ; 지정한 태스크에 대해 리셋을 수행.
```

## 사용 예

- 0번 태스크 리셋 하기.

```python
request url:
GET /project/context/tasks[0]/reset
