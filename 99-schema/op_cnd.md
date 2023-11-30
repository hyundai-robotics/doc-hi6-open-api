# op_cnd

## Description
op_cnd (operation condition) : value of `Condition setting`  
You can check the values when you press the `Condition setting` button in TP.  

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1 cycle <br> `2` : repeat|Automatic operation cycle mode|
|step_goback_max_spd|`10` ~ `250` (mm/sec)|Maximum speed when stepping forward/reverse|
|step_go_func_ex|`0` : invalid <br> `1` : valid <br> `2` : I ON (=DI signal)|Function execution when advancing step|
|func_reexe_on_trace| `0` : invalid <br> `1` : valid |After stepping backwards, re-execute the function when moving forward|
|path_recov_confirm|`0` : invalid <br> `1` : valid|Path recovery when stepping forward/backward|
|playback_spd_rate|`1` ~ `100` (%)|Automatic operation speed ratio|
|robot_lock|`0` : invalid <br> `1` : valid |Robot Lock|
|intp_base|`0` : robot tool <br> `1` : stationary tool|Interpolation criteria|
|ucrd_num|`0` ~ `20`|Specify user coordinate system|
|plc_mode|`0` : Off -> Stop <br> `1` : Stop -> Remote Stop <br> `2` : Remote Stop -> Remote Stop <br> `3` : Remote Run -> Remote Stop <br> `4` : Run -> Off|PLC operation mode|

<br>

## Example

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
