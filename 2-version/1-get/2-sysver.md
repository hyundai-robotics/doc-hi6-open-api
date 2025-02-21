## 2.1.2 sysver

### 설명

- `GET` : 로봇제어기 시스템의 소프트웨어 버전을 얻습니다.

### path-parameter

<div style="width: fit-content;">

```python
GET /versions/sysver
```
</div>

### response-body

modules : 모듈 버전 정보의 배열
  - 모듈 버전 정보 :
    - `name` : 모듈명
        - `com` : 로봇 제어기
        - `tp` : 티칭 펜던트
    - `ver` : 버전번호
    - `build-date` : 빌드 날짜
    - `build-time` : 빌드 시간
    - `commit-id` : 소스코드의 커밋 ID

### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /versions/sysver

response-body:
{
    "modules" : [
        {
            "build-date": ...
            "build-time": ...
                 ...
            "ver": ...
        }
    ] 
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests

def get_sysver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/versions/sysver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_sysver())
```
```sh
$python test.py
{'modules': [{'build-date': 'Jan 00 2000', 'build-time': '00:00:00' ...
```
</div>