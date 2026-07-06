#### 4.1.4 `tools`

##### Description

- `GET` : 获取机器人所有工具信息。仅获取 T0 到 T31 范围内存在的工具。

##### path-parameter

```python
GET /project/robot/tools
```

##### response-body

- t_0 : [工具数据](../../99-schema/tool_data.md)
- t_1 : 工具数据
- t_2 : 工具数据  
...
- t_31 : 工具数据

##### Example

仅存在工具 0 和工具 31 的系统示例。

```python
request url:
GET /project/robot/tools

response-body:
{
  "_type" : "Tools",
	"t_0" : { ... },
	"t_1" : { ... },
	 ...
}
```

Python 脚本示例

```python
# test.py
import requests

def get_tools_data() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/tools'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(get_tools_data())
```
```sh
$python test.py
{'_type': 'Tools', 't_31': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_0': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0, 'load_rate': {'_type': 'JObject', 'high_load_mode': -11, 'moment_rate': 0, 'inertia_rate': 0, 'mass_rate': 0}}, 't_1': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_15': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}}
```