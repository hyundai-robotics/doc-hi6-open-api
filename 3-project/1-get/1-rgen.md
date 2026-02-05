#### 3.1.1 `rgen`

##### 설명

- `GET` : 제어기에 설정된 일반적인 정보들을 읽습니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/rgen
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	##### 2-1) 모드 정보
	<div style="width: fit-content;">

	|key|value|type|description|
	|:---|:---|:---|:---|
	|`cur_mode`| `0` : 수동 <br> `1` : 수동, 시스템 설정 <br>`3` : 자동, 1-cycle <br> `4` : 자동, 연속 (cycle 반복)|`int`|수동/자동 모드|
	|`enable_state`|`0번` 바이트(`LSB`) : 모터 ON (0: On / 1: Off / 2: Busy) <br> `1번` 바이트 : TP Enable (deadman) 스위치 (0: OFF / 1: ON)<br>`2번` 바이트 : 머신 Lock (0: OFF / 1: ON)<br>`3번` 바이트 : 건(gun) Lock (0: OFF / 1: ON)<br>`4번` 바이트 : 건(gun) (0: OFF / 1: ON)|`int`||
	|`is_playback`|`0` : 정지 중 <br>`1` : 재생 중|`int`||
	|`is_remote_mode`|`0`: False <br> `1`: True|`int`|원격(Remote) 모드 여부|
	|`is_ext_start`|`0`: False <br> `1`: True|`int`|외부 기동 여부|
	|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|외부 프로그램 선택 여부|

	</div>

	<br>


	##### 2-2) current 프로그램 카운터
	수동모드나 자동모드에서 티치펜던트 JOB 패널의 막대형 커서가 위치한 지점입니다. 현재 실행되고 있는 명령문, 혹은 편집의 대상 위치입니다.


	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`cur_prog_no`|`int`|current 프로그램 번호|
	|`cur_step_no`|`int`|current 스텝 번호|
	|`cur_func_no`|`int`|current 펑션 번호|

	</div>

	<br>

	##### 2-3) moving 프로그램 카운터

	재생 중 로봇이 이동하고 있는 목표 스텝입니다.

	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`mov_prog_no`|`int`|moving 프로그램 번호|
	|`mov_step_no`|`int`|moving 스텝 번호|
	|`mov_func_no`|`int`|moving 펑션 번호|

	</div>

	<br>

	##### 2-4) 속도


	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`spd_lev`|`int`|수동모드 조그 속도 레벨 (1~8)|
	|`manual_spd_max`|`int`|수동모드 최대 속도 (mm/sec)|
	|`auto_spd`|`int`|자동모드 재생 속도 (%)|
	|`jog_inch_status`|`int`|조그 인칭 상태 (0:OFF/ 1:ON)|
	|`step_execute_unit_status`|`int`|StepFWD의 실행단위 (run to)<br>0: Cmd (명령문)<br>1: Step (스텝)<br>2: End (end문까지)|
	|`cont_path`|`int`|연속 모션 모드 (0~2)|

	</div>

<br>

##### 사용 예
Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_rgen() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/rgen"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_rgen())
```
```sh
$python test.py
(200, {'_type': 'JObject', 'plc_mode': 4, 'safety_recovery_mode': 0, 'arcon_welder_0': 0, 'job_sub_state': 0, 'arcon_welder_1': -1, 'maintenance_status': 0, 'cur_mode': 0, 'cur_crd': 0, 'eid_last_err': 50033, 'eid_last_con_out': -1, 'is_manual_full_spd': 0, 'axis_ctrl': [1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'reducer_status': 0, 'cur_mech_no': 0, 'in_position': [1, 0, 0, 0, 0, 0, 0, 0], 'posi_sync': 0, 'job_state': 0, 'shift_state': 0, 'enable_state': 256, 'apps_sync_seq': 0, 'task_no': 0, 'a
uto_spd': 100, 'battery_status': 0, 'cooper_ctrl': 16128, 'cur_scm_status': 0, 'base_intp': 0, 'eid_last_start_stop': -1, 'is_ext_prog_sel': 0, 'arc_welder_no': 0, 'is_remote_mode': 0, 'is_playback': 0, 'axis_lock': 0, 'mov_prog_no': 3344, 'call_pno': -1, 'spot_seq_no': [0, 0, 
0, 0], 'eid_last_history': 50761, 'arcon_cnd_no_-1': 1, 'task_enable': [1, 0, 0, 0, 0, 0, 0, 0], 'ucrd_no': 0, 'high_load': 0, 'cur_prog_no': 3344, 'arc_weld_appl': 1, 'rec_step_ex_sw': 0, 'job_state_msg': '', 'spot_gun_no': [0, 0, 0, 0], 'step_execute_unit_status': 0, 'direct_
teaching': 0, 'jog_inch_status': 0, 'gun_search_status': 0, 'eid_last_noti': 36154, 'tool_no': 0, 'next_exe_pno': -1, 'paint_gun_no': 0, 'n_forced_io': 0, 'load_esti': 1, 'chk_brake_release': [1, 1, 1, 1, 1, 1], 'eng_code': 0, 'spd_lev': 1, 'spot_cnd_no': [0, 0, 0, 0], 'mov_fun
c_no': 0, 'confirm_command_delete': 1, 'paint_block_state': 0, 'cont_path': 1, 'cur_mech_axis_info': 63, 'arcon_cnd_no_0': 1, 'spot_panel_thickness': 0.0, 'robot_model': 'HA006B-01', 'manual_spd_max': 250, 'cur_step_no': 1, 'cur_func_no': 0, 'is_ext_start': 0, 'opc_ua_server_st
ate': -1, 'n_prompt': 0, 'svgun_state': 0, 'mov_step_no': 1, 'step_goback_resume': 0, 'call_depth': 0, 'eid_last_warn': -1})
```
</div>
