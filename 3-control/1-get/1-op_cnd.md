# 3.1.1 `op_cnd`

## 설명

`op_cnd` (operation condition)

- `GET` : 로봇의 조건설정 값을 얻습니다.

## path-parameter

```python
GET /project/control/op_cnd
```

## response-body

- [로봇 조건설정 파라미터](../../7-schema/op_cnd.md)

<blockquote>

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
</blockquote>

<details><summary>Python Script 예시</summary>

```python
# test.py
import requests

def get_operation_condition() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/control/op_cnd"

    response = requests.get(url=base_url + path_parameter).json()
    print(response)

    return response

get_op_cnd()
```
```sh
$python test.py
{'step_goback_max_spd': 130, 'playback_mode': 2, '_type': 'CondGrp', 'step_go_func_ex': 0, 'robot_lock': 1, 'playback_spd_rate': 80, 'intp_base': 1, 'ucrd_num': 19, 'path_recov_confirm': 0, 'func_reexe_on_trace': 2, 'plc_mode': 0}
```
</details>
