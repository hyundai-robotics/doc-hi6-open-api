### 9.2.5 `release_wait`

<div style="width: fit-content;">

#### 설명

- `POST` : WAIT 을 실행중인 태스크에 대해서 wait 상태를 강제로 해제합니다.
- **<u>필요 조건</u>** : TP > 시스템 > 1: 사용자 환경 > `wait(di/wi) 강제 해제` > `유효` 선택

#### path-parameter

```python
POST /project/context/tasks[{task index}]/release_wait
```

#### request-body

```json
{}
```

#### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - 상기 필요 조건 불충족
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>

3) error code
   - -1442069 : 사용자 환경 설정 오류. 상기 필요 조건을 확인하십시오.


#### 사용 예

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

Python Script 예시

```python
import requests


def post_release_wait() -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/release_wait"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret = post_release_wait()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```

</div>
