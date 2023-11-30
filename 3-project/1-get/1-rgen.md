## 3.1.1 `rgen`

### Description

`rgen` (remote general status)

- `GET` : Obtain general information set in the controller.

### path-parameter

```python
GET /project/rgen
```

### response-body

#### 1) Mode
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : manual <br> `1` : manual, system settings <br>`3` : auto, 1-cycle <br> `4` : auto, continue (cycle)|`int`|manual/auto mode|
|`enable_state`|`0` Byte(`LSB`) : Motor ON (0: On / 1: Off / 2: Busy) <br> `1` Byte : TP Enable (deadman) Switch (0: OFF / 1: ON)<br>`2` Byte : Machine Lock (0: OFF / 1: ON)<br>`3` Byte : gun Lock (0: OFF / 1: ON)<br>`4` Byte : gun (0: OFF / 1: ON)|`int`||
|`is_playback`|`0` : Pause <br>`1` : play|`int`||
|`is_remote_mode`|`0`: False <br> `1`: True|`int`|Remote mode or not|
|`is_ext_start`|`0`: False <br> `1`: True|`int`|External start-up or not|
|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|Whether to select an external program|

<br>

#### 2) current program counter
This is the point where the bar cursor on the teach pendant JOB panel is located in manual mode or automatic mode. This is the currently executing statement or the target location for editing.
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|current program number|
|`cur_step_no`|`int`|current step number|
|`cur_func_no`|`int`|current function number|

<br>

#### 3) moving program counter

This is the target step the robot is moving during playback.
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|moving program number|
|`mov_step_no`|`int`|moving step number|
|`mov_func_no`|`int`|moving function number|

<br>

#### 4) Speed

|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|Manual mode jog speed level (1~8)|
|`manual_spd_max`|`int`|Manual mode maximum speed (mm/sec)|
|`auto_spd`|`int`|Auto mode playback speed (%)|
|`jog_inch_status`|`int`|jog inching state (0:OFF/ 1:ON)|
|`step_execute_unit_status`|`int`|StepFWD execution unit (run to)<br>0: Cmd <br>1: Step<br>2: End |
|`cont_path`|`int`|continuous motion mode (0~2)|

<br>

### Example
Python Script Example

```python
import requests

def get_is_remote_mode() -> bool:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/rgen'    
    
    response = requests.get(url = base_url + path_parameter).json()    

    print(f"is remote mode? {response['is_remote_mode']}")    
    
    return response['is_remote_mode']

get_is_remote_mode()
```
```sh
$python test.py
is remote mode? 0
```
