### 4.3.1 `op_cnd`

#### 설명

- `PUT` : 로봇의 `조건설정값`을 변경합니다.
- TP 에서 조건 설정 창을 열고 해당 메서드를 요청한 경우, 창을 닫았다 다시 열어야 값이 반영됩니다.

#### path-parameter

<div style="width: fit-content;">

```python
PUT /project/control/op_cnd
```

#### request-body

- [조건설정 파라미터](../../99-schema/op_cnd.md)

#### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - {'_text': ''}

#### 사용 예

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}

response-body:
{'_text': ''}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def put_op_cnd() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/op_cnd"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "playback_mode": 2,
        "step_goback_max_spd": 130,
        "step_go_func_ex": 0,
        "func_reexe_on_trace": 1,
        "path_recov_confirm": 0,
        "playback_spd_rate": 80,
        "robot_lock": 0,
        "intp_base": 0,
        "ucrd_num": 0,
        "plc_mode": 0,
    }

    response = requests.put(url=base_url + path_parameter, headers=head, json=body)
    return response


print(put_op_cnd())
```
```sh
$python test.py
(200, {'_text': ''})
```
</div>
