#### 4.2.7 `joint_traject_init`

##### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : Initializes the trajectory buffer.
- Before requesting a new trajectory while the robot is stopped, the previously stored trajectory must be cleared by the user.
- ex)
  - request traj1 → error occurs during motion → buffer must be cleared using `joint_traject_init` → request traj2 <br>
  : If the trajectory data from the time of the error remains in the buffer, requesting traj2 without clearing the buffer may result in another error.
- If this api is called while a trajectory is being executed via the [joint_traject_insert_points](./8-joint_traject_insert_points.md) API, the buffer will be updated immediately.
  - Removing previously stored trajectory points from the buffer may cause the robot to stop and trigger an error. Use with caution.

##### 70.04-00 ↑ Changes

Agility mode for joint_traject_insert_point has been added.

```json
{ "agility_mode": true, "agility_freq": 30 }
```

<div style="width: fit-content;">


| Parameter | Description |
| --------- | ----------- |
| `agility_mode` | A mode that significantly improves the initial control response speed of the robot to reach the target command. |
| `agility_freq` | Specifies the operating bandwidth frequency of the agility mode. Higher frequency values result in faster robot response and increased agility. |


If agility-related parameters are omitted or requested with an empty object ({}), agility mode is automatically deactivated (false).

{% hint style="info" %}

`Note on Vibration and Noise`: Setting a higher frequency value drastically sharpens the control system's responsiveness. However, depending on the robot's mechanical rigidity and environmental conditions, it may induce high-frequency noise or system vibration.

`Safe Operation Tip`: For system stability during initial setup, begin within a lower frequency bandwidth. Monitor the robot's behavior and noise level, then gradually increase the frequency to find the optimal control point.

{% endhint %}

</div>


##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

##### request-body

<div style="width: fit-content;">

Normal Mode
```json
{}
```

Properties added after `70.04-00`

Agility Mode
```json
{"agility_mode": true, "agility_freq": 30}
```

</div>


<div style="width: fit-content;">

| Parameter | Attribute | Type | Default | Description & Constraints |
| --------- |------------ | -------- | -------- | -------- |
| agility_mode | Optional|boolean|false|Returns a 400 Bad Request error if an invalid type (e.g., string) is assigned.|
| agility_freq | Optional|integer|20|Automatically applied as the default frequency if omitted. Returns a 400 Bad Request error if it falls outside the controller's physical allowance range (0 ~ 500) or if an invalid type is assigned.|

</div>

##### status code

- 200 : Request succeeded
- 400 : Bad Requests
  -  v70.04-00↑ : `err_msg` - Returns error description details.
- 403 : Request failed
  - Returned when calling an unsupported API
  - `err_code` (<0): Initialization failed

##### Example

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
ex1)
{}

ex2) V70.04-00 &uparrow;
{"agility_mode": true, "agility_freq": 30}

response-body
{'_type': 'JObject'}
```

Python Script Example
```python
# test.py

from typing import Union
import requests


def post_init_trajectories(
base_url: str, session: requests.Session
) -> Union[requests.Response, None]:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_init"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = session.post(url=uri, headers=headers)
        response.raise_for_status()
        print(f"[INFO] Initialization successful: status={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to initialize trajectory buffer: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        response = post_init_trajectories(base_url, session)


if __name__ == "__main__":
    main()
```
```sh
$python test.py
[INFO] Initialization successful: status=200
```
</div>
