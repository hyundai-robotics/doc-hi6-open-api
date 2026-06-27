#### 5.1.2 `po_cur`

##### Description

- `GET` : 获取机器人当前所处的姿态。

##### path-parameter

```python
GET /project/robot/po_cur
```

##### query-parameter

- `task_no` : 任务编号 (0~7)。
  - unspecified : 应用为任务 0。
  - &gt;=0 : 如果未指定 mechinfo，则应用任务的当前 mechinfo。
- `crd` :  
  - unspecified : 获取所有 tcp、轴和编码器。
  - <0 : 遵循当前记录的坐标系统。
  - &gt;=0 : [坐标系统](../../99-schema/crdsys.md)
- `ucrd_no` : 用户坐标系统编号 (仅在 crd 为用户时指定)。
- `mechinfo` : [机制信息](../../99-schema/mechinfo.md)

##### response-body

- [姿态信息](../../99-schema/pose.md)


##### Example

示例系统包含 6 个机器人轴 (j1~j6) + 1 个驱动轴 (j7) + 2 个定位轴 (j8, j9)。

- 仅获取机器人的基坐标

```python
request url:
GET /project/robot/po_cur?crd=0&mechinfo=1

response-body:
{
	"nsync" : 0,
	"_type" : "Pose",
	"rx" : 0.000000,
	"x" : 1782.000000,
	"ry" : 90.000000,
	"y" : 0.000000,
	"rz" : 0.000000,
	"z" : 1938.000000,
	"mechinfo" : 1,
	"crd" : "base"
}
```

- 获取所有轴的轴坐标

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=-1

response-body:
{
	"nsync" : 0,
	"_type" : "Pose",
	"mechinfo" : 65535,
	"j9" : 0.000000,
	"crd" : "joint",
	"j1" : 0.000000,
	"j2" : 90.000000,
	"j3" : 0.000000,
	"j4" : 0.000000,
	"j5" : 0.000000,
	"j6" : 0.000000,
	"j7" : 0.000000,
	"j8" : 0.000000
}
```

- 获取定位器 2 轴的轴坐标 (即机制 M2)

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=2

response-body:
{
    "nsync": 0,
    "_type": "Pose",
    "rx": 0.000000,
    "x": 0.000000,
    "ry": 0.000000,
    "y": 0.000000,
    "rz": 0.000000,
    "z": 0.000000,
    "mechinfo": 2,
    "crd": "joint",
    "j1": -0.690000,
    "j2": 84.448000,
    "j3": 22.304000,
    "j4": 0.000000,
    "j5": 0.000000,
    "j6": 0.000000
}
```

Python 脚本示例

```python
# test.py
import requests

def get_base_coordinate() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/po_cur'
    query_parameter = {'crd': 0, 'mechinfo': 1}

    response = requests.get(url = base_url + path_parameter, params = query_parameter).json()

    return response

print(get_base_coordinate())
```
```sh
$python test.py
{'nsync': 0, '_type': 'Pose', 'rx': 0.0, 'x': 1067.366, 'ry': 73.248, 'y': -12.859, 'rz': -0.69, 'z': 1609.909, 'mechinfo': 1, 'crd': 'base', 'j1': 0.0, 'j2': 0.0, 'j3': 0.0, 'j4': 0.0, 'j5': 0.0, 'j6': 0.0}
```