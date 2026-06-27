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
|08|auto_spd|`int`|自动模式中的播放速度 (%)|
|09|axis_ctrl|`list`||
|10|axis_lock|`int`||
|11|base_intp|`int`||
|12|battery_status|`int`||
|13|call_depth|`int`||
|14|call_pno|`int`||
|15|chk_brake_release|`list`||
|16|confirm_command_delete|`int`||
|17|cont_path|`int`|连续运动模式 (0~2)|
|18|cooper_ctrl|`int`||
|19|cur_crd|`int`|坐标系统 (见 ./crdsys.md)|
|20|cur_func_no|`int`|当前功能编号|
|21|cur_mech_axis_info|`int`||
|22|cur_mech_no|`int`||
|23|cur_mode|`int`|0: 手动<br>1: 手动 (系统决定)<br>3: 自动, 1循环<br>4: 自动, 连续 (循环重复)|
|24|cur_prog_no|`int`|当前程序编号|
|25|cur_scm_status|`int`||
|26|cur_step_no|`int`|当前步骤编号|
|27|direct_teaching|`int`||
|28|eid_last_con_out|`int`||
|29|eid_last_err|`int`||
|30|eid_last_history|`int`||
|31|eid_last_noti|`int`||
|32|eid_last_warn|`int`||
|33|enable_state|`int`|Byte0 (LSB): 电机开启 (0: 开 / 1: 关 / 2: 忙)<br>Byte1: TP 启用 (死手) 开关 (0: 关闭 / 1: 开启)<br>Byte2: 机器锁 (0: 关闭 / 1: 开启)<br>Byte3: 枪锁 (0: 关闭 / 1: 开启)<br>Byte4: 枪启用 (0: 关闭 / 1: 开启)|
|34|eng_code|`int`||
|35|gun_search_status|`int`||
|36|high_load|`int`||
|37|is_ext_prog_sel|`int`|外部程序选择状态|
|38|is_ext_start|`int`|外部启动信号状态|
|39|is_manual_full_spd|`int`||
|40|is_playback|`int`|0: 停止<br>1: 运行|
|41|is_remote_mode|`int`|远程模式状态|
|42|job_state|`int`||
|43|job_state_msg|`str`||
|44|job_sub_state|`int`||
|45|jog_inch_status|`int`|电动进给状态 (0: 关闭 / 1: 开启)|
|46|load_esti|`int`||
|47|manual_spd_max|`int`|手动模式下的最大速度 (mm/sec)|
|48|mov_func_no|`int`|移动功能编号|
|49|mov_prog_no|`int`|移动程序编号|
|50|mov_step_no|`int`|移动步骤编号|
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
|62|spd_lev|`int`|手动模式下的 jog 速度级别 (1~8)|
|63|spot_cnd_no|`list`||
|64|spot_gun_no|`list`||
|65|spot_panel_thickness|`int`||
|66|spot_seq_no|`list`||
|67|step_execute_unit_status|`int`|StepFWD 执行单元 (运行到)<br>0: 命令<br>1: 步骤<br>2: 结束 (直到 END 语句)|
|68|step_goback_resume|`int`||
|69|svgun_state|`int`||
|70|task_enable|`list`||
|71|task_no|`int`||
|72|tool_no|`int`||
|73|ucrd_no|`int`||