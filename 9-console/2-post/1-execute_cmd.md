<div style="width: fit-content;">

#### 9.2.1 `execute_cmd`


##### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : ${cont_model} 제어기의 콘솔 명령어를 실행합니다.    
- [CLI 로봇 언어 명령어 형식](../.././99-schema/robotlang.md)에 따른 명령을 수행할 수 있습니다.  

##### path-parameter

```python
POST /console/execute_cmd
```

##### request-body

```json
{
    "cmd_line" : "rl.reinit"
}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
   - 404 : Not Found

2) response body
	<div style="width: fit-content;">

	```json
	{ "_type" : "JObject" }
	```
	</div>

3) error code

   - 1: 로봇 언어 명령어 규칙을 벗어난 경우


##### 사용 예

</blockquote>

Python Script 예시
- `모터온` 이후 `원격모드` 상태에서 하기 명령어 수행 가능
- 현재 로봇 축 수에 맞춰서 move 문 입력 시 수행 가능

```python
# test.py
import time
import requests


cmds = [
    "rl.stop",   # 외부정지
    "rl.reinit", # 재시작
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
    "rl.i end",
    "rl.start",  # 재생
]

def post_execute_cmd(cmd: str) -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/console/execute_cmd"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"cmd_line": cmd}

    res = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return res


for cmd in cmds:
    ret = post_execute_cmd(cmd)
    print((ret.status_code, ret.json()))
    time.sleep(0.1)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```

</div>
