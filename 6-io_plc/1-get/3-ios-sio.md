#### 6.1.3 `ios/sio/{sio_val}` 

##### 描述

- `GET` : 获取系统 IO 值。

##### 路径参数

```python
GET /project/control/ios/sio/{sio_val}
```

##### 路径变量

- `sio_val` :
  - `si_val` : 获取输入 (si) 值。
  - `so_val` : 获取输出 (so) 值。

##### 查询参数

- `类型 (type)` : IO 值的类型
  - si 或 so : 位
  - sib 或 sob : 有符号字节
  - siw 或 sow : 有符号字 (2字节)
  - sil 或 sol : 有符号双字 (4字节)
  - sif 或 sof : 浮点数
- `sig_no` : 信号索引 (0~)

##### 示例

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

Python 脚本示例

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