#### 4.2.16 `joystick/joy`

##### Description

- Supported version: `70.04-00` ↑
- `POST`: Jogs the robot in the direction specified by an external device.
- This API is for **directional jogging** only. It does not provide speed control proportional to stick deflection or modify the robot path while a job is running.

##### Prerequisites

1. Assign an input signal to **Joystick jog enable** and keep it **ON** while using joystick mode.
   - **TP630:** System → 4: Application Parameter → 16: Joystick mode → General settings → Enter the Joystick jog enable signal number → OK
   - For example, entering signal number `0` in the **Joystick jog enable** field assigns `di0`. The `di0` signal must be **ON** to use the joystick.
2. On the same screen, set **Execution type** to **Open-api**.
3. The motor must be **on**, and the controller must be in **Remote Auto mode**.
4. No **job or task** may be running.

See also: [Joystick mode](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/en-tp630/7-system/5-application-parameter/16-joystick-mode/README?cont_model=Hi6)


##### path-parameter

<div style="max-width: fit-content;">

```text
POST /project/robot/joystick/joy
```

##### request-body

```json
{
  "axes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

</div>

Send all 10 values in `axes` and use `0` for unused axes.

Jogging uses the current mechanism, [jog coordinate system](./4-crd_sys.md), [tool](./3-tool_no.md), and jog speed settings.

###### Direction mapping by index

| index | `-1` | `0` | `1` |
|:---:|:---|:---:|:---|
| 0 | Left | Neutral | Right |
| 1 | Forward | Neutral | Backward |
| 2 | Down | Neutral | Up |
| 3 | R2- | Neutral | R2+ |
| 4 | B- | Neutral | B+ |
| 5 | R1- | Neutral | R1+ |
| 6 | R3- | Neutral | R3+ |
| 7 | J8- | Neutral | J8+ |
| 8, 9 | Not used | **Send 0** | Not used |

The table shows jog key directions. The actual direction of movement may vary with the settings and robot model.

##### Precautions

On first use, verify the direction of movement at low speed using approved safety procedures.

{% hint style="warning" %}
**An empty or short array may leave previous jog inputs active. To set all jog inputs to neutral, send ten `0` values.**

A neutral request alone does not confirm that the robot has stopped.
{% endhint %}

###### Receive timeout

- The jog input timeout is **300 ms**. If the jogging conditions remain satisfied and no valid request is received within this period, the jog input is cleared.
- After communication is restored or the jogging conditions are met again, do not automatically resend the previous direction. Verify that the inputs are neutral and that the conditions for restarting are met.

{% hint style="warning" %}
The 300 ms timeout is not the robot's stopping time. This API does not replace an emergency stop or personnel safeguarding devices.
{% endhint %}

##### response

1) status code
   - 200 : OK
     - The request was processed successfully. This does not indicate that the robot has completed a move or come to a stop.
   - 400 : Bad Request
     - The request body could not be parsed, the operating conditions were not met, or `axes` was invalid.
   - 404 : Not Found

2) response-body

<div style="max-width: fit-content;">

   ```json
   {}
   ```

3) error code
   - -39010: A prerequisite was not met.
   - -39011: The `axes` input was invalid.

##### Example

```json
POST /project/robot/joystick/joy

request-body
{
  "axes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

Python script example

```python
import requests


def post_joystick_joy() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    url = f"{base_url}/project/robot/joystick/joy"
    body = {"axes": [0] * 10}

    return requests.post(url, json=body)


response = post_joystick_joy()
print((response.status_code, response.json()))
```

```sh
$python test.py
(200, {})
```

</div>
