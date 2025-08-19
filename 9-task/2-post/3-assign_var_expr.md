## 9.2.3 `assign_var_expr`

<div style="width: fit-content;">

### 설명

- `POST` : 태스크 구문의 변수를 재지정합니다.

### path-parameter

```python
POST /project/context/tasks[{task index}]/assign_var_expr
```

### request-body

- `name` : 변수명
- `expr` : 변수에 대입할 수식
- `save` : 저장 유무 (true/false). 변수 파일에 해당 데이터를 저장하기 위함입니다.
- `scope` : 해당 변수의 유효 스코프 설정
	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

### response

1) status code
	- 200 : OK
	- 400 : Bad Request
	- 403 : Forbidden
	- 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>



### 사용 예

현재 태스크에 지역 변수 a 가 선언된 상태인 경우

```python
request url:
POST /project/context/tasks[0]/assign_var_expr

request-body
{
    "name" : "a",
    "scope": "local",
    "expr" : "465 + 312",
    "save" : "true"
}
```


Python Script 예시

```python
# test.py
import requests


def post_read_var(var: str, scope=None) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/solve_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"expr": f"{var}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


def assign_var_expr(var: str, scope=None, expression: str = "") -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/assign_var_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"name": f"{var}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret1 = post_read_var("a", "local")
ret2 = assign_var_expr("a", "local", "465 + 312")
ret3 = post_read_var("a", "local")

try:
    print((ret1.status_code, ret1.json()))
    print((ret2.status_code, ret2.json()))
    print((ret3.status_code, ret3.json()))
except:
    print(ret1)
    print(ret2)
    print(ret3)
```
```sh
$python test.py
(200, 0)
(200, {'_type': 'JObject'})
(200, 777)
```

</div>