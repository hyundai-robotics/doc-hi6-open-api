#### 5.1.5 `tools/t_{number}`

##### 설명

- `GET` : 특정 툴의 설정값 정보를 받는 함수입니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/robot/tools/t_{number}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [툴 데이터](../../99-schema/tool_data.md)

##### 사용 예

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "_type" : "Tool",
    "x"     : 0.0,
    "y"     : 0.0,
    "z"     : 0.0,
    "rx"    : 0.0,
    "ry"    : 0.0,
    "rz"    : 0.0,
        ...
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_tool1_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/tools/t_1"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_tool1_data())
```
```sh
$python test.py
(200, {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, '
ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0})
```

</div>
