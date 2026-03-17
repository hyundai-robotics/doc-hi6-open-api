#### 6.2.1 `设置继电器值`

##### 描述

- `POST` : 设置继电器值。

##### 路径参数

```python
POST /project/plc/set_relay_value
```

##### 请求参数

- `名称 (name)` : 根据 [继电器表达式](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model}) 输入您想要设置的继电器名称。
- `值 (value)` : 请注意上面的标记中的 'data-type'，并输入您想要设置的值。
```json
{
    "name": "fb3.dof14",
    "value": "2.718"
}
```

##### 示例

```json
请求 URL:
POST /project/plc/set_relay_value

请求体:
{
    "name": "fb1.do0",
    "value": "1"
}
```

Python 脚本示例

```python
# test.py
import requests

def get_relay_value() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/fb1_do/val_s32'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

def post_set_relay_value() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/set_relay_value'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"name": "fb1.do0", "value": 1}
 
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.status_code

print(f"{get_relay_value()}")
print(f"response: {post_set_relay_value()}")
print(f"{get_relay_value()}")
```
```sh
$python test.py
[0, 0, 0, 0, 0, 0, 0, 0]
响应: 200
[1, 0, 0, 0, 0, 0, 0, 0]
```
