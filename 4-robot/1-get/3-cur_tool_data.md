#### 4.1.3 `cur_tool_data`

##### 설명

- `GET` : 로봇의 현재 툴 데이터 얻기.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/cur_tool_data
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val : [툴 데이터](../../99-schema/tool_data.md)

##### 사용 예

```python
request url:
GET /project/robot/cur_tool_data

response-body:
{
    "_type": "Tool",
    "x": 0.000000,
    "rx": 0.000000,
    "y": 0.000000,
    "ry": 0.000000,
    "z": 0.000000,
    "rz": 0.000000,
    "cy": 0.000000,
    "mass": 20.000000,
    "cx": 100.000000,
    "cz": 65.000000,
    "ixx": 0.059000,
    "iyy": 0.061000,
    "izz": 0.075000,
    "mass_esti": 20.000000,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_cur_tool_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/cur_tool_data"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_cur_tool_data())
```
```sh
$python test.py
(200, {'_type': 'Tool', 'mass': 6.0, 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'y': 0.0, 'izz': 0.013, 'z': 0.0, 'iyy': 0.024, '
ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0})
```

</div>
