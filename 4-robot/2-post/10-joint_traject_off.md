#### 4.2.10 `joint_traject_off`

##### 说明

- 支持版本：`70.06-00` ↑（计划支持）
- `POST`：请求结束当前运行的外部轨迹（在线跟踪）模式。
- 此请求只**发出结束指令**，控制器仍需时间完成内部清理。必须等待 [joint_traject_mode](../1-get/10-joint_traject_mode.md) 返回 `false` 才能确认结束。
- 在结束完成前发送下一段轨迹可能导致意外错误。

##### path-parameter

```text
POST /project/robot/trajectory/joint_traject_off
```

##### request-body

```json
{}
```

无需输入参数。

##### response

1. 状态码：200 OK、400 Bad Request、403 Forbidden（不支持的 API）、404 Not Found
2. 响应体：

```json
{"_type": "JObject"}
```

##### 结束与恢复步骤

1. 调用 `joint_traject_off`。
2. 轮询 [joint_traject_mode](../1-get/10-joint_traject_mode.md)，等待 `mode == false`。
3. 使用敏捷模式时，运动结束后至少等待 `0.5 秒`，以便控制器完成内部 clean-up。
4. 若因错误停止，在发送下一段轨迹前，使用 [joint_traject_init](./7-joint_traject_init.md) 清空残留的缓冲区数据。
5. 再次查询 [joint_traject_ready](../1-get/11-joint_traject_ready.md) 后恢复发送轨迹指令。

{% hint style="warning" %}

使用敏捷模式时，运动结束后控制器需要 `0.5 秒`进行内部 clean-up。立即发送下一段轨迹可能导致意外错误。

{% endhint %}

##### 示例

```text
POST /project/robot/trajectory/joint_traject_off

request-body:
{}

response-body:
{"_type": "JObject"}
```

Python 脚本示例

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
uri = f"{base_url}/project/robot/trajectory/joint_traject_off"

try:
    response = requests.post(uri, json={}, timeout=5)
    response.raise_for_status()
    print(response.status_code, response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```

```sh
$ python test.py
200 {'_type': 'JObject'}
```

HTTP 200 仅表示结束请求已被接受。发送下一段轨迹前，必须确认 [joint_traject_mode](../1-get/10-joint_traject_mode.md) 返回 `mode == false`。
