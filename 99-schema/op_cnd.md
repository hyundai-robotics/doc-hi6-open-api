## op_cnd

### 설명
op_cnd (operation condition) : 로봇의 조건설정 값입니다.  
TP 에서 `조건설정` 버튼을 눌렀을 때 해당 값들을 확인할 수 있습니다.

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1사이클 <br> `2` : 반복|자동운전 동작 사이클 모드|
|step_goback_max_spd|`10` ~ `250` (mm/sec)|스텝 전/후진 시 최고속|
|step_go_func_ex|`0` : 무효 <br> `1` : 유효 <br> `2` : I ON (=DI신호)|스텝 전진 시 펑션 실행|
|func_reexe_on_trace| `0` : 무효 <br> `1` : 유효 |스텝 후진 후, 전진 시 펑션 재실행|
|path_recov_confirm|`0` : 무효 <br> `1` : 유효|스텝 전/후진 시 경로복구|
|playback_spd_rate|`1` ~ `100` (%)|자동운전 속도비율|
|robot_lock|`0` : 무효 <br> `1` : 유효 |로봇 Lock|
|intp_base|`0` : 로봇툴 <br> `1` : 정치툴|보간 기준|
|ucrd_num|`0` ~ `20`|사용자 좌표계 지정|
|plc_mode|`0` : Off -> Stop <br> `1` : Stop -> Remote Stop <br> `2` : Remote Stop -> Remote Stop <br> `3` : Remote Run -> Remote Stop <br> `4` : Run -> Off|PLC 동작 모드|

<br>

### 예 (example)

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
