## 5.1.9 `joint_traject_insert_point`

### 설명
- 지원 버전 : `60.34-00` ↑
- `POST` : 조인트 궤적 실행을 위해 **다음 조인트 목표 포인트를 순차적으로 추가**합니다.
- 해당 API를 반복 호출하여 연속적인 조인트 궤적을 구성할 수 있습니다.


### 주의 사항

* [축속도 제한값 초과 (E159)](https://hr-alarms.web.app/#/hi6/ko/E159)

  * 로봇 및 부가축 시스템이 허용하는 **최대 속도 및 토크를 초과해서는 안됩니다**.
  * 과도한 토크를 요구하는 지령이 전달되는 경우, 다음과 같은 **에러 또는 경고가 발생할 수 있습니다.**
  * 감속기 과토크
    * [E249](https://hr-alarms.web.app/#/hi6/ko/E249), [E6402](https://hr-alarms.web.app/#/hi6/ko/E6402), [E6403](https://hr-alarms.web.app/#/hi6/ko/E6403)
  * 감속기 과전류
    * [W153](https://hr-alarms.web.app/#/hi6/ko/W153), [W181](https://hr-alarms.web.app/#/hi6/ko/W181), [W182](https://hr-alarms.web.app/#/hi6/ko/W153)
  * 위치 편차 에러
    * [E2630](https://hr-alarms.web.app/#/hi6/ko/E2630), [E2636](https://hr-alarms.web.app/#/hi6/ko/E2636), [E2638](https://hr-alarms.web.app/#/hi6/ko/E2638)
* 실제 발생하는 에러 또는 경고는 **축 구성, 하중 조건, 동작 상황**에 따라 달라질 수 있습니다.

### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
```

</div>

### request-body

<div style="width: fit-content;">

```json
{
	"interval": 0.01,
	"time_from_start": 0.0,
	"look_ahead_time": 0.5,
	"point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

* interval

  * 증분 방식으로 포인트를 추가할 때 사용되는 시간 간격
* time_from_start

  * 궤적 시작 시점으로부터의 누적 시간
* look_ahead_time

  * 궤적 실행을 위한 look-ahead 시간
* point

  * 각 조인트의 목표 각도 배열 (deg)


### response

1. status code
   * 200 : OK
   * 400 : Bad Request
     * request body 가 유효성 검사에서 실패한 경우
   * 403 : Forbidden
   * 404 : Not Found


### 사용 예

```python
request url:
POST /project/robot/trajectory/joint_traject_insert_point

request-body:
{
    "interval": 0.01,
    "time_from_start": 0.0,
    "look_ahead_time": 0.5,
    "point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def post_joint_traject_insert_point() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/trajectory/joint_traject_insert_point"

    body = {
        "interval": 0.01,
        "time_from_start": 0.0,
        "look_ahead_time": 0.5,
        "point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
    }

    response = requests.post(url=base_url + path_parameter, json=body)

    return response


print(post_joint_traject_insert_point())
```

```sh
$python test.py
<Response [200]>
```

</div>