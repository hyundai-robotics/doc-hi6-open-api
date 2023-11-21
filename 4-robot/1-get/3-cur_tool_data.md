# 4.1.3 `cur_tool_data`

## 설명

`cur_tool_data`

- `GET` : 로봇의 현재 툴 데이터 얻기.

## path-parameter

```python
GET /project/robot/cur_tool_data
```

## response-body

- val : [툴 데이터](/99-schema/tool_data.md)

## 사용 예

```python
request url:
GET /project/robot/cur_tool_data

response-body:
{
    "_type" : "JObject",
    "val" : 1
}
```

<details><summary>Python Script 예시</summary>

```python
# test.py
import requests

def get_cur_tool_data() -> dict:
	base_url        = 'http://192.168.1.150:8888'
	path_parameter  = '/project/robot/cur_tool_data'

	response = requests.get(url = base_url + path_parameter).json()

	return response

print(get_cur_tool_data())
```
```sh
$python test.py
{'_type': 'Tool', 'x': 0.0, 'rx': 0.0, 'y': 0.0, 'ry': 0.0, 'z': 0.0, 'rz': 0.0, 'cy': 0.0, 'mass': 20.0, 'cx': 100.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'bias_2': 0.0, 'mass_esti': 20.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```

</details>