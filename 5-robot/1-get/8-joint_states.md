### 5.1.8 `joint_states`

#### 설명
- 지원 버전 : `60.34-00` ↑
- `GET` : 로봇의 현재 조인트 상태를 조회합니다.
- 각 조인트의 **각도(position, °), 속도(velocity), 토크(effort)** 정보를 반환하며, 전체 축 또는 지정한 축 구간만 선택적으로 조회할 수 있습니다.

#### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

#### query-parameter

* * 파라미터를 지정하지 않으면 전체 조인트를 조회합니다.
* jno_start (optional)
  * 조회를 시작할 조인트 번호 (1-base)
* jno_n (optional)
  * 조회할 조인트 개수


#### response

1. status code

   * 200 : OK
   * 400 : Bad Request
     * query parameter 가 유효성 검사에서 실패한 경우
   * 403 : Forbidden
   * 404 : Not Found

2. response-body

   * position : 조인트 각도 배열 (deg)
   * velocity : 조인트 속도 배열
   * effort : 조인트 토크 배열 (Nm)

		<div style="width: fit-content;">

		```json
		{
			"position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
			"velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			"effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
		}
		```

        </div>

#### 사용 예

<div style="max-width: 60vw;">

```python
request url:
GET /project/robot/joint_states?jno_start=1&jno_n=6

response-body:
{
    "position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
    "velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
}
```

Python Script 예시

```python
# test.py
import requests

def get_joint_states() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/joints/joint_states"
    query = {"jno_start": 1, "jno_n": 6}

    res = requests.get(url=base_url + path, params=query)

    print(res.json())

    return res


get_joint_states()


```

```sh
$python test.py
{'_type': 'JObject', 'position': [0.949533, 90.949655, 0.949155, 0.948415, -89.050195, 0.948001], 'effort': [0.0, 93.988759, 93.925036, 0.179785, -5.312434, 0.102171], 'velocity': [-0.0, -0.0
, 0.0, 0.0, -0.0, 0.0]}
```

</div>
