<div style="width: fit-content;">

## 10.2.1 `execute_cmd`


### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : Hi6 제어기의 콘솔 명령어를 실행합니다.    
- [CLI 로봇 언어 명령어 형식](../.././99-schema/robotlang.md)에 따른 명령을 수행할 수 있습니다.  

### path-parameter

```python
POST /console/execute_cmd
```

### request-body

```json
{
    "cmd_line" : "rl.reinit"
}
```

### response-body

- 200 : 요청 성공  
	- 로봇 언어 명령어 규칙을 벗어난 경우 아래와 같이 ecode 1이 반환됩니다.
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400 : 요청 실패  
	- request body 가 유효성 검사에서 실패한 경우  
- 403/4 : 요청 실패  
	- 서비스 되지 않는 API 에 대해서 요청한 경우  

### 사용 예

</blockquote>

Python Script 예시
- `모터온`, `자동모드` 상태에서 하기 명령어 수행 가능
- 현재 로봇 축 수에 맞춰서 move 문 입력 시 수행 가능

```python
# test.py
import time
import requests


class ExecuteCmds:
    request_to = {
        "com": [
            "rl.stop",  # 외부정지
            "rl.reinit",  # 재시작
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i end",
            "rl.start",  # 재생
        ],
    }


def post_execute_cmd() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/console/execute_cmd"
    head = {"Content-Type": "application/json; charset=utf-8"}

    execute_cmds = ExecuteCmds.request_to["com"]

    response: int = None
    for cmd in execute_cmds:
        data = {"cmd_line": cmd}
        response = requests.post(url=base_url + path_parameter, headers=head, json=data)
        print(f"response: {response}")
        time.sleep(0.1)

    return 200


print(f"response: {post_execute_cmd()}")
```
```sh
$python test.py 
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: 200
```

</div>