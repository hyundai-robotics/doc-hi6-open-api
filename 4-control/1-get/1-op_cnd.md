## 4.1.1 `op_cnd`

### Description

`op_cnd` (operation condition)

- `GET` : Obtain the condition setting value.

### path-parameter

```python
GET /project/control/op_cnd
```

### response-body

- [Condition Setting parameter](../../99-schema/op_cnd.md)

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

Python Script Example

```python
# test.py
import requests

def get_operation_condition() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/control/op_cnd"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_operation_condition())
```
```sh
$python test.py
{'step_goback_max_spd': 130, 'playback_mode': 2, '_type': 'CondGrp', 'step_go_func_ex': 0, 'robot_lock': 1, 'playback_spd_rate': 80, 'intp_base': 1, 'ucrd_num': 19, 'path_recov_confirm': 0, 'func_reexe_on_trace': 2, 'plc_mode': 0}
```