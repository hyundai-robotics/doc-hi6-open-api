# 3.2.1 `op_cnd`

## 설명

`op_cnd` (operation condition)

- `PUT` : 로봇의 조건설정 값을 변경합니다.

## path-parameter

```python
PUT /project/control/op_cnd
```

## request-body

- [포즈](/99-schema/op_cnd.md)


## 사용 예

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "_type": "CondGrp",
    "playback_mode": 2,
    "step_goback_max_spd": 130,
    "step_go_func_ex": 0,
    "func_reexe_on_trace": 2,
    "path_recov_confirm": 0,
    "playback_spd_rate": 80,
    "robot_lock": 1,
    "intp_base": 1,
    "ucrd_num": 19,
    "plc_mode": 4
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
                       "_type": "CondGrp",
                       "playback_mode": 2,
                       "step_goback_max_spd": 190,
                       "step_go_func_ex": 0,
                       "func_reexe_on_trace": 2,
                       "path_recov_confirm": 0,
                       "playback_spd_rate": 80,
                       "robot_lock": 1,
                       "intp_base": 1,
                       "ucrd_num": 19,
                       "plc_mode": 4 
                     }

    response = requests.put(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {put_op_cnd()}")
```
```sh
$python test.py
response: 200 
```