## 5.1.2 `po_cur`

### Description

`po_cur` (pose current)

- `GET` : Get the pose the robot is currently taking.

### path-parameter

```python
GET /project/robot/po_cur
```

### query-parameter

- `task_no` : task number (0~7).
  - unspecified : Applied as task 0.
  - &gt;=0 : If mechinfo is not specified, the current mechinfo of the task is applied.
- `crd` :  
  - unspecified : Obtain all tcp, axis, and encoder.
  - <0 : Follows the current recording coordinate system.
  - &gt;=0 : [coordinate system](../../99-schema/crdsys.md)
- `ucrd_no` : User coordinate system number (Specified only when crd is user.)
- `mechinfo` : [Mechanism information](../../99-schema/mechinfo.md)

### response-body

- [Pose information](../../99-schema/pose.md)


### Example

Example of a system with 6 robot axes (j1~j6) + 1 driving axis (j7) + 2 positioner axes (j8, j9).

- Obtain only the base coordinates of the robot

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

- Obtaining axis coordinates of all axes

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

- Obtain the axis coordinates of the positioner 2 axis (i.e. mechanism M2)

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

Python Script Example

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