## 9.2.5 `assign_var_json`

### 설명

`assign_var_json`

- `POST` : 현재 태스크 구문의 변수를 재지정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

### request-body

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

### 사용 예

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

상기 job 파일을 수행하여 태스크 상 지역 변수 a 가 선언된 상태일 경우

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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

def assign_var_json(var_name: str, scope = None, var_json: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_json"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {
                         "name" : f"{var_name}",
                         "scope": f"{scope}",
                         "json" : f"{var_json}",
                         "save" : "true"
                       }

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"before: {post_read_var('a', 'local')}")
print(f"""response: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
before: 1234
response: 200
after: {'_type': 'JObject', 'test': 10}
```