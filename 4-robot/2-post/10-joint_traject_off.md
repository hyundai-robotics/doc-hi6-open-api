#### 4.2.10 `joint_traject_off`

##### Description

- Supported version: `70.06-00` ↑ (planned)
- `POST`: Requests termination of the active external trajectory (online tracking) mode.
- The request **initiates** termination; controller clean-up takes additional time. Confirm completion only when [joint_traject_mode](../1-get/10-joint_traject_mode.md) returns `false`.
- Sending another trajectory before termination completes may cause unexpected errors.

##### path-parameter

```text
POST /project/robot/trajectory/joint_traject_off
```

##### request-body

```json
{}
```

No input parameters.

##### response

1. Status code: 200 OK, 400 Bad Request, 403 Forbidden (unsupported API), 404 Not Found
2. Response body:

```json
{"_type": "JObject"}
```

##### Termination and recovery procedure

1. Request `joint_traject_off`.
2. Poll [joint_traject_mode](../1-get/10-joint_traject_mode.md) until `mode == false`.
3. When agility mode was used, allow at least `0.5 seconds` after motion ends for controller clean-up.
4. After an error stop, clear remaining buffered points with [joint_traject_init](./7-joint_traject_init.md) before sending another trajectory.
5. Recheck [joint_traject_ready](../1-get/11-joint_traject_ready.md) before resuming trajectory commands.

{% hint style="warning" %}

Agility mode requires `0.5 seconds` of controller clean-up after motion ends. Sending another trajectory immediately may cause unexpected errors.

{% endhint %}

##### Example

```text
POST /project/robot/trajectory/joint_traject_off

request-body:
{}

response-body:
{"_type": "JObject"}
```

Python Script Example

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_off"

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

HTTP 200 only confirms that the termination request was accepted. Before sending another trajectory, check that [joint_traject_mode](../1-get/10-joint_traject_mode.md) reports `mode == false`.
