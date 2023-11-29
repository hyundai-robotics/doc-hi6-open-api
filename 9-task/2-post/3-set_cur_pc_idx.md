## 9.2.3 `set_cur_pc_idx`

### 설명

`set_cur_pc_idx`

- `POST` : 현재 커서를 index 라인에 위치 시키는 함수

### path-parameter

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

### request-body
```json
{
  "idx": 1
}
```

### 사용 예

<blockquote>

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
  "idx": 2
}
```

</blockquote>

Python Script

```python
# test.py
import requests

def set_cur_pc_idx() -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/set_cur_pc_idx"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"idx": 1}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {set_cur_pc_idx()}")
```
```sh
$python test.py 
response 200 # + TP 상 커서 위치 변경 됨
```