#### 5.1.8 `joint_states`

##### 描述
- 支持的版本: `60.34-00` ↑
- `GET`: 获取机器人的当前关节状态。
- 返回 **关节角度（位置，°），速度和扭矩（努力）** 信息，每个关节均有。  
  你可以查询所有轴或选择性查询指定范围的轴。

##### 路径参数

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

##### 查询参数

* * 如果未指定参数，则查询所有关节。
* jno_start（可选）

  * 开始查询的关节索引（基于1）
* jno_n（可选）

  * 要查询的关节数量

##### 响应

1. 状态码

   * 200 : 正常
   * 400 : 请求错误

     * 查询参数验证失败
   * 403 : 禁止
   * 404 : 未找到

2. 响应体

   * position : 关节角度数组（度）
   * velocity : 关节速度数组
   * effort : 关节扭矩数组（Nm）

        <div style="width: fit-content;">

     ```json
     {
     	"position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
     	"velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     	"effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
     }
     ```
        </div>

##### 使用示例

<div style="max-width: 60vw;">

```python
请求 URL:
GET /project/robot/joint_states?jno_start=1&jno_n=6

响应主体:
{
    "position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
    "velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
}
```

Python 脚本示例

```python
# test.py
import requests

def get_joint_states() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/joints/joint_states"
    query = {"jno_start": 1, "jno_n": 6}

    res = requests.get(url=base_url + path, params=query)

    print(res.json())

    return res


get_joint_states()


```

```sh
$python test.py
{'_type': 'JObject', 'position': [0.949533, 90.949655, 0.949155, 0.948415, -89.050195, 0.948001], 'effort': [0.0, 93.988759, 93.925036, 0.179785, -5.312434, 0.102171], 'velocity': [-0.0, -0.0
, 0.0, 0.0, -0.0, 0.0]}
```

</div>
