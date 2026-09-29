#### 4.1.12 `joint_traject_log`

##### Description

- Supported version: `70.04-00` ↑
- `GET`: Returns whether joint trajectory logging is enabled.
- Use [POST joint_traject_log](../2-post/11-joint_traject_log.md) to enable or disable logging.
- If the controller rejects an external trajectory command because it is not ready, logging is disabled automatically. This API then returns `0`.

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_log
```

##### query-parameter

- None

##### response

1. Status code: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found
2. Response body: `val` (integer) - `1` enabled, `0` disabled.

```json
{"val": 1}
```

##### Example

```text
GET /project/robot/trajectory/joint_traject_log

response-body:
{"val": 1}
```

Python Script Example

```python
# test.py
import requests


def get_joint_traject_log(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    try:
        ret = session.get(url=uri)
        ret.raise_for_status()
        return ret.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        print(get_joint_traject_log(base_url, session))
```

```sh
$ python test.py
{'val': 1}
```
