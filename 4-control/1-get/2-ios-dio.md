## 4.1.2 `ios/dio/{dio_val}`

### Description

`dio` (digital input/output)

- `GET` : Obtain user IO values.

### path-parameter

```python
GET /project/control/ios/dio/{dio_val}
```

### path-variable

- `dio_val` :
  - `di_val` : Get the input(di) value.
  - `do_val` : Get the output(do) value.

### query-parameter

- `type` : Type of io value
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : block number (0~9)
- `sig_no` : signal index (0~)

### Example

- Get the fb2.dob3 value. (Result : 0b11001000 = 0xc8 = -56)

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```

Python Script Example

```python
# test.py
import requests

def get_dio_val() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/control/ios/dio/do_val'
    query_parameter = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3 }
    
    response = requests.get(url=base_url + path_parameter, params=query_parameter).json()

    return response

print(get_dio_val())
```
```sh
$python test.py
{'_type': 'JObject', 'val': -56}
```