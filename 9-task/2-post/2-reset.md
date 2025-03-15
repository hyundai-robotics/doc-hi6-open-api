<link rel="stylesheet" href="../../_assets/style.css">

## 9.2.2 `task/reset`

<div style="width: fit-content;">

### 설명

- `POST`: 스텝 카운터를 초기화하여 STEP0으로 이동합니다.
- [R코드 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/korean-tp630/8-r-code/1-use-r-code)를 활용합니다. 
  
	<div caution> <span u>R코드 0</span> 이외의 코드는 예정된 동작이 아닙니다. </div>

### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

### request-body

```json
{"code": 0}
```

### 사용 예

```python
request url:
POST /project/service/r_code/execute

request-body:
{
    "code":0
}
```

Python Script

```python
import requests


def post_rcode_0() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 0}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response.status_code


print(f"response: {post_rcode_0()}")

```
```sh
$python test.py
response: 200
```

</div>