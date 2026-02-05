### 4.1.1 `op_cnd`

#### 설명

- `GET` : 조건설정 값을 얻습니다.

#### path-parameter

<div style="width: fit-content;">

```python
GET /project/control/op_cnd
```

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [조건설정 파라미터](../../99-schema/op_cnd.md)

		```json
		{
			"_type": "CondGrp",
			"step_goback_max_spd": 200,
			"playback_mode": 1,
			"step_go_func_ex": 1,
			"robot_lock": 0,
			"playback_spd_rate": 100,
			"intp_base": 0,
			"ucrd_num": 0,
			"path_recov_confirm": 2,
			"func_reexe_on_trace": 1,
			"plc_mode": 1
		}
		```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_operation_condition() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/control/op_cnd"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_operation_condition())
```
```sh
$python test.py
(200, {'plc_mode': 1, 'step_go_func_ex': 1, '_type': 'CondGrp', 'intp_base': 0, 'playback_spd_rate': 100, 'step_goback_max_spd': 250, 'robot_lock': 0, 'func_reexe_on_trace': 1, 'ucrd_num': 0, 'playback_mode': 1, 'path_recov_confirm': 2})
```
</div>
