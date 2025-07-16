## 5.2.7 `joint_traject_init`

### Description

- Supported version : `61.00-00` &uparrow;
- `POST` : Initializes the trajectory buffer.
- Before requesting a new trajectory while the robot is stopped, the previously stored trajectory must be cleared by the user.
- ex)
  - request traj1 → error occurs during motion → buffer must be cleared using `joint_traject_init` → request traj2 <br>
  : If the trajectory data from the time of the error remains in the buffer, requesting traj2 without clearing the buffer may result in another error.
- If this api is called while a trajectory is being executed via the [joint_traject_insert_points](./8-joint_traject_insert_points.md) API, the buffer will be updated immediately.
  - Removing previously stored trajectory points from the buffer may cause the robot to stop and trigger an error. Use with caution.


### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

### request-body

<div style="width: fit-content;">

- {}

</div>


### status code

- 200 : Request succeeded
- 403 : Request failed
  - Returned when calling an unsupported API
  - `err_code` (<0): Initialization failed

### Example

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}
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