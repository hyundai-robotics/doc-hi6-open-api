#### 4.2.11 `joint_traject_log`

##### Description

- Supported version: `70.04-00` ↑
- `POST`: Enables or disables joint trajectory logging.
- When enabled, the controller logs trajectory ring-buffer operations (`RECV`, `WRTE`, `READ`, `INTP`, `SEND`, `EMPTY`), joint positions and buffer indices at each step.
- Check the current setting with [GET joint_traject_log](../1-get/12-joint_traject_log.md).
- This API is for trajectory debugging; continuous logging is not recommended.

##### path-parameter

```text
POST /project/robot/trajectory/joint_traject_log
```

##### request-body

```json
{"enable": true}
```

| Parameter | Attribute | Type | Default | Description and constraints |
| --------- | --------- | ---- | ------- | --------------------------- |
| `enable` | Required | boolean | false | `true` enables logging; `false` disables it. Missing or non-boolean values cause the request to fail. |

##### response

1. Status code: 200 OK, 400 Bad Request, 403 Forbidden (missing or non-boolean `enable`), 404 Not Found
2. Response body:

```json
{"_type": "JObject"}
```

{% hint style="info" %}

A failed request can return the same response body (`{"_type": "JObject"}`). Confirm the effective setting using `val` from [GET joint_traject_log](../1-get/12-joint_traject_log.md).

{% endhint %}

{% hint style="warning" %}

If the controller rejects an external trajectory command because it is not ready, logging is automatically disabled. Re-enable logging when restarting after an error if you need further logs.

{% endhint %}

##### Example

```text
POST /project/robot/trajectory/joint_traject_log

request-body:
{"enable": true}

response-body:
{"_type": "JObject"}
```

Python Script Example

```python
# test.py
import requests


def set_joint_traject_log(base_url: str, session: requests.Session, enable: bool):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    try:
        response = session.post(url=uri, json={"enable": enable})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to set trajectory log: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    with requests.Session() as session:
        response = set_joint_traject_log(base_url, session, True)
        if response is None:
            return
        print(response.status_code, response.json())
        print(session.get(url=uri).json())  # Verify the effective setting


if __name__ == "__main__":
    main()
```

```sh
$ python test.py
200 {'_type': 'JObject'}
{'val': 1}
```
