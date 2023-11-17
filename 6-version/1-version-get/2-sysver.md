# 6.2 sysver

## 설명

- GET : 로봇제어기 시스템의 소프트웨어 버전을 얻습니다.

## path-parameter

```python
GET /versions/sysver
```

## response-body

- modules : 모듈 버전 정보의 배열
  - 모듈 버전 정보 :
    - name : 모듈명
    - ver : 버전번호
    - build-date : 빌드 날짜
    - build-time : 빌드 시간
    - commit-id : 소스코드의 커밋 ID

## 사용 예

```python
request url:
GET /versions/sysver

response-body:
{
    "modules" : [
        {
???
        }
    ] 
}
