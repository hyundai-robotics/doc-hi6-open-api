#### 5.2.9 `joint_traject_insert_point`

##### Description
- Supported version: `70.00-00` ↑
- `POST`: **顺序附加下一个关节目标点**以执行关节轨迹。
- 通过重复调用此 API，可以构建连续的关节轨迹。

---

##### Notes

Operating Condition: 程序必须正在运行
* 只有在控制器程序运行时才能调用 API。
* 正常示例: 在自动模式下执行 `wait di1` 语句
* 结果错误: [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) (外部命令操作准备状态错误)

Physical Condition: 遵守速度和扭矩限制
* 超过系统允许的最大速度和扭矩的命令将导致错误。
* 基本错误: [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) (轴速度限制超出错误)

由过扭矩命令触发的级联警报
* 减速器过扭矩: [E249](https://hr-alarms.web.app/#/${cont_model}/ko/E249) · [E6402](https://hr-alarms.web.app/#/${cont_model}/ko/E6402) · [E6403](https://hr-alarms.web.app/#/${cont_model}/ko/E6403)
* 减速器过电流: [W153](https://hr-alarms.web.app/#/${cont_model}/ko/W153) · [W181](https://hr-alarms.web.app/#/${cont_model}/ko/W181) · [W182](https://hr-alarms.web.app/#/${cont_model}/ko/W153)
* 位置偏差超出: [E2630](https://hr-alarms.web.app/#/${cont_model}/ko/E2630) · [E2636](https://hr-alarms.web.app/#/${cont_model}/ko/E2636) · [E2638](https://hr-alarms.web.app/#/${cont_model}/ko/E2638)

注意: 显示的实际警报可能会因轴配置、有效载荷和操作条件而异。

---

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
````</div>

---

##### request-body

<div style="width: fit-content;">

```json
{
	"interval": 0.01,
	"time_from_start": 0.0,
	"look_ahead_time": 0.5,
	"point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

* interval

  * 添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始计算的累计时间
* look_ahead_time

  * 轨迹执行的提前时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态码

   * 200 : OK
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### Usage Example

```python
request url:
POST /project/robot/trajectory/joint_traject_insert_point

request-body:
{
    "interval": 0.01,
    "time_from_start": 0.0,
    "look_ahead_time": 0.5,
    "point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

---

##### Python Script Example

###### Prerequisites

1. 将机器人移动到参考姿态。
   (示例 - 对于一个六轴机器人: (

</div>

---

##### request-body

<div style="width: fit-content;">

```json
{
	"interval": 0.01,
	"time_from_start": 0.0,
	"look_ahead_time": 0.5,
	"point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

* interval

  * 添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始计算的累计时间
* look_ahead_time

  * 轨迹执行的提前时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态码

   * 200 : OK
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### Usage Example

```python
request url:
POST /project/robot/trajectory/joint_traject_insert_point

request-body:
{
    "interval": 0.01,
    "time_from_start": 0.0,
    "look_ahead_time": 0.5,
    "point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

---

##### Python Script Example

###### Prerequisites

1. 将机器人移动到参考姿态。
   (示例 - 对于一个六轴机器人: )`[0, 90, 0, 0, -90, 0]`)
2. 插入语句 ()
2. 插入语句 )`wait di1` 到任务中。
3. 切换到自动模式并开始程序播放。
4. 在该状态下运行下面的测试代码。

<div style="width: fit-content;">

```python
# test.py
import time

import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888" # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}

    try:
        r = session.get(BASE_URL + path, params=params)
        return r.json().get("position")
    except Exception:
        return None


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }

    try:
        session.post(BASE_URL + path, json=body)
    except Exception as e:
        print(f"[ERROR] {e}")


def fmt6(arr):
    if arr is None:
        return None
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02, 89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04, 89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06, 89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08, 89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10, 89.90, 0.0, 0.0, -90.0, 0.0],
    ]

    with requests.Session() as s:
        before = get_joint_positions(s)
        print("BEFORE: ", fmt6(before), end="\n\n")

        t = 0.0
        for i, p in enumerate(points, 1):
            t += interval
            insert_point(s, p, interval, look_ahead_time, t)
            print(f"[INSERT {i}] OK  t={t:.6f}s")
            time.sleep(0.001)

        time.sleep(0.05)

        after = get_joint_positions(s)
        print("\nAFTER:", fmt6(after))


if __name__ == "__main__":
    main()
```

```sh
$python test.py
BEFORE:  ['0.000000', '90.000000', '0.000000', '0.000000', '-90.000000', '0.000000']

[INSERT 1] OK  t=0.002000s
[INSERT 2] OK  t=0.004000s
[INSERT 3] OK  t=0.006000s
[INSERT 4] OK  t=0.008000s
[INSERT 5] OK  t=0.010000s

AFTER: ['0.072196', '89.928004', '0.000000', '-0.000574', '-90.000000', '-0.001393']
```

</div>