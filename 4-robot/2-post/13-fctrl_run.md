#### 4.2.13 `fctrl_run`

##### Description

- Supported version : `70.06-00` ↑ (planned)
- `POST` : **Starts force control based motion** with the specified force control condition (`cnd`).
- Specify the force control condition number to use via `cnd` in the request body.
- The request only **instructs** the motion to start; it takes time until the internal processing of the controller is complete.
- Use [fctrl_stop](./15-fctrl_stop.md) to halt the force control motion, and [fctrl_control](./14-fctrl_control.md) to change only the condition while the motion is running.

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
POST /project/force_control/ctrl/run
```
</div>

##### request-body

<div style="width: fit-content;">

```json
{ "cnd": 1 }
```

| Parameter | Attribute | Type | Default | Description and constraints |
| ----- | ------ | ------ | ------ | ------ |
| `cnd` | Required | integer | - | Force control condition number to apply. Assigning a wrong type or an unregistered condition number returns 400 Bad Request |

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

##### Related APIs

<div style="width: fit-content;">

| API | Purpose |
| ----- | ------ |
| `fctrl_run` | **Start** force control motion |
| [fctrl_control](./14-fctrl_control.md) | **Change** the force control condition (`cnd`) |
| [fctrl_stop](./15-fctrl_stop.md) | **Halt** force control and motion |
| [joint_traject_init](./7-joint_traject_init.md) | Enter force control trajectory mode with `fctrl_mode : true` |
| [joint_traject_reset_under_fctrl](./12-joint_traject_reset_under_fctrl.md) | Reset the state before re-transmitting a trajectory in `fctrl_mode : true` mode |

</div>

{% hint style="warning" %}

- This is a state changing request, so **do not apply automatic retries.** Even if a timeout occurs, the controller may have already executed the command. Check the controller state before deciding whether to re-run.
- Do not parallelize requests on the client side; reuse a single session to **preserve command order**.
- Do not treat redirect (3xx) responses as normal responses; handle them as errors.

{% endhint %}

##### Usage example

<div style="width: fit-content;">

```fctrl_run
POST /project/force_control/ctrl/run

request-body
{"cnd": 1}

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


def main():
    with requests.Session() as session:
        print("[ACTION] Starting force control (Run)...")
        fctrl_run(session, 1)


if __name__ == "__main__":
    main()
```
```sh
$ python test.py
[ACTION] Starting force control (Run)...
[INFO] /project/force_control/ctrl/run OK: status=200
```

A 200 response means the request to start force control motion has been accepted.
</div>
