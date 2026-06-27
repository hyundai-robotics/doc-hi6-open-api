#### 6.1.3 `ios/sio/{sio_val}` 

##### Description

- `GET` : 获取系统 IO 值。

##### path-parameter

```python
GET /project/control/ios/sio/{sio_val}
```

##### path-variable

- `sio_val` :
  - `si_val` : 获取输入(si) 值。
  - `so_val` : 获取输出(so) 值。

##### query-parameter

- `类型 (type)` : IO 值的类型
  - si 或 so : bit
  - sib 或 sob : signed-byte
  - siw 或 sow : signed-word (2byte)
  - sil 或 sol : signed-dword (4yte)
  - sif 或 sof : float
- `sig_no` : 信号索引 (0~)


##### Example

- 获取 sib1 值。 (结果 : 0b00000010 = 0x02 = 2)

```python
request url:
GET /project/control/ios/sio/si_val?type=sib&sig_no=1

response-body:
{
    "_type" : "JObject",
    "val" : 2,
}
```

Python Script Example

```python
# test.py
import requests

def get_sio_val() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/control/ios/sio/so_val'
    query_parameter = { 'type': 'sob', 'sig_no': 3 }
    
    response = requests.get(url = base_url + path_parameter, params = query_parameter).json()

    return response

print(get_sio_val())
```
```sh
$python test.py
{'_type': 'JObject', 'val': 0}
```