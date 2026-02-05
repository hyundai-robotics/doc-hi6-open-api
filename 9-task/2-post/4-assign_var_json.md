### 9.2.4 `assign_var_json`

<div style="width: fit-content;">

#### 설명

- `POST` : 태스크 구문의 변수를 재지정합니다.

#### path-parameter

```python
POST /project/context/tasks[{task index}]/assign_var_json
```

#### request-body

- `name` : 변수명
- `json` : 변수에 대입할 json 형태의 문자열
- `save` : 저장 유무 (true/false). 변수 파일에 해당 데이터를 저장하기 위함입니다.
- `scope` : 해당 변수의 유효 스코프 설정
	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|


	```json
	{
		"name" : "a",
		"scope": "local",
		"json" : "{\"test\": 10}",
		"save" : "true"
	}
	```

#### response

1) status code
	- 200 : OK
	- 400 : Bad Request
	- 403 : Forbidden
	- 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject", ${request-body 에서 요청한 body의 json값}}
	```
	</div>

	e.g. "json" 으로 {"test":10} 을 요청한 경우
	<div style="width: fit-content;">

	```json
	{"_type": "JObject", "test": 10}
	```
	</div>


#### 사용 예


현재 태스크에 지역 변수 a 가 선언된 상태일 경우

```python
request url:
POST /project/context/tasks[0]/assign_var_json

request-body
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```

Python Script 예시

```python
# test.py
import requests


def post_read_var(var_name: str, scope=None) -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/solve_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.json()


def assign_var_json(var_name: str, scope=None, var_json: str = "") -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/assign_var_json"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "name": f"{var_name}",
        "scope": f"{scope}",
        "json": f"{var_json}",
        "save": "true",
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"before: {post_read_var('a', 'local')}")
print(f"""response: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py
before: 777
response: 200
after: {'_type': 'JObject', 'test': 10}
```

</div>
