#### 5.1.9 `joint_traject_insert_point`

##### 描述
- 支持的版本: `70.00-00` ↑
- `POST`: **顺序附加下一个关节目标点**以执行关节轨迹。
- 通过重复调用此 API，可以构建连续的关节轨迹。

---

##### 注意事项

* [轴速度限制超出 (E159)](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E159)

  * 不要超过机器人的**最大允许速度和扭矩**以及辅助轴的限制。
  * 如果发出需要过大扭矩的命令，可能会发生以下**错误或警告**。
  * 减速机过扭矩
    * [E249](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E249), [E6402](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E6402), [E6403](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E6403)
  * 减速机过电流
    * [W153](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W153), [W181](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W181), [W182](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W153)
  * 位置偏差错误
    * [E2630](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2630), [E2636](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2636), [E2638](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2638)
* 实际的错误或警告可能会根据**轴配置、负载条件和操作状态**而有所不同。

---

##### 路径参数

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
````</div>

---

##### 请求体

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
* 间隔

  * 增量添加点时使用的时间间隔
* 从开始时间

  * 从轨迹开始的累积时间
* 前瞻时间

  * 轨迹执行的前瞻时间
* 点

  * 目标关节角度数组（度）

---

##### 响应

1. 状态码

   * 200 : 成功
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### 使用示例

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

##### Python 脚本示例

###### 先决条件
1. 将机器人移动到参考位置。
   (示例 - 对于6轴机器人：( 

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

  * 在逐步添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始的累计时间
* look_ahead_time

  * 轨迹执行的前瞻时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态代码

   * 200 : 成功
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 被禁止
   * 404 : 未找到

---
##### 使用示例

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

##### Python 脚本示例

###### 先决条件

1. 将机器人移动到参考姿态。
   (示例 - 对于一个 6 轴机器人: )`[0, 90, 0, 0, -90, 0]`)
2. 插入语句 ()
2. 在作业中插入语句 )`wait di1`。
3. 切换到自动模式并开始程序播放。
4. 在该状态下运行以下测试代码。

<div style="width: fit-content;">

```python
import time
import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888"  # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}
    return session.get(BASE_URL + path, params=params).json()["position"]


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }
    session.post(BASE_URL + path, json=body)


def fmt6(arr):
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02,  89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04,  89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06,  89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08,  89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10,  89.90, 0.0, 0.0, -90.0, 0.0],
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
之前:  ['0.000000', '90.000000', '0.000000', '0.000000', '-90.000000', '0.000000']

[插入 1] 已确认  t=0.002000s
[插入 2] 已确认  t=0.004000s
[插入 3] 已确认  t=0.006000s
[插入 4] 已确认  t=0.008000s
[插入 5] 已确认  t=0.010000s

之后: ['0.072196', '89.928004', '0.000000', '-0.000574', '-90.000000', '-0.001393']
```
