#### 4.2.12 `joint_traject_reset_under_fctrl`

##### Description

- Supported version : `70.06-00` ↑ (planned)
- `POST` : API that **resets the trajectory state required to re-run a trajectory** while in the mode where `fctrl_mode` of [joint_traject_init](./7-joint_traject_init.md) is `true`.
- The re-run procedure differs depending on the `fctrl_mode` value.

<div style="width: fit-content;">

| `fctrl_mode` | First run | Re-run |
| ----- | ------ | ------ |
| `false` | `joint_traject_init` | `joint_traject_init` |
| `true` | `joint_traject_init` | **`joint_traject_reset_under_fctrl`** |

</div>

- [joint_traject_init](./7-joint_traject_init.md) does not perform initialization while the trajectory mode is running ([joint_traject_mode](../1-get/10-joint_traject_mode.md) is `true`), so in `fctrl_mode : true` mode you must reset with this API.

##### Prerequisites

The force control function **does not operate on its own.** All of the following are required.

1. Controller force control **environment configuration**
2. Force control **license**
3. The mode entered by requesting [joint_traject_init](./7-joint_traject_init.md) with `fctrl_mode : true`

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_reset_under_fctrl
```
</div>

##### request-body

<div style="width: fit-content;">

```
{} : no input parameters
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - When a request is made for an API that is not permitted or not serviced
   - 404 : Not Found

2) response-body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```
</div>

{% hint style="warning" %}

- If called **while the trajectory is moving**, the trajectory points in the buffer are discarded, which may stop the robot and raise an error. Please call it after the previous trajectory has finished.
- Do not retry automatically on timeout; confirm whether the request was processed before re-running.

{% endhint %}

##### Usage example

<div style="width: fit-content;">

```joint_traject_reset_under_fctrl
POST /project/robot/trajectory/joint_traject_reset_under_fctrl

request-body
{}

response-body
{'_type': 'JObject'}
```

Python Script example

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_reset_under_fctrl"

try:
    response = requests.post(uri, json={}, timeout=5)
    response.raise_for_status()
    print(response.status_code, response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```
```sh
$ python test.py
200 {'_type': 'JObject'}
```

A 200 response means the trajectory state reset is complete and the next trajectory can be transmitted.
</div>
