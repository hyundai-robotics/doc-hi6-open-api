#### 4.1.11 `joint_traject_ready`

##### Description

- Supported version: `70.06-00` ↑ (planned)
- `GET`: Returns whether the controller is ready to accept external trajectory commands.
- `ready` is `true` only if **both** conditions hold:
  - The base task motion state is waiting for command output (`MotMoveReadyState`).
  - Program playback is not stopped (a Job is running in Auto Mode).
- If a trajectory command is sent while `ready` is `false`, the controller raises an "external command not ready" error and clears the internal buffer. Trajectory logging is also disabled automatically.

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_ready
```

##### query-parameter

- None

##### response

1. Status code: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found
2. Response body: `ready` (boolean) — whether an external trajectory command can be started.

```json
{"ready": true}
```

##### Procedure

1. Move the robot to a safe reference pose.
2. Add a waiting statement such as `wait di1` to the Job, then run the program in Auto Mode.
3. Check that this API returns `ready == true`.
4. Clear the buffer with [joint_traject_init](../2-post/7-joint_traject_init.md), then send trajectory points.
5. If `ready == false`, do not send points; check program playback and controller errors first.

{% hint style="info" %}

Calling a trajectory API when no program is running may cause [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554). Trajectories exceeding speed limits may cause [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) and stop the robot.

{% endhint %}

##### Example

```text
GET /project/robot/trajectory/joint_traject_ready

response-body:
{"ready": true}
```

Python Script Example

```python
# test.py
import time
import requests


def wait_traject_ready(base_url: str, session: requests.Session, timeout: float = 10.0) -> bool:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_ready"
    deadline = time.time() + timeout

    while time.time() < deadline:
        try:
            ret = session.get(url=uri)
            ret.raise_for_status()
            if ret.json().get("ready") is True:
                return True
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {e}")
            return False
        time.sleep(0.1)

    return False


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        print(wait_traject_ready(base_url, session))
```

```sh
$ python test.py
True
```
