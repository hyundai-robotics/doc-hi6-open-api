#### 4.1.12 `joint_traject_log`

##### 说明

- 支持版本：`70.04-00` ↑
- `GET`：查询关节轨迹日志保存功能是否启用。
- 启用或关闭日志请使用 [POST joint_traject_log](../2-post/11-joint_traject_log.md)。
- 如果控制器因未处于可执行状态而拒绝外部轨迹指令，日志保存会自动关闭，此接口返回 `0`。

##### path-parameter

```text
GET /project/robot/trajectory/joint_traject_log
```

##### query-parameter

- 无

##### response

1. 状态码：200 OK、400 Bad Request、403 Forbidden、404 Not Found
2. 响应体：`val`（integer），`1` 表示启用，`0` 表示关闭。

```json
{"val": 1}
```

##### 示例

```text
GET /project/robot/trajectory/joint_traject_log

response-body:
{"val": 1}
```

Python 脚本示例

```python
# test.py
import requests


def get_joint_traject_log(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    try:
        ret = session.get(url=uri)
        ret.raise_for_status()
        return ret.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        print(get_joint_traject_log(base_url, session))
```

```sh
$ python test.py
{'val': 1}
```
