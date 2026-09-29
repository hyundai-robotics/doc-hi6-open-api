#### 4.1.10 `joint_traject_mode`

##### 说明

- 支持版本：`70.06-00` ↑（计划支持）
- `GET`：查询外部轨迹（在线跟踪）模式是否正在运行或结束处理过程中。
- 以下任一条件成立时，`mode` 返回 `true`：
  - 外部轨迹模式正在运行；
  - 敏捷模式（agility mode）的 bypass 已开启；
  - 外部轨迹模式正在进行结束清理（clean-up）。
- 调用 [joint_traject_off](../2-post/10-joint_traject_off.md) 后，必须等待 `mode` 变为 `false`，再开始下一段轨迹。
- `mode` 为 `true` 时，[joint_traject_init](../2-post/7-joint_traject_init.md) 不会清空缓冲区；初始化前请先查询此接口。

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_mode
```

##### query-parameter

- 无

##### response

1. 状态码：200 OK、400 Bad Request、403 Forbidden、404 Not Found
2. 响应体：`mode`（boolean），表示外部轨迹模式正在运行或进行结束处理。

```json
{"mode": true}
```

{% hint style="warning" %}

使用敏捷模式时，运动结束后控制器需要 `0.5 秒`进行内部 clean-up。此期间 `mode` 仍为 `true`。未等待 `false` 就发送下一段轨迹可能导致意外错误。

{% endhint %}

##### 示例

```text
GET /project/robot/trajectory/joint_traject_mode

response-body:
{"mode": true}
```

Python 脚本示例

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_mode"

try:
    response = requests.get(uri, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```

```sh
$ python test.py
{'mode': True}
```
