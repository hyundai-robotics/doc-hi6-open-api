# op_cnd

## 설명

op_cnd (operation condition)

로봇의 조건설정 값입니다.

- playback_mode : 자동운전 동작 사이클 모드
  - 1 : 1사이클
  - 2 : 반복
- step_goback_max_spd : 스텝 전/후진 시 최고속
  - 10~250 (mm/sec)
- step_go_func_ex : 스텝 전진 시 펑션 실행
  - 0 : 무효
  - 1 : 유효
- func_re_execution_on_trace : 스텝 후진 후, 전진 시 펑션 재실행
  - 0 : 무효
  - 1 : 유효
  - 2 : I On
- path_recov_confirm : 스텝 전/후진 시 경로복구
  - 0 : 무효
  - 1 : 유효
- playback_spd_rate : 자동운전 속도비율
  - 1~100 (%)
- robot_lock : 로봇 Lock
  - 무효 : 0
  - 유효 : 1
- intp_base : 보간 기준
  - 0 : 로봇툴
  - 1 : 정치툴
- ucrd_num : 사용자 좌표계 지정
  - 0~20
- plc_mode : PLC 동작 모드
  - 0 : Off
  - 1 : Stop
  - 2 : Remote Stop
  - 3 : Remote Run
  - 4 : Run


## 예 (example)

```python
{
  "_type": "CondGrp",
  "playback_mode": 1,
  "step_goback_max_spd": 200,
  "step_go_func_ex": 1,
  "func_re_execution_on_trace": 0,
  "path_recov_confirm": 2,
  "playback_spd_rate": 100,
  "robot_lock": 0,
  "intp_base": 0,
  "ucrd_num": 0,
  "plc_mode": 4
}
```
