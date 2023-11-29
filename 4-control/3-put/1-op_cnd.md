## 4.3.1 `op_cnd`

### 설명

`op_cnd` (operation condition)

- `PUT` : 로봇의 조건설정 값을 변경합니다.
- TP 에서 조건 설정 창을 열고 해당 메서드를 요청한 경우, 창을 닫았다 다시 열어야 값이 반영됩니다.

### path-parameter

```python
PUT /project/control/op_cnd
```

### request-body

- [조건설정 파라미터](../../99-schema/op_cnd.md)


### 사용 예

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}
```

Python Script 예시

```python
# test.py
import requests 

def put_op_cnd() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/op_cnd'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = { 
                          "playback_mode": 1,
                          "step_goback_max_spd": 130,
                          "ucrd_num": 2
                     }

    response = requests.put(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {put_op_cnd()}")
```
```sh
$python test.py
response: 200 
```