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

사전준비
1. 로봇 기준자세로 이동. (예시 - 6축 기준, [0, 90, 0, 0, -90, 0])
2. job 에서 ```wait di1``` 의 구문을 입력한다
3. 자동모드로 전환하고 프로그램을 재생한다.
4. 그 상태로 하기 테스트 코드를 실행한다.

<div style="width: fit-content;">

```python
import time
import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888"  # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}
    return session.get(BASE_URL + path, params=params).json()["position"]


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }
    session.post(BASE_URL + path, json=body)


def fmt6(arr):
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02,  89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04,  89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06,  89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08,  89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10,  89.90, 0.0, 0.0, -90.0, 0.0],
    ]

    with requests.Session() as s:
        before = get_joint_positions(s)
        print("BEFORE: ", fmt6(before), end="\n\n")

        t = 0.0
        for i, p in enumerate(points, 1):
            t += interval
            insert_point(s, p, interval, look_ahead_time, t)
            print(f"[INSERT {i}] OK  t={t:.6f}s")
            time.sleep(0.001)

        time.sleep(0.05)

        after = get_joint_positions(s)
        print("\nAFTER:", fmt6(after))

if __name__ == "__main__":
    main()
```

```sh
$python test.py
BEFORE:  ['0.000000', '90.000000', '0.000000', '0.000000', '-90.000000', '0.000000']

[INSERT 1] OK  t=0.002000s
[INSERT 2] OK  t=0.004000s
[INSERT 3] OK  t=0.006000s
[INSERT 4] OK  t=0.008000s
[INSERT 5] OK  t=0.010000s

AFTER: ['0.072196', '89.928004', '0.000000', '-0.000574', '-90.000000', '-0.001393']
```

</div>