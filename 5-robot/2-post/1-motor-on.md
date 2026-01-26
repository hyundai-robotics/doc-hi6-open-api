## 5.2.1 `motor_on`

- <b style="color:orange"> `motor_off` API 는 [v60.30-00](../../1-release-note/60-30.md)부터 지원되지 않습니다.</b>

<div style="width: fit-content;">
### 설명

- `POST` : 모터 ON을 수행합니다.

### path-parameter


```python
POST /project/robot/motor_on
```

### request-body

```json
{}
```

### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 원격모드가 아닌 상태에서 요청한 경우(v60.30-09 부터 적용)
   - 404 : Not Found

2) response-body
	```json
	{ "_type": "JObject"}
	```

3) error code
   - -38500: 원격 모드가 아닌 상태로 해당 api 요청

### 사용 예

```python
POST /project/robot/motor_on

request-body:
{}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
import requests


def post_motor_on() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/motor_on"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_motor_on())

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```

</div>
