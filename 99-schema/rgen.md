### rgen

#### description

|index|key|value type(python)|description|
|:---:|:---|:---|:---|
|01|apps_sync_seq|`int`||
|02|arc_weld_appl|`int`||
|03|arc_welder_no|`int`||
|04|arcon_cnd_no_|`int`||
|05|arcon_cnd_no_0|`int`||
|06|arcon_welder_0|`int`||
|07|arcon_welder_1|`int`||
|08|auto_spd|`int`|Playback speed in AUTO mode (%)|
|09|axis_ctrl|`list`||
|10|axis_lock|`int`||
|11|base_intp|`int`||
|12|battery_status|`int`||
|13|call_depth|`int`||
|14|call_pno|`int`||
|15|chk_brake_release|`list`||
|16|confirm_command_delete|`int`||
|17|cont_path|`int`|Continuous motion mode (0~2)|
|18|cooper_ctrl|`int`||
|19|cur_crd|`int`|Coordinate system (see ./crdsys.md)|
|20|cur_func_no|`int`|Current function number|
|21|cur_mech_axis_info|`int`||
|22|cur_mech_no|`int`||
|23|cur_mode|`int`|0: Manual<br>1: Manual (system decision)<br>3: Auto, 1-cycle<br>4: Auto, continuous (cycle repeat)|
|24|cur_prog_no|`int`|Current program number|
|25|cur_scm_status|`int`||
|26|cur_step_no|`int`|Current step number|
|27|direct_teaching|`int`||
|28|eid_last_con_out|`int`||
|29|eid_last_err|`int`||
|30|eid_last_history|`int`||
|31|eid_last_noti|`int`||
|32|eid_last_warn|`int`||
|33|enable_state|`int`|Byte0 (LSB): Motor ON (0: On / 1: Off / 2: Busy)<br>Byte1: TP Enable (deadman) switch (0: OFF / 1: ON)<br>Byte2: Machine Lock (0: OFF / 1: ON)<br>Byte3: Gun Lock (0: OFF / 1: ON)<br>Byte4: Gun Enable (0: OFF / 1: ON)|
|34|eng_code|`int`||
|35|gun_search_status|`int`||
|36|high_load|`int`||
|37|is_ext_prog_sel|`int`|External program selection status|
|38|is_ext_start|`int`|External start signal status|
|39|is_manual_full_spd|`int`||
|40|is_playback|`int`|0: Stopped<br>1: Running|
|41|is_remote_mode|`int`|Remote mode status|
|42|job_state|`int`||
|43|job_state_msg|`str`||
|44|job_sub_state|`int`||
|45|jog_inch_status|`int`|Jog inch status (0: OFF / 1: ON)|
|46|load_esti|`int`||
|47|manual_spd_max|`int`|Maximum speed in manual mode (mm/sec)|
|48|mov_func_no|`int`|Moving function number|
|49|mov_prog_no|`int`|Moving program number|
|50|mov_step_no|`int`|Moving step number|
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
|62|spd_lev|`int`|Jog speed level in manual mode (1~8)|
|63|spot_cnd_no|`list`||
|64|spot_gun_no|`list`||
|65|spot_panel_thickness|`int`||
|66|spot_seq_no|`list`||
|67|step_execute_unit_status|`int`|StepFWD execution unit (run to)<br>0: Command<br>1: Step<br>2: End (until END statement)|
|68|step_goback_resume|`int`||
|69|svgun_state|`int`||
|70|task_enable|`list`||
|71|task_no|`int`||
|72|tool_no|`int`||
|73|ucrd_no|`int`||
