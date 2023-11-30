## 6.1.1 `relay values`

### Description

- `GET` :Obtain the relay value for the entire object type.

### path-parameter

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

### path-variable

[relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/english/3-relay/2-relay-expression) (lowercase letter)

* (`{obj_type}{obj_idx}_` must be specified for `di`, `do`, `x`, and `y`. The remaining `relay_type` is not specified.)

- `obj_type` : object type
  - `fb`
  - `fn`

- `obj_idx` : object index (fb: 0~9, fn: 0~63)

- `relay_type` : 
	|`di`|`do`|`x` |`y` |`m` |`s` |`r`|`k`|
	|:---|:---|:---|:---|:---|:---|:---|:---|

	

### query-parameter

- `st` : start byte index (default: 0)
- `len` : number of words (default: 8)


### Example

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
request url:
GET /project/plc/m/val_s32?st=32&len=4

response-body:
[
	0,
	-2139095040,
	0,
	134217728
]
```

Python Script Example

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