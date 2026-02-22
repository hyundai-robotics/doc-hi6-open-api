#### 6.1.2 `ios/dio/{dio_val}`

##### 描述

- `GET` : 获取用户 IO 值。
- 请参考 [sio api](./3-ios-sio.md) 以获取系统输入/输出值。

##### 路径参数

```python
GET /project/control/ios/dio/{dio_val}
```

##### 路径变量

- `dio_val` :
  - `di_val` : 获取输入 (di) 值。
  - `do_val` : 获取输出 (do) 值。

##### 查询参数

- `类型 (type)` : IO 值的类型
  - di 或 do : 位
  - dib 或 dob : 有符号字节
  - diw 或 dow : 有符号字 (2byte)
  - dil 或 dol : 有符号双字 (4byte)
  - dif 或 dof : 浮点数
- `blk_no` : 块号 (0~9)
- `sig_no` : 信号索引 (0~)

##### 示例

- 获取 fb2.dob3 值。 (结果 : 0b11001000 = 0xc8 = -56)

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```

Python 脚本示例

```python
# test.py
import requests

BASE_URL = "http://127.0.0.1:8888"


def get_do_val(sig_no: int = 0) -> requests.Response:
    path = "/project/control/ios/dio/do_val"
    params = {"type": "dob", "blk_no": 0, "sig_no": sig_no}
    return requests.get(BASE_URL + path, params=params)


def get_di_val(sig_no: int = 0) -> requests.Response:
    path = "/project/control/ios/dio/di_val"
    params = {"type": "dib", "blk_no": 0, "sig_no": sig_no}
    return requests.get(BASE_URL + path, params=params)


def extract_u8(res: requests.Response) -> int:
    assert res is not None, "response is necessary."

    res.raise_for_status()

    payload = res.json()
    if "val" not in payload:
        raise KeyError(f"no 'val' in response: {payload}")

    # MSB (最高有效位) -> LSB (最低有效位)
    return int(payload["val"]) & 0xFF


def lsb_first(u8: int) -> str:
    # LSB -> MSB
    return format(u8, "08b")[::-1]


do_u8 = extract_u8(get_do_val(2))
di_u8 = extract_u8(get_di_val(1))

print("do 值:", lsb_first(do_u8))
print("di 值:", lsb_first(di_u8))

```
# (当 fb0.do18 = 1, fb0.do20 = 1 / fb0.di14 = 1)
$python test.py
do 值: 00101000
di 值: 00000010