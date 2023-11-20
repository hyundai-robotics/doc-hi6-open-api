# 3.2.1 `op_cnd`

## 설명

`op_cnd` (`op`eration `c`o`nd`ition)

- `POST` : 로봇의 조건설정 값을 변경합니다.

## path-parameter

```python
POST /project/control/op_cnd
```

## request-body

- [포즈](/7-schema/op_cnd.md)


## 사용 예

```python
request url:
POST /project/control/op_cnd

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
<details><summary>Python Script 예시</summary>

```python
# test.py
import requests 

def post_op_cnd() -> int:
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

    response = requests.post(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {post_op_cnd()}")
```
```sh
$python test.py
response: 200 
```
</details>