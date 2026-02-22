#### 6.1.1 `get relay values`

##### 描述

- `GET` : 获取整个对象类型的继电器值。

##### 路径参数

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

##### 路径变量

[继电器表达式](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model})（小写字母）

* (`{obj_type}{obj_idx}_` 必须为 `di`、`do`、`x` 和 `y` 指定。剩余的 `relay_type` 不做规定。)

- `obj_type` : 对象类型
  - `fb`
  - `fn`

- `obj_idx` : 对象索引（fb: 0~9, fn: 0~63）

- `relay_type` : `di`、`do`、`x`、`y`、`m`、`字母s (s)`、`r`、`k`

##### 查询参数

- `st` : 起始字节索引（默认: 0）
- `len` : 字数（默认: 8）

##### 示例

```python
request url:
GET /project/plc/s/val_s32

response-body:
[
    16975105,
    132579331,
    252449291,
    406585366,
    327681,
    712706500,
    118947845,
    28
]
```
```python
请求 URL:
GET /project/plc/m/val_s32?st=32&len=4

响应主体:
[
    0,
    -2139095040,
    0,
    134217728
]
```

Python 脚本示例

```python
# test.py
import requests

def get_relay_value() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/m/val_s32'
    query_parameter = {"st": "32", "len": "4"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(f"{get_relay_value()}")
```
```sh
$python test.py
[0, 0, 0, 0]
```