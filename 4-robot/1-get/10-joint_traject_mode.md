#### 4.1.10 `joint_traject_mode`

##### Description

- Supported version: `70.06-00` ↑ (planned)
- `GET`: Returns whether external trajectory (online tracking) mode is active or being cleaned up.
- `mode` is `true` if any of the following applies:
  - External trajectory mode is active.
  - Agility mode bypass is enabled.
  - External trajectory mode clean-up is in progress.
- After [joint_traject_off](../2-post/10-joint_traject_off.md), wait until `mode` becomes `false` before starting the next trajectory sequence.
- [joint_traject_init](../2-post/7-joint_traject_init.md) does not clear the buffer while `mode` is `true`; check this API before initializing.

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_mode
```

##### query-parameter

- None

##### response

1. Status code: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found
2. Response body: `mode` (boolean) — external trajectory mode is active or clean-up is in progress.

```json
{"mode": true}
```

{% hint style="warning" %}

With agility mode, the controller requires `0.5 seconds` of internal clean-up after motion ends. `mode` remains `true` during this period. Sending the next trajectory without waiting for `false` may cause unexpected errors.

{% endhint %}

##### Example

```text
GET /project/robot/trajectory/joint_traject_mode

response-body:
{"mode": true}
```

Python Script Example

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_mode"

try:
    response = requests.get(uri, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```

```sh
$ python test.py
{'mode': True}
```
