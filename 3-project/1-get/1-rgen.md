#### 3.1.1 `rgen`

##### 描述

- `GET`: 在控制器中获取远程一般信息。

##### 路径参数

```python
GET /project/rgen
```

##### 响应体

###### 1) 模式
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0`: 手动 <br> `翻译 (1)`: 手动, 系统设置 <br>`翻译 (3)`: 自动, 1循环 <br> ` (4)`: 自动, 持续 (循环)|`int`|手动/自动模式|
|`enable_state`|`0` 字节(`LSB`): 电机开启 (0: 开 / 1: 关 / 2: 繁忙) <br> `翻译 (1)`: TP 启用 (死 man's) 开关 (0: 关闭 / 1: 开)<br>`翻译 (2)`: 机器锁 (0: 关闭 / 1: 开)<br>`翻译 (3)`: 枪锁 (0: 关闭 / 1: 开)<br>` (4)`: 枪 (0: 关闭 / 1: 开)|`int`||
|`is_playback`|`0`: 暂停 <br>`翻译 (1)`: 播放|`int`||
|`is_remote_mode`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否为远程模式|
|`is_ext_start`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否为外部启动|
|`is_ext_prog_sel`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否选择外部程序|

<br>

###### 2) 当前程序计数器
这是教导挂件 JOB 面板上条形光标在手动模式或自动模式中的位置。这是当前执行的语句或编辑的目标位置。
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|当前程序编号|
|`cur_step_no`|`int`|当前步骤编号|
|`cur_func_no`|`int`|当前功能编号|

<br>

###### 3) 移动程序计数器
这是机器人在播放过程中移动的目标步骤。
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|移动程序编号|
|`mov_step_no`|`int`|移动步骤编号|
|`mov_func_no`|`int`|移动功能编号|

<br>

###### 4) 速度
|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|手动模式的 Jog 速度等级 (1~8)|
|`manual_spd_max`|`int`|手动模式下的最大速度 (mm/sec)|
|`auto_spd`|`int`|自动模式播放速度 (%)|
|`jog_inch_status`|`int`|jog 微调状态 (0:关闭/ 1:开启)|
|`step_execute_unit_status`|`int`|StepFWD 执行单元 (运行到)<br>0: Cmd <br>1: Step<br>2: 结束 |
|`cont_path`|`int`|连续运动模式 (0~2)|

<br>

##### 示例
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