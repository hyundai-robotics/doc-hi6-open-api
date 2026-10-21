#### 4.2.14 `fctrl_control`

##### Description

- Supported version : `70.06-00` ↑ (planned)
- `POST` : **Changes the force control condition (`cnd`)** currently being applied.
- Used to replace only the condition without halting the motion after force control motion has been started with [fctrl_run](./13-fctrl_run.md).
- The request only **instructs** the condition change; it takes time until the internal processing of the controller is complete.

##### Prerequisites

The force control function **does not operate on its own.** **All** of the following conditions must be satisfied before using this API.

<div style="width: fit-content;">

| Prerequisite | Details |
| ----- | ------ |
| Force control environment configuration | The force control related **environment configuration must be completed** on the controller. |
| Force control license | The **force control license must be registered** on the controller. |
| Force control trajectory mode | It must be the mode entered by requesting [joint_traject_init](./7-joint_traject_init.md) with `fctrl_mode : true`. |

</div>

{% hint style="danger" %}

If any one of the above conditions is not satisfied, the force control function will not operate.

- It does not operate **if the controller environment configuration is not done or the force control license is missing**.
- **This API cannot be used on its own** unless the mode has `fctrl_mode` of [joint_traject_init](./7-joint_traject_init.md) set to `true`.

{% endhint %}

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/force_control/ctrl/control
```
</div>

##### request-body

<div style="width: fit-content;">

```json
{ "cnd": 2 }
```

| Parameter | Attribute | Type | Default | Description and constraints |
| ----- | ------ | ------ | ------ | ------ |
| `cnd` | Required | integer | - | Force control condition number to change to. Assigning a wrong type or an unregistered condition number returns 400 Bad Request |

</div>

{% hint style="warning" %}

`cnd` is a number that points to a **force control condition registered in advance** on the controller.
Specifying an unregistered number may cause unintended motion or errors, so please verify that the condition is registered before use.

{% endhint %}

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - When `cnd` is missing or has a wrong type
     - When an unregistered force control condition number is specified
   - 403 : Forbidden
     - When a request is made for an API that is not permitted or not serviced
   - 404 : Not Found

2) response-body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```
</div>

##### Difference from `fctrl_run`

<div style="width: fit-content;">

| Category | [fctrl_run](./13-fctrl_run.md) | `fctrl_control` |
| ----- | ------ | ------ |
| Role | **Start** force control motion | **Change** the force control condition in effect |
| When to use | Force control not running | After motion has been started with [fctrl_run](./13-fctrl_run.md) |
| path | `/project/force_control/ctrl/run` | `/project/force_control/ctrl/control` |
| request-body | `{"cnd": <condition number>}` | `{"cnd": <condition number>}` |

</div>

{% hint style="warning" %}

- Changing the condition **while force control is running** immediately alters the behavior of the robot. Please verify the force/speed changes caused by the condition change in advance before use.
- This is a state changing request, so **do not apply automatic retries.** Even if a timeout occurs, the controller may have already executed the command. Check the controller state before deciding whether to re-run.
- Do not parallelize requests on the client side; reuse a single session to **preserve command order**.
- Do not treat redirect (3xx) responses as normal responses; handle them as errors.

{% endhint %}

##### Usage example

<div style="width: fit-content;">

```fctrl_control
POST /project/force_control/ctrl/control

request-body
{"cnd": 2}

response-body
{'_type': 'JObject'}
```

Python Script example

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
# base_url = "http://127.0.0.1:8888"  # hrspace

# Specify connect / read timeouts separately. These are not real-time guaranteed values.
REQUEST_TIMEOUT = (3.05, 10.0)


def post_json(session, path, body):
    """State changing POST. Propagates failures so that subsequent commands do not continue."""
    response = session.post(
        base_url + path,
        json=body,
        timeout=REQUEST_TIMEOUT,
        allow_redirects=False,
    )
    response.raise_for_status()
    if 300 <= response.status_code < 400:
        raise requests.HTTPError(f"Unexpected redirect: {response.status_code}")
    print(f"[INFO] {path} OK: status={response.status_code}")
    response.close()


def fctrl_run(session, cnd):
    """Start force control based motion (Run). Raises on request failure."""
    post_json(session, "/project/force_control/ctrl/run", {"cnd": cnd})


def fctrl_control(session, cnd):
    """Change the force control condition (Control). Raises on request failure."""
    post_json(session, "/project/force_control/ctrl/control", {"cnd": cnd})


def main():
    # Reuse the same session to preserve command order.
    with requests.Session() as session:
        print("[ACTION] Starting force control (Run)...")
        fctrl_run(session, 1)

        print("[ACTION] Changing force control cnd...")
        fctrl_control(session, 2)


if __name__ == "__main__":
    main()
```
```sh
$ python test.py
[ACTION] Starting force control (Run)...
[INFO] /project/force_control/ctrl/run OK: status=200
[ACTION] Changing force control cnd...
[INFO] /project/force_control/ctrl/control OK: status=200
```

A 200 response means the request to change the force control condition has been accepted.
</div>
