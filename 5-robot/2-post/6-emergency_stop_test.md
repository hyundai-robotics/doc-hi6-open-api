## 5.2.6 `emergency_stop_test`

- <b style="color:orange"> 해당 API 는 `60.28-00` 까지 `emergency_stop` API 로 사용되었습니다. </b>  

### 설명

- 지원 버전 : `60.30-00` &uparrow;
- `POST` : 비상 정지 테스트 요청을 보냅니다.

### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/emergency_stop_test
```
</div>

### request-body

<div style="width: fit-content;">

-  |key|type|contents|validation|
	|---:|:---:|---|---|
	|`step_no`| int | 비상정지 타겟 스텝 번호, 현재 진행 중인 job 의 총 step 번호 이내| 1 ~ 999 |
	|`stop_at`| double | 지정위치의 몇 % 에서 멈출지 설정| 1 ~ 100 |
	|`stop_at_corner`| int | 0: 일반정지, 1: 코너정지| 0 or 1 |
	|`category`| int | 0: 즉시정지, 1: 감속정지, 2: 일시정지| 0 or 1 or 2 |

</div>

- `0: 즉시정지`  
  &rightarrow; 로봇 재생 중에 제어기가 꺼져버리는 경우와 동일한 경우. 정지 후 모터 오프가 됨  
- `1: 감속정지`  
	&rightarrow;  비상정지 버튼을 눌렀을 동작하는 경우. 정지 후 모터 오프가 됨  
- `2: 일시정지`  
	&rightarrow;  로봇 모션을 잠시 정지하는 경우. 정지 후 모터 오프가 되지 않음

### response 

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - v61.00-00 미만
       - 400 반환
     - v61.00-00 이상 (에러 세분화)
       - -38502: step number 유효성 검사 실패
       - -38503: stop at 유효성 검사 실패
       - -38504: stop at corner 유효성 검사 실패
       - -38505: category 유효성 검사 실패
       - -38506: request-body key 유효성 검사 실패
   - 404 : Not Found

2) response-body
	- v60.30 이하
		<div style="width: fit-content;">

		```json
		{"err_code": 200}
		```
		</div>
	- v61.00 이상
		<span>
		<div style="width: fit-content;">

		```json
		{"_type": "JObject"}
		```
		</div>
		<div style="width: fit-content;">

		```json
		{"err_code": "-38502"}
		```
		</div>
		</span>


### 사용 예

<div style="width: fit-content;">

```emergency_stop
POST /project/robot/emergency_stop

request-body
{
  "step_no": 1,
  "stop_at": 50,
  "stop_at_corner": 0,
  "category": 1,
}
```

Python Script 예시

```python
import requests


def post_emergency_stop_test() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/emergency_stop_test"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body_0 = {
        "step_no": 1,
        "stop_at": 1,
        "stop_at_corner": 0,
        "category": 1,
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body_0)

    return response


ret = post_emergency_stop_test()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>