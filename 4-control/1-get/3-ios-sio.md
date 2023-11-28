## 4.1.3 `ios/sio/{sio_val}`

### 설명

`sio` (system input/output)

- `GET` : 시스템 IO 값을 얻습니다.

### path-parameter

```python
GET /project/control/ios/sio/{sio_val}
```

### path-variable

- `sio_val` :
  - `si_val` : 입력(si) 값을 얻습니다.
  - `so_val` : 출력(so) 값을 얻습니다.

### query-parameter

- `type` : io 값의 타입
  - si or so : bit
  - sib or sob : signed-byte
  - siw or sow : signed-word (2byte)
  - sil or sol : signed-dword (4yte)
  - sif or sof : float
- `sig_no` : 신호 인덱스 (0~)


### 사용 예

- sib1 값 얻기. (결과값 : 0b00000010 = 0x02 = 2)

```python
request url:
GET /project/control/ios/sio/si_val?type=sib&sig_no=1

response-body:
{
	"_type" : "JObject",
    "val" : 2,
}
```

Python Script 예시

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