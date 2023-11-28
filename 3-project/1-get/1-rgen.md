## 3.1.1 `rgen`

### 설명

`rgen` (remote general status)

- `GET` : 로봇의 조건설정 값을 얻습니다.

### path-parameter

```python
GET /project/rgen
```

### response-body

#### 1) 모드
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : 수동 <br> `1` : 수동, 시스템 설정 <br>`3` : 자동, 1-cycle <br> `4` : 자동, 연속 (cycle 반복)|`int`|수동/자동 모드|
|`enable_state`|`0번` 바이트(`LSB`) : 모터 ON (0: On / 1: Off / 2: Busy) <br> `1번` 바이트 : TP Enable (deadman) 스위치 (0: OFF / 1: ON)<br>`2번` 바이트 : 머신 Lock (0: OFF / 1: ON)<br>`3번` 바이트 : 건(gun) Lock (0: OFF / 1: ON)<br>`4번` 바이트 : 건(gun) (0: OFF / 1: ON)|`int`||
|`is_playback`|`0` : 정지 중 <br>`1` : 재생 중|`int`||
|`is_remote_mode`|`0`: False <br> `1`: True|`int`|원격(Remote) 모드 여부|
|`is_ext_start`|`0`: False <br> `1`: True|`int`|외부 기동 여부|
|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|외부 프로그램 선택 여부|

<br>

#### 2) current 프로그램 카운터
수동모드나 자동모드에서 티치펜던트 JOB 패널의 막대형 커서가 위치한 지점입니다. 현재 실행되고 있는 명령문, 혹은 편집의 대상 위치입니다.
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|current 프로그램 번호|
|`cur_step_no`|`int`|current 스텝 번호|
|`cur_func_no`|`int`|current 펑션 번호|

<br>

#### 3) moving 프로그램 카운터

재생 중 로봇이 이동하고 있는 목표 스텝입니다.
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|moving 프로그램 번호|
|`mov_step_no`|`int`|moving 스텝 번호|
|`mov_func_no`|`int`|moving 펑션 번호|

<br>

#### 4) 속도

|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|수동모드 조그 속도 레벨 (1~8)|
|`manual_spd_max`|`int`|수동모드 최대 속도 (mm/sec)|
|`auto_spd`|`int`|자동모드 재생 속도 (%)|
|`jog_inch_status`|`int`|조그 인칭 상태 (0:OFF/ 1:ON)|
|`step_execute_unit_status`|`int`|StepFWD의 실행단위 (run to)<br>0: Cmd (명령문)<br>1: Step (스텝)<br>2: End (end문까지)|
|`cont_path`|`int`|연속 모션 모드 (0~2)|

<br>

### 사용 예
Python Script 예시

```python
import requests

def is_remote_mode() -> bool:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/rgen'    
    
    response = requests.get(url = base_url + path_parameter).json()    

    print(f'is remote mode? {response['is_remote_mode']}')    
    
    return response['is_remote_mode']

get_is_remote_mode()
```
```sh
$python test.py
is remote mode? 0
```
