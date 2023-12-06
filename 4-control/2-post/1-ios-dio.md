## 4.2.1 `ios/dio/{do_val}`

### Description

`do` (digital output)

- `POST` : Change digital output.

### path-parameter

```python
POST /project/control/ios/dio/do_val
```

### request-body

```json
{
    "type": "do",
    "blk_no": 1,
    "sig_no": 1,
    "val": 1
}
```


### query-parameter

- `type` : Type of io value
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : block number (0~9)
- `sig_no` : signal index (0~)
- `val` : Setting value you want to change


### Example

```python
request url:
POST /project/control/ios/dio/do_val

request-body:
{
    "type": "do",
    "blk_no": 2,
    "sig_no": 3,
    "val": -99
}
```

Python Script Example

- Please refer to [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) for the response HTTP status code.
```python
# test.py
import requests 

def post_do_val() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ios/dio/do_val'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"type": "dob", "blk_no": 2, "sig_no": 3,"val": -99}

    response = requests.post(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {post_do_val()}")
```
```sh
$python test.py
response: 200 
```