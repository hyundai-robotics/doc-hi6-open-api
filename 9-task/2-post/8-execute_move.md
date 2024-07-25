## 9.2.8 `execute_move`

### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : 지정한 포즈로 이동합니다.  

### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

### request-body
- `stmt` : 요청 바디의 키 값으로, 구문(statment)을 뜻합니다.
- move 문 작성법과 관련된 내용은 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/korean/5-moving-robot/4-move)을 참조 바랍니다.

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

### response-body

- 200 : 요청 성공  
- 400 : 요청 실패  
	- request body 가 유효성 검사에서 실패  
- 403 : 요청 실패  
	- 서비스 되지 않는 API 에 대해서 요청을 한 경우

Python Script 예시
- 모터온이 된 상태에서, 현재 로봇 축에 맞는 pose 명령문 입력

```python
# test.py
import requests


def post_execute_move(flag: int, in_pose: str) -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(post_execute_move(1, "[-10, 90, -10, 0, 0, 0]"))

```
```sh
$python test.py 
200
```