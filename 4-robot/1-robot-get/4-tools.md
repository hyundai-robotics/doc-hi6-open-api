# 3.4 tools

## 설명

tools

- GET : 로봇의 모든 툴 정보 얻기. T0~T31까지의 툴 중 존재하는 툴만 얻습니다.

## method path

```python
GET /project/robot/tools
```

## response-body

- t_0 : [툴 데이터](/7-schema/tool_data.md)
- t_1 : 툴 데이터
- t_2 : 툴 데이터  
...
- t_31 : 툴 데이터

## 사용 예

툴 0과 툴 31만 존재하는 시스템의 사례.

```python
request url:
GET /project/robot/tools

response-body:
{
???
}
```