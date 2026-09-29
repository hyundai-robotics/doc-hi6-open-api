#### 4.1.11 `joint_traject_ready`

##### 说明

- 支持版本：`70.06-00` ↑（计划支持）
- `GET`：查询控制器是否已准备好接收外部轨迹指令。
- 仅当以下**两个条件同时满足**时，`ready` 才为 `true`：
  - 基本任务的运动状态处于等待指令输出状态；
  - 程序播放未停止（自动模式下 Job 正在运行）。
- 若 `ready` 为 `false` 时发送轨迹指令，控制器会报“外部指令不可执行”错误，并清空内部缓冲区；轨迹日志保存也会自动关闭。

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_ready
```

##### query-parameter

- 无

##### response

1. 状态码：200 OK、400 Bad Request、403 Forbidden、404 Not Found
2. 响应体：`ready`（boolean），表示是否可以开始发送外部轨迹指令。

```json
{"ready": true}
```

##### 使用步骤

1. 将机器人移动到安全的参考姿态。
2. 在 Job 中设置 `wait di1` 等等待语句，在自动模式下运行程序。
3. 确认本接口返回 `ready == true`。
4. 通过 [joint_traject_init](../2-post/7-joint_traject_init.md) 初始化缓冲区，然后发送轨迹点。
5. 若 `ready == false`，不要发送轨迹点；先检查程序运行状态和控制器错误。

{% hint style="info" %}

程序未运行时调用轨迹 API 可能触发 [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554)。轨迹超过速度限制可能触发 [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159)，使机器人停止。

{% endhint %}

##### 示例

```text
GET /project/robot/trajectory/joint_traject_ready

response-body:
{"ready": true}
```

Python 脚本示例

```python
# test.py
import time
import requests


def wait_traject_ready(base_url: str, session: requests.Session, timeout: float = 10.0) -> bool:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_ready"
    deadline = time.time() + timeout

    while time.time() < deadline:
        try:
            ret = session.get(url=uri)
            ret.raise_for_status()
            if ret.json().get("ready") is True:
                return True
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {e}")
            return False
        time.sleep(0.1)

    return False


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        print(wait_traject_ready(base_url, session))
```

```sh
$ python test.py
True
```
