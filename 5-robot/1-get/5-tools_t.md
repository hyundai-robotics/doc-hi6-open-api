#### 5.1.5 `tools/t_{number}`

##### 描述

- `GET` : 这是一个接收特定工具设置信息的功能。

##### 路径参数

```python
GET /project/robot/tools/t_{number}
```

##### 响应主体

- [工具数据](../../99-schema/tool_data.md)

##### 示例

```python
请求网址:
GET /project/robot/tools/t_1

响应主体:
{
  "_type" : "Tool",
	"x" : 0.0,
	"y" : 0.0,
	"z" : 0.0,
	"rx" : 0.0,
	"ry" : 0.0,
	"rz" : 0.0,
	 ...
}
```

Python 脚本示例

```python
# test.py
import requests

def get_tool1_data() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/tools/t_1'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(get_tool1_data())
```
```sh
$python test.py
{'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```