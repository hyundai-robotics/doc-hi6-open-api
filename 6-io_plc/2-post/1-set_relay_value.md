## 6.2.1 `set_relay_value`

### Description
`set_relay_value`

- `POST` : Set the relay value.

### path-parameter

```python
POST /project/plc/set_relay_value
```

### request-parameter

- `name` : Enter the relay name you want to set according to [relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/korean/3-relay/2-relay-expression).
- `value` : Please pay attention to ‘data-type’ in the notation above and enter the value you want to set.
```json
{
	"name": "fb3.dof14",
	"value": "2.718"
}
```

### Example

```json
request url:
POST /project/plc/set_relay_value

request-body:
{
	"name": "fb1.do0",
	"value": "1"
}
```

Python Script Example

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
response: 200
[1, 0, 0, 0, 0, 0, 0, 0]
```