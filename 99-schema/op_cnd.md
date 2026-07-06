### `op_cnd`

#### Description
op_cnd (操作条件) : value of `条件设置 (Condition setting)`  
You can check the values when you press the `条件设置 (Condition setting)` button in TP.  

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1周期 <br> `2` : 重复|自动操作周期模式|
|step_goback_max_spd|` (10)` ~ `250` (mm/sec)|前进/后退时的最大速度|
|step_go_func_ex|`0` : 无效 <br> `1` : 有效 <br> `2` : I ON (=DI信号)|前进步骤时的功能执行|
|func_reexe_on_trace| `0` : 无效 <br> `1` : 有效 |后退后，再次执行向前移动时的功能|
|path_recov_confirm|`0` : 无效 <br> `1` : 有效|前进/后退时的路径恢复|
|playback_spd_rate|`1` ~ `100` (%)|自动操作速度比率|
|robot_lock|`0` : 无效 <br> `1` : 有效 |机器人锁定|
|intp_base|`0` : 机器人工具 <br> `1` : 定位工具|插补标准|
|ucrd_num|`0` ~ ` (20)`|指定用户坐标系|
|plc_mode|`0` : 关 -> 停止 <br> `1` : 停止 -> 远程停止 <br> `2` : 远程停止 -> 远程停止 <br> `3` : 远程运行 -> 远程停止 <br> `4` : 运行 -> 关|PLC操作模式|

<br>

#### Example

```python
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
    "ucrd_num": 10,
    "plc_mode": 4
}
```