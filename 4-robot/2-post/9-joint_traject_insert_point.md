#### 4.2.9 `joint_traject_insert_point`

##### Description
- Supported version: `70.00-00` ↑
- `POST`: **Sequentially appends the next joint target point** for joint trajectory execution.
- By repeatedly calling this API, a continuous joint trajectory can be constructed.

---

##### Notes

Operating Condition: Program Must Be Running
* The API must only be called while the controller program is running.
* Normal example: Executing a `wait di1` statement in Auto Mode
* Resulting error: [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) (External Command Operation Ready State Error)

Physical Condition: Comply with Speed and Torque Limits
* Commands exceeding the maximum speed and torque allowed by the system will cause an error.
* Basic error: [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) (Axis Speed Limit Exceeded Error)

Cascading Alarms Triggered by Over-Torque Commands
* Reducer Over-Torque: [E249](https://hr-alarms.web.app/#/${cont_model}/ko/E249) · [E6402](https://hr-alarms.web.app/#/${cont_model}/ko/E6402) · [E6403](https://hr-alarms.web.app/#/${cont_model}/ko/E6403)
* Reducer Over-Current: [W153](https://hr-alarms.web.app/#/${cont_model}/ko/W153) · [W181](https://hr-alarms.web.app/#/${cont_model}/ko/W181) · [W182](https://hr-alarms.web.app/#/${cont_model}/ko/W153)
* Position Deviation Exceeded: [E2630](https://hr-alarms.web.app/#/${cont_model}/ko/E2630) · [E2636](https://hr-alarms.web.app/#/${cont_model}/ko/E2636) · [E2638](https://hr-alarms.web.app/#/${cont_model}/ko/E2638)

Note: The actual alarms displayed may vary depending on the axis configuration, payload, and operating conditions.

##### `70.04-00` ↑

- `agility mode` has been added to significantly improve the initial control response speed of the robot to reach the target command.
- For details on how to activate this mode, please refer to the [`joint_traject_init` API](../2-post/7-joint_traject_init.md).

{% hint style="warning" %}

When using agility mode, a `0.5 second` controller internal clean-up process is required `after a motion ends`.  
Unexpected controller errors may occur if a consecutive trajectory is sent immediately without observing this delay.

{% endhint %}

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
# test.py
import time

import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888" # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}

    try:
        r = session.get(BASE_URL + path, params=params)
        return r.json().get("position")
    except Exception:
        return None


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }

    try:
        session.post(BASE_URL + path, json=body)
    except Exception as e:
        print(f"[ERROR] {e}")


def fmt6(arr):
    if arr is None:
        return None
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02, 89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04, 89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06, 89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08, 89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10, 89.90, 0.0, 0.0, -90.0, 0.0],
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
