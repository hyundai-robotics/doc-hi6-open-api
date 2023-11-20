# rgen
## 설명
|index|key|value type(python)|description|
|:---:|:---|:---|:---|
|01|apps_sync_seq|`int`||
|02|arc_weld_appl|`int`||
|03|arc_welder_no|`int`||
|04|arcon_cnd_no_|`int`|
|05|arcon_cnd_no_0|`int`||
|06|arcon_welder_0|`int`||
|07|arcon_welder_1|`int`||
|08|auto_spd|`int`|자동모드 재생 속도 (%)|
|09|axis_ctrl|`list`||
|10|axis_lock|`int`||
|11|base_intp|`int`||
|12|battery_status|`int`||
|13|call_depth|`int`||
|14|call_pno|`int`||
|15|chk_brake_release|`list`||
|16|confirm_command_delete|`int`||
|17|cont_path|`int`|연속 모션 모드 (0~2)|
|18|cooper_ctrl|`int`||
|19|cur_crd|`int`||
|20|cur_func_no|`int`|current 펑션 번호|
|21|cur_mech_axis_info|`int`||
|22|cur_mech_no|`int`||
|23|cur_mode|`int`|0: 수동<br>1: 수동, 시스템 결정<br>3: 자동, 1-cycle<br>4: 자동, 연속 (cycle 반복)|
|24|cur_prog_no|`int`|current 프로그램 번호|
|25|cur_scm_status|`int`||
|26|cur_step_no|`int`|current 스텝 번호|
|27|direct_teaching|`int`||
|28|eid_last_con_out|`int`||
|29|eid_last_err|`int`||
|30|eid_last_history|`int`||
|31|eid_last_noti|`int`||
|32|eid_last_warn|`int`||
|33|enable_state|`int`|`0번` 바이트(`LSB`) : 모터 ON (0: On / 1: Off / 2: Busy) <br> `1번` 바이트 : TP Enable (deadman) 스위치 (0: OFF / 1: ON)<br>`2번` 바이트 : 머신 Lock (0: OFF / 1: ON)<br>`3번` 바이트 : 건(gun) Lock (0: OFF / 1: ON)<br>`4번` 바이트 : 건(gun) (0: OFF / 1: ON)
|34|eng_code|`int`||
|35|gun_search_status|`int`||
|36|high_load|`int`||
|37|is_ext_prog_sel|`int`|외부 프로그램 선택 여부|
|38|is_ext_start|`int`|외부 기동 여부|
|39|is_manual_full_spd|`int`||
|40|is_playback|`int`|0: 정지 중<br>1: 재생 중|
|41|is_remote_mode|`int`|원격(Remote) 모드 여부|
|42|job_state|`int`||
|43|job_state_msg|`str`||
|44|job_sub_state|`int`||
|45|jog_inch_status|`int`|조그 인칭 상태 (0: OFF / 1: ON)
|46|load_esti|`int`||
|47|manual_spd_max|`int`|수동모드 최대 속도 (mm/sec)|
|48|mov_func_no|`int`|moving 펑션 번호|
|49|mov_prog_no|`int`|moving 프로그램 번호|
|50|mov_step_no|`int`|moving 스텝 번호|
|51|n_forced_io|`int`||
|52|n_prompt|`int`||
|53|next_exe_pno|`int`||
|54|paint_block_state|`int`||
|55|paint_gun_no|`int`||
|56|plc_mode|`int`||
|57|posi_sync|`int`||
|58|rec_step_ex_sw|`int`||
|59|robot_model|`str`||
|60|safety_recovery_mode|`int`||
|61|shift_state|`int`||
|62|spd_lev|`int`|수동모드 조그 속도 레벨 (1~8)|
|63|spot_cnd_no|`list`||
|64|spot_gun_no|`list`||
|65|spot_panel_thickness|`int`||
|66|spot_seq_no|`list`||
|67|step_execute_unit_status|`int`|StepFWD의 실행단위 (run to) <br> 0: Cmd (명령문) / 1: Step (스텝) / 2: End (end문까지)
|68|step_goback_resume|`int`||
|69|svgun_state|`int`||
|70|task_enable|`list`|
|71|task_no|`int`||
|72|tool_no|`int`||
|73|ucrd_no|`int`||




<details><summary>json</summary>

```json
{
    "_type": "JObject",
    "spot_cnd_no": [
        0,
        0,
        0,
        0
    ],
    "cont_path": 1,
    "eng_code": 0,
    "apps_sync_seq": 0,
    "call_pno": -1,
    "cur_mode": 0,
    "is_manual_full_spd": 0,
    "arc_welder_no": 0,
    "is_playback": 0,
    "high_load": 0,
    "spot_gun_no": [
        0,
        0,
        0,
        0
    ],
    "mov_func_no": 2,
    "is_ext_start": 0,
    "is_remote_mode": 0,
    "is_ext_prog_sel": 0,
    "enable_state": 256,
    "arc_weld_appl": 0,
    "manual_spd_max": 190,
    "n_forced_io": 0,
    "posi_sync": 0,
    "eid_last_err": 28203,
    "spd_lev": 1,
    "arcon_welder_0": 0,
    "eid_last_warn": -1,
    "arcon_cnd_no_0": 1,
    "eid_last_noti": 22750,
    "eid_last_history": 18009,
    "job_state": 0,
    "cur_func_no": 2,
    "eid_last_con_out": -1,
    "n_prompt": 0,
    "cur_prog_no": 7003,
    "cur_step_no": 0,
    "mov_prog_no": 7003,
    "task_enable": [
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "mov_step_no": 0,
    "axis_lock": 0,
    "task_no": 0,
    "shift_state": 0,
    "call_depth": 0,
    "next_exe_pno": -1,
    "tool_no": 0,
    "auto_spd": 100,
    "job_sub_state": 0,
    "jog_inch_status": 0,
    "spot_seq_no": [
        0,
        0,
        0,
        0
    ],
    "step_execute_unit_status": 0,
    "robot_model": "HH020-03",
    "cur_mech_no": 0,
    "base_intp": 0,
    "cur_mech_axis_info": 63,
    "load_esti": 1,
    "cur_crd": 0,
    "spot_panel_thickness": 0.000000,
    "ucrd_no": 0,
    "gun_search_status": 0,
    "step_goback_resume": 0,
    "job_state_msg": "",
    "cooper_ctrl": 16128,
    "svgun_state": 0,
    "arcon_welder_1": -1,
    "arcon_cnd_no_-1": 1,
    "plc_mode": 1,
    "battery_status": 0,
    "axis_ctrl": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    ],
    "paint_gun_no": 0,
    "paint_block_state": 0,
    "confirm_command_delete": 1,
    "direct_teaching": 0,
    "safety_recovery_mode": 0,
    "rec_step_ex_sw": 0,
    "cur_scm_status": 0,
    "chk_brake_release": [
        1,
        1,
        1,
        1,
        1,
        1
    ]
}
```
</details>