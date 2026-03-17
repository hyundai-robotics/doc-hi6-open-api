### `op_cnd`

#### 描述
op_cnd (操作条件) : `条件设置 (Condition setting)` 的值  
当您在 TP 中按下 `条件设置 (Condition setting)` 按钮时，可以查看这些值。

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `翻译 (1)` : 1 周期 <br> `翻译 (2)` : 重复|自动操作周期模式|
|step_goback_max_spd|`10` ~ `250` (毫米/秒)|前进/后退时的最大速度|
|step_go_func_ex|`0` : 无效 <br> `翻译 (1)` : 有效 <br> `翻译 (2)` : I ON (=DI 信号)|前进步骤时的功能执行|
|func_reexe_on_trace| `0` : 无效 <br> `翻译 (1)` : 有效 |向后走后，在向前移动时重新执行功能|
|path_recov_confirm|`0` : 无效 <br> `翻译 (1)` : 有效|前进/后退时的路径恢复|
|playback_spd_rate|`翻译 (1)` ~ `100` (%)|自动操作速度比例|
|robot_lock|`0` : 无效 <br> `翻译 (1)` : 有效 |机器人锁定|
|intp_base|`0` : 机器人工具 <br> `翻译 (1)` : 静止工具|插补标准|
|ucrd_num|`0` ~ `20`|指定用户坐标系|
|plc_mode|`0` : 关闭 -> 停止 <br> `翻译 (1)` : 停止 -> 远程停止 <br> `翻译 (2)` : 远程停止 -> 远程停止 <br> `翻译 (3)` : 远程运行 -> 远程停止 <br> ` (4)` : 运行 -> 关闭|PLC 操作模式|

<br>

#### 示例

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