#### 4.1.11 `joint_traject_ready`

##### Description

- Supported version: `70.06-00` ↑ (planned)
- `GET`: Returns whether the controller is ready to accept external trajectory commands.
- `ready` is `true` only if **both** conditions hold:
  - The base task motion state is waiting for command output.
  - Program playback is not stopped (a Job is running in Auto Mode).
- If a trajectory command is sent while `ready` is `false`, the controller raises an "external command not ready" error and clears the internal buffer. Trajectory logging is also disabled automatically.

{% hint style="warning" %}

**`ready` is always `false` in power-saving mode.** Before using external trajectory commands, set **System > 2: Control Parameter > 1: Control Environment Setting > Power saving function** to **Disable**.

{% endhint %}

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

1. Set **System > 2: Control Parameter > 1: Control Environment Setting > Power saving function** to **Disable**.
2. Move the robot to a safe reference pose.
3. Add a waiting statement such as `wait di1` to the Job, then run the program in Auto Mode.
4. Check that this API returns `ready == true`.
5. Clear the buffer with [joint_traject_init](../2-post/7-joint_traject_init.md), then send trajectory points.
6. If `ready == false`, do not send points; check the power-saving setting, program playback and controller errors first.

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
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_ready"

try:
    response = requests.get(uri, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```

```sh
$ python test.py
{'ready': True}
```
