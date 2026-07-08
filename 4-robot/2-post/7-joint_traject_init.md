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

##### 70.04-00 ↑ Changes

新增了 joint_traject_insert_point 的敏捷模式（agility mode）。

```json
{ "agility_mode": true, "agility_freq": 30 }
```

<div style="width: fit-content;">


| Parameter | Description |
| --------- | ----------- |
| `agility_mode` | 显著提升机器人到达目标指令的初始控制响应速度的模式。 |
| `agility_freq` | 指定敏捷模式的带宽工作频率。频率值设置得越高，机器人的响应速度越快，敏捷性越高。 |


如果未包含敏捷模式相关参数，或以空对象（{}）发送请求，敏捷模式将自动停用（false）。

{% hint style="info" %}

`关于振动与噪音的注意事项`: 频率值设置得越高，控制系统的响应性会急剧提升，但根据机器人的机械刚性及环境条件，可能会引发高频噪音或系统振动。

`安全运行提示`: 首次设置时，为保证系统稳定性，请从较低的频率带宽开始，在监控机器人运行状态和噪音的同时逐步提高频率，以找到最佳控制点。

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

普通模式
```json
{}
```

`70.04-00` 之后新增的属性

敏捷模式
```json
{"agility_mode": true, "agility_freq": 30}
```

</div>


<div style="width: fit-content;">

| Parameter | Attribute | Type | Default | Description & Constraints |
| --------- |------------ | -------- | -------- | -------- |
| agility_mode | Optional|boolean|false|若赋予 string 等无效类型，将返回 400 Bad Request 错误。|
| agility_freq | Optional|integer|20|省略时将自动应用默认频率。若超出控制器物理允许范围（0 ~ 500）或赋予无效类型，将返回 400 Bad Request 错误。|

</div>

##### status code

- 200 : 请求成功
- 400 : Bad Request
  -  v70.04-00↑ : `err_msg` - 返回错误详细信息。
- 403 : 请求失败
  - 当调用不支持的 API 时返回
  - `err_code` (<0): 初始化失败

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
