#### 5.1.9 `joint_traject_insert_point`

##### Description
- Supported version: `60.34-00` ↑
- `POST`: **Sequentially appends the next joint target point** for joint trajectory execution.
- By repeatedly calling this API, a continuous joint trajectory can be constructed.

---

##### Notes

* [Axis Velocity Limit Exceeded (E159)](https://hr-alarms.web.app/#/hi6/ko/E159)

  * Do not exceed the **maximum allowable speed and torque** of the robot and auxiliary axes.
  * If commands requiring excessive torque are issued, the following **errors or warnings may occur**.
  * Reducer over-torque
    * [E249](https://hr-alarms.web.app/#/hi6/ko/E249), [E6402](https://hr-alarms.web.app/#/hi6/ko/E6402), [E6403](https://hr-alarms.web.app/#/hi6/ko/E6403)
  * Reducer over-current
    * [W153](https://hr-alarms.web.app/#/hi6/ko/W153), [W181](https://hr-alarms.web.app/#/hi6/ko/W181), [W182](https://hr-alarms.web.app/#/hi6/ko/W153)
  * Position deviation error
    * [E2630](https://hr-alarms.web.app/#/hi6/ko/E2630), [E2636](https://hr-alarms.web.app/#/hi6/ko/E2636), [E2638](https://hr-alarms.web.app/#/hi6/ko/E2638)
* Actual errors or warnings may vary depending on the **axis configuration, payload conditions, and operating state**.

---

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
````

</div>

---

##### request-body

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

  * Time interval used when adding points incrementally
* time_from_start

  * Cumulative time from the start of the trajectory
* look_ahead_time

  * Look-ahead time for trajectory execution
* point

  * Array of target joint angles (deg)

---

##### response

1. status code

   * 200 : OK
   * 400 : Bad Request

     * Request body validation failed
   * 403 : Forbidden
   * 404 : Not Found

---

##### Usage Example

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

---

##### Python Script Example

###### Prerequisites

1. Move the robot to the reference pose.
   (Example - for a 6-axis robot: `[0, 90, 0, 0, -90, 0]`)
2. Insert the statement `wait di1` in the job.
3. Switch to auto mode and start program playback.
4. Run the test code below in that state.

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
