# 3.1 rgen

## 설명

rgen (remote general status)

- GET : 로봇의 조건설정 값을 얻습니다.

## method path

```python
GET /project/rgen
```

## response-body

### 모드

- cur_mode : 수동/자동 모드
  - 0 : 수동
  - 1 : 수동, 시스템 설정
  - 3 : 자동, 1-cycle
  - 4 : 자동, 연속 (cycle 반복)

- is_playback : 재생 중
- is_remote_mode : 원격(Remote) 모드 여부
- is_ext_start : 외부 기동 여부
- is_ext_prog_sel : 외부 프로그램 선택 여부

- enable_state :
  - 0번 바이트(LSB) : 모터 ON
    - 0 : On
    - 1 : Off
    - 2 : Busy
  - 1번 바이트 : TP Enable (deadman) 스위치
    - 0 : OFF
    - 1 : ON
  - 2번 바이트 : 머신 Lock
    - 0 : OFF
    - 1 : ON
  - 3번 바이트 : 건(gun) Lock
    - 0 : OFF
    - 1 : ON
  - 4번 바이트 : 건(gun)
    - 0 : OFF
    - 1 : ON

### current 프로그램 카운터

수동모드나 자동모드에서 티치펜던트 JOB 패널의 막대형 커서가 위치한 지점입니다. 현재 실행되고 있는 명령문, 혹은 편집의 대상 위치입니다.

- cur_prog_no : current 프로그램 번호
- cur_step_no : current 스텝 번호
- cur_func_no : current 펑션 번호

### moving 프로그램 카운터

재생 중 로봇이 이동하고 있는 목표 스텝입니다.

- mov_prog_no : moving 프로그램 번호
- mov_step_no : moving 스텝 번호
- mov_func_no : moving 펑션 번호

## 속도

- spd_lev : 수동모드 조그 속도 레벨 (1~8)
- manual_spd_max : 수동모드 최대 속도 (mm/sec)
- auto_spd : 자동모드 재생 속도 (%)
- jog_inch_status : 조그 인칭 상태
  - 0 : OFF
  - 1 : ON
- step_execute_unit_status : StepFWD의 실행단위 (run to)
  - 0 : Cmd (명령문)
  - 1 : Step (스텝)
  - 2 : End (end문까지)
- cont_path : 연속 모션 모드 (0~2)
