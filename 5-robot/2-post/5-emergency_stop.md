## 5.2.5 `emergency_stop`

### 설명

- 지원 버전 : `60.30-00` &uparrow;
- `POST` : 비상 정지를 실행합니다.  
- 비상정지 버튼을 눌렀을 때와 동일한 감속 프로파일이 적용됩니다.
- API 호출 시, 네트워크 지연(Latency) 또는 요청 처리 시간 때문에 물리적 버튼보다 늦게 반응할 가능성이 있습니다.


### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/emergency_stop
```

### request-body
```python 
{}
```

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found
2) response-body
	- v60.30 이하
		<div style="width: fit-content;">

		```json
		{"err_code": 200}
		```
		</div>
	- v60.32 이상
		<div style="width: fit-content;">

		```json
		{"_type": "JObject"}
		```
		</div>

### 사용 예

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_emergency_stop())

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>
