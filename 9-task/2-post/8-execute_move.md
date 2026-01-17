## 9.2.8 `execute_move`

<div style="width: fit-content;">

### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : 지정한 포즈로 이동합니다.  

### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

### request-body
- `stmt` : 요청 바디의 키 값으로, 구문(statment)을 뜻합니다.
- move 문 작성법과 관련된 내용은 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/ko/5-moving-robot/4-move?cont_model=${cont_model})을 참조 바랍니다.
	<div style="width: fit-content;">

	```json
	{
		"stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
	}
	```
	</div>
1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패
   - 403 : Forbidden
    	- 원격모드가 아닌 상태로 API 요청(v60.32 부터 적용)
   - 404 : Not Found

2) response-body
	- v60.30 이하 정상 응답
		<div style="width: fit-content;">

		```json
		{ "err_code" : 0 }
		```
		</div>
	- v60.32 이상 정상 응답

		<div style="width: fit-content;">

		```json
		{ "_type" : "JObject" }
		```
		</div>

3) error code
   - -38500 : 원격 모드가 아닌 상태로 해당 api 요청
   - -1442071 : MOTOR OFF 에서 api 요청
   - -1442080 : 프로그램 자동 운전 중에 api 요청
   - -1376272 : api 요청 수행 중 로봇 언어 문법 오류 발생

Python Script 예시
- 모터온이 된 상태에서, 현재 로봇 축에 맞는 pose 명령문 입력

```python
# test.py
import requests
import time


def post_execute_move(in_pose: str) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


poses = ["[-10, 90, -10, 0, 0, 0]", "[-5, 90, 5, 0, 0, 0]", "[0, 90, 0, 0, 0, 0]"]

for idx, pose in enumerate(poses):
    res = post_execute_move(pose)
    print((res.status_code, res.json()))

    if idx < len(poses) - 1:
        time.sleep(1.5)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
``````

</div>
