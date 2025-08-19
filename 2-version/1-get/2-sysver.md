## 2.1.2 sysver

### 설명

- `GET` : 로봇제어기 시스템의 소프트웨어 버전을 얻습니다.

### path-parameter

<div style="width: fit-content;">

```python
GET /versions/sysver
```
</div>

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - modules : 모듈 버전 정보의 배열
     - `name` : 모듈명(`com` : 로봇 제어기, `tp` : 티칭 펜던트)
      - `ver` : 버전번호
      - `build-date` : 빌드 날짜
      - `build-time` : 빌드 시간
      - `commit-id` : 소스코드의 커밋 ID

### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /versions/sysver

response:
(200,{"modules" : [{"build-date": ..., "build-time": ..., "ver": ...}]})
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_sysver() -> dict:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/versions/sysver"
    response = requests.get(url=base_url + path_parameter)

    return response


print(get_sysver())

```
```sh
$python test.py
(200, {'modules': [{'build-date': 'Aug 13 2025', 'build-time': '12:50:21', 'commit-id': 'a11c02406c', 'name': 'com', 'sub-modules': [{'build-date': '', 'build-time': '', 'commit-id': '', 'name': 'fbr', 'ver': '2.1-1(1.1-3)'}], 'ver': '61.01-01.dev'}, {'build-date': 'Aug 13 2025
', 'build-time': '12:59:33', 'commit-id': 'fadf82cbb9', 'name': 'tp', 'ver': '61.01-01.dev'}]})
```
</div>