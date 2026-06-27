#### 3.1.1 `rgen`

##### Description

- `GET` : 在控制器中获取远程一般信息。

##### path-parameter

```python
GET /project/rgen
```

##### response-body

###### 1) Mode
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : 手动 <br> `1` : 手动, 系统设置 <br>`3` : 自动, 1周期 <br> `4` : 自动, 继续 (循环)|`int`|手动/自动模式|
|`enable_state`|`0` Byte(`LSB`) : 电机开启 (0: 开 / 1: 关 / 2: 忙)<br> `1` Byte : TP 启用 (死区) 开关 (0: 关 / 1: 开)<br>`2` Byte : 机器锁 (0: 关 / 1: 开)<br>`3` Byte : 枪锁 (0: 关 / 1: 开)<br>`4` Byte : 枪 (0: 关 / 1: 开)|`int`||
|`is_playback`|`0` : 暂停 <br>`1` : 播放|`int`||
|`is_remote_mode`|`0`: 错误 <br> `1`: 正确|`int`|是否为远程模式|
|`is_ext_start`|`0`: 错误 <br> `1`: 正确|`int`|是否为外部启动|
|`is_ext_prog_sel`|`0`: 错误 <br> `1`: 正确|`int`|是否选择外部程序|

<br>

###### 2) current program counter
在手动模式或自动模式下，教导挂件 JOB 面板上的条形光标所在位置。这是当前正在执行的语句或编辑的目标位置。
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|当前程序编号|
|`cur_step_no`|`int`|当前步骤编号|
|`cur_func_no`|`int`|当前功能编号|

<br>

###### 3) moving program counter
这是机器人在回放期间移动的目标步骤。
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|移动程序编号|
|`mov_step_no`|`int`|移动步骤编号|
|`mov_func_no`|`int`|移动功能编号|

<br>

###### 4) Speed
|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|手动模式 jog 速度级别 (1~8)|
|`manual_spd_max`|`int`|手动模式最大速度 (mm/sec)|
|`auto_spd`|`int`|自动模式回放速度 (%)|
|`jog_inch_status`|`int`|jog 细微移动状态 (0:关/ 1:开)|
|`step_execute_unit_status`|`int`|StepFWD 执行单元 (运行到)<br>0: 命令 <br>1: 步骤<br>2: 结束 |
|`cont_path`|`int`|连续运动模式 (0~2)|

<br>

##### Example
Python 脚本示例

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