#### 4.2.15 `fctrl_stop`

##### Description

- Supported version : `70.06-00` ↑ (planned)
- `POST` : Requests a **halt of force control and motion (Halt)**.
- Halts the force control motion started with [fctrl_run](./13-fctrl_run.md).
- The request only **instructs** the halt; it takes time until the internal termination processing of the controller is complete.
- There are no input parameters.

{% hint style="danger" %}

This API **does not replace a hardware emergency stop.**

Because it is a software halt request that travels over the network, an immediate stop is not guaranteed when communication is delayed or disconnected.
For safety related stops, always use a hardware emergency stop device.

{% endhint %}

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
POST /project/force_control/ctrl/stop
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

##### Related APIs

<div style="width: fit-content;">

| API | Purpose |
| ----- | ------ |
| [fctrl_run](./13-fctrl_run.md) | **Start** force control motion |
| [fctrl_control](./14-fctrl_control.md) | **Change** the force control condition (`cnd`) |
| `fctrl_stop` | **Halt** force control and motion |
| [joint_traject_off](./10-joint_traject_off.md) | **Exit** external trajectory mode |
| [emergency_stop](./5-emergency_stop.md) | Emergency stop |

</div>

{% hint style="warning" %}

- If the force control trajectory mode (`fctrl_mode : true` of [joint_traject_init](./7-joint_traject_init.md)) was used together, exiting the trajectory mode must be performed separately with [joint_traject_off](./10-joint_traject_off.md). Please confirm that the exit is complete by checking that [joint_traject_mode](../1-get/10-joint_traject_mode.md) becomes `false`.
- This is a state changing request, so **do not apply automatic retries.** Even if a timeout occurs, the controller may have already performed the halt. Check the controller state before deciding whether to re-run.
- Even if the client program terminates due to an error or `Ctrl+C`, **robot motions already accepted may continue.** Terminating the program does not mean the robot stops.
- Do not treat redirect (3xx) responses as normal responses; handle them as errors.

{% endhint %}

##### Usage example

<div style="width: fit-content;">

```fctrl_stop
POST /project/force_control/ctrl/stop

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


def fctrl_stop(session):
    """Request a halt of force control and motion (Halt). Does not replace a hardware emergency stop."""
    post_json(session, "/project/force_control/ctrl/stop", {})


def main():
    with requests.Session() as session:
        print("[ACTION] Stopping force control (Halt)...")
        fctrl_stop(session)


if __name__ == "__main__":
    main()
```
```sh
$ python test.py
[ACTION] Stopping force control (Halt)...
[INFO] /project/force_control/ctrl/stop OK: status=200
```

A 200 response means the halt request has been accepted. Whether the halt is complete must be confirmed from the controller state.
</div>
