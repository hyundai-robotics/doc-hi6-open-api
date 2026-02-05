### 5.1.4 `tools`

#### 설명

- `GET` : 로봇의 모든 툴 정보 얻기. T0~T31까지의 툴 중 존재하는 툴만 얻습니다.

#### path-parameter


<div style="width: fit-content;">

```python
GET /project/robot/tools
```

#### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - t_0 : [툴 데이터](../../99-schema/tool_data.md)
   - t_1 : 툴 데이터
   - t_2 : 툴 데이터  
   ...
   - t_31 : 툴 데이터

#### 사용 예

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
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_tools_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/tools"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_tools_data())
```
```sh
$python test.py
(200, {'_type': 'Tools', 't_1': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0,
 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_0': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.
0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_31': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias
_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_15': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.
0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}})
```

</div>
