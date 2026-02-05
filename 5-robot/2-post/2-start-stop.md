### 5.2.2 `start / stop`

#### 설명

- `POST` : 로봇 기동(start)과 로봇 정지(stop)를 수행합니다.

#### path-parameter


<div style="width: fit-content;">

```python
POST /project/robot/start
POST /project/robot/stop
```

#### request-body

```json
{}
```

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - start 요청 시 원격모드가 아닌 상태에서 요청한 경우(v60.30-07 부터 적용)
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{ "_type": "JObject"}
	```
	</div>


1) error code
   - -38500: 원격 모드가 아닌 상태로 해당 api 요청

#### 사용 예

```python
POST /project/robot/start or /project/robot/stop

request-body:
{}

response-body:
{}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def post_start() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/start"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response

def post_stop() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_start())
print(post_stop())
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```
</div>
