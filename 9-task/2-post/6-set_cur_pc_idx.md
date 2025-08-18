## 9.2.6 `set_cur_pc_idx`

<div style="width: fit-content;">

### 설명

- `POST` : 현재 커서를 index 라인에 위치 시키는 함수

### path-parameter

```python
POST /project/context/tasks[{task index}]/set_cur_pc_idx
```

### request-body
```json
{
  "idx": 1
}
```
### status code

- 200 : OK
- 400 : Bad Request
- 403 : Forbidden
  - 상기 필요 조건 불충족
- 404 : Not Found

### error code

- -38501 : 재생 중인 task 가 있을 때는 적용이 되지 않습니다.

### 사용 예

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
  "idx": 2
}
```


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
</div>