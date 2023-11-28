## 8.2.5 `assign_var_json`

### 설명

`assign_var_json`

- `POST` : 현재 태스크 구문의 변수를 재지정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

### request-body
```json
{
    "name": "a",
    "expr": 12
}
```

### 사용 예

<blockquote>

```text
Hyundai Robot Job File;
    a = 1234
    end
```

상기 job 파일을 수행하는 상황일 때

```python
request url:
POST /project/context/tasks[0]/assign_var_json

request-body
{
    "name": "a",
    "json": 1
}
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_cur_local_var() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/cur_local_vars"

    response = requests.get(url = base_url + path_parameter)

    return response.json()

def assign_var_json(x: int = 1) -> int:
    base_url         = "http://127.0.0.1:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_json"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"name": "a", "json": x}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(get_cur_local_var())
print(f"response: {assign_var_json(321)}")
print(get_cur_local_var())
```
```sh
$python test.py 
{'_type': 'JObject', 'a': 123, 'b': 5678, 'c': 5432}
response: 200
{'_type': 'JObject', 'a': 321, 'b': 5678, 'c': 5432}
```