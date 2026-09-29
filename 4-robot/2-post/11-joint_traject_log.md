#### 4.2.11 `joint_traject_log`

##### 说明

- 支持版本：`70.04-00` ↑
- `POST`：启用或关闭关节轨迹日志保存功能。
- 启用时，控制器会记录轨迹环形缓冲区操作（`RECV`、`WRTE`、`READ`、`INTP`、`SEND`、`EMPTY`）、各时刻的关节位置及缓冲区索引。
- 通过 [GET joint_traject_log](../1-get/12-joint_traject_log.md) 查询当前状态。
- 此接口用于轨迹调试，不建议长期启用日志保存。

##### path-parameter

```text
POST /project/robot/trajectory/joint_traject_log
```

##### request-body

```json
{"enable": true}
```

| 参数 | 属性 | 类型 | 默认值 | 说明及限制 |
| ---- | ---- | ---- | ------ | ---------- |
| `enable` | Required | boolean | false | `true` 启用日志，`false` 关闭日志。省略或传入非 boolean 值会导致请求失败。 |

##### response

1. 状态码：200 OK、400 Bad Request、403 Forbidden（缺少 `enable` 或其类型不是 boolean）、404 Not Found
2. 响应体：

```json
{"_type": "JObject"}
```

{% hint style="info" %}

请求失败时也可能返回相同的响应体（`{"_type": "JObject"}`）。请通过 [GET joint_traject_log](../1-get/12-joint_traject_log.md) 的 `val` 确认设置是否生效。

{% endhint %}

{% hint style="warning" %}

如果控制器因未处于可执行状态而拒绝外部轨迹指令，日志保存会自动关闭。若错误后仍需保存日志，重新开始时请再次启用。

{% endhint %}

##### 示例

```text
POST /project/robot/trajectory/joint_traject_log

request-body:
{"enable": true}

response-body:
{"_type": "JObject"}
```

Python 脚本示例

```python
# test.py
import requests


def set_joint_traject_log(base_url: str, session: requests.Session, enable: bool):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    try:
        response = session.post(url=uri, json={"enable": enable})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to set trajectory log: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    with requests.Session() as session:
        response = set_joint_traject_log(base_url, session, True)
        if response is None:
            return
        print(response.status_code, response.json())
        print(session.get(url=uri).json())  # 确认设置是否生效


if __name__ == "__main__":
    main()
```

```sh
$ python test.py
200 {'_type': 'JObject'}
{'val': 1}
```
