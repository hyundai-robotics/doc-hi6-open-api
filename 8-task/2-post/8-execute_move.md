#### 8.2.8 `execute_move`

##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : 移动到指定姿态。

{% hint style="warning" %}
HRSpace 用户专用<br>
execute_move 可能因 VRC_${cont_model} v60.30-10 到 v60.32-06 的远程模式验证错误而失败<br>
→ 使用 v60.30-09 或更早版本，或 v60.32-07 或更高版本（物理 ${cont_model:upper} 控制器不受影响）
{% endhint %}

##### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### request-body
- `stmt` : 请求体中的关键值，指代语句。
- 有关如何编写移动语句的详细信息，请参见 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/zh/5-moving-robot/4-move?cont_model=${cont_model})。

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

##### response

1. 状态代码
- 200 : OK
- 400 : 错误请求
    - 请求体未通过验证。
- 403 : 禁止
    - 在未处于远程模式下尝试 API 请求（自 v60.30-07 起生效）。
- 404 : 未找到

2. 响应体

- v60.30 或更早版本的正常响应

```json
{ "err_code" : 0 }
```

- v60.32 或更高版本的正常响应

```json
{ "_type" : "JObject" }
```

3. 错误代码

- -38500 : 在未处于远程模式下尝试 API 请求
- -1442071 : 在电机关闭时尝试 API 请求
- -1442080 : 在自动程序执行期间尝试 API 请求
- -1376272 : 处理 API 请求时出现机器人语言语法错误

Python 脚本示例
- 当电机开启并与当前机器人轴匹配时输入姿态命令。

```python
# test.py
import requests
import time


def post_execute_move(in_pose: str) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


poses = ["[-10, 90, -10, 0, 0, 0]", "[-5, 90, 5, 0, 0, 0]", "[0, 90, 0, 0, 0, 0]"]

for idx, pose in enumerate(poses):
    res = post_execute_move(pose)
    print((res.status_code, res.json()))

    if idx < len(poses) - 1:
        time.sleep(1.5)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```