#### 9.2.8 `execute_move`

##### 描述

- 支持的版本 : `60.28-00` &uparrow;
- `POST` : 移动到指定的姿态。

{% hint style="warning" %}
仅限HRSpace用户<br>
由于VRC_Hi6 v60.30-10到v60.32-06上的远程模式验证错误，execute_move可能会失败<br>
→ 使用v60.30-09或更早版本，或v60.32-07或更高版本（物理Hi6控制器不受影响）
{% endhint %}

##### 路径参数

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### 请求体
- `stmt` : 请求体中的键值，指向该语句。
- 有关如何编写移动语句的详细信息，请参阅 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/zh/5-moving-robot/4-move?cont_model=${cont_model})。

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

##### 响应

1. 状态码
- 200 : OK
- 400 : Bad Request
    - 请求体未通过验证。
- 403 : Forbidden
    - 尝试在非远程模式下进行API请求（自v60.30-07起生效）。
- 404 : Not Found

2. 响应体

- v60.30或更早版本的正常响应

```json
{ "err_code" : 0 }
```

- v60.32或更高版本的正常响应

```json
{ "_type" : "JObject" }
```
3. 错误代码

- -38500 : 尝试在非远程模式下发出API请求
- -1442071 : 尝试在电机关闭时发出API请求
- -1442080 : 尝试在自动程序执行期间发出API请求
- -1376272 : 处理API请求时发生机器人语言语法错误

Python脚本示例
- 在电机开启并符合当前机器人轴时输入位姿命令。

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