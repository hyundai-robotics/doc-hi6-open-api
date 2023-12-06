## 4.1.2 `ios/dio/{dio_val}`

### 설명

`dio` (digital input/output)

- `GET` : 사용자 IO 값을 얻습니다.

### path-parameter

```python
GET /project/control/ios/dio/{dio_val}
```

### path-variable

- `dio_val` :
  - `di_val` : 입력(di) 값을 얻습니다.
  - `do_val` : 출력(do) 값을 얻습니다.

### query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)

### 사용 예

- fb2.dob3 값 얻기. (결과값 : 0b11001000 = 0xc8 = -56)

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```

Python Script 예시

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