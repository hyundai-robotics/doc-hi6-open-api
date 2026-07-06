#### 4.2.7 `joint_traject_init`

##### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : 初始化轨迹缓冲区。
- 在请求新的轨迹之前，用户必须清除之前存储的轨迹，尤其是在机器人停止时。
- ex)
  - request traj1 → 在运动过程中发生错误 → 必须使用 `joint_traject_init` 清除缓冲区 → request traj2 <br>
  : 如果错误发生时的轨迹数据仍保留在缓冲区中，则在未清除缓冲区的情况下请求 traj2 可能会导致另一个错误。
- 如果在通过 [joint_traject_insert_points](./8-joint_traject_insert_points.md) API 执行轨迹时调用此 API，缓冲区将立即更新。
  - 从缓冲区中删除之前存储的轨迹点可能导致机器人停止并触发错误。 请谨慎使用。


##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

##### request-body

<div style="width: fit-content;">

- {}

</div>


##### status code

- 200 : 请求成功
- 403 : 请求失败
  - 当调用不支持的 API 时返回
  - `err_code` (<0): 初始化失败

##### Example

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}
```

Python 脚本示例
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
        print(f"[INFO] 初始化成功: status={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] 初始化轨迹缓冲区失败: {e}")
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
[INFO] 初始化成功: status=200
```
</div>