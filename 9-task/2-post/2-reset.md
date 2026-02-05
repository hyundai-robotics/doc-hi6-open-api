#### 9.2.2 `task/reset`

##### Description

- `POST` : Perform a reset on the task.  
- It operates the same as using [RCode 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/en-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}). 
  - <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;"> Any other code is not intended for operation </span>

##### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

##### request-body

```json
{"code": 0}
```

##### Example

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
