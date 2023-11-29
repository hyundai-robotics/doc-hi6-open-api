## 6.1.1 `relay values`

### 설명

- `GET` : relay 값을 객체.타입 전체에 대해 얻습니다.

### path-parameter

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

### path-variable

[릴레이명](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/korean/3-relay/2-relay-expression) (소문자 표기)

* (`di`, `do`, `x`, `y`에는 `{obj_type}{obj_idx}_`를 지정해야 합니다. 나머지 `relay_type`에는 지정하지 않습니다.)

- `obj_type` : 객체 타입
  - `fb`
  - `fn`

- `obj_idx` : 객체 인덱스 (fb: 0~9, fn: 0~63)

- `relay_type` : 
	|`di`|`do`|`x` |`y` |`m` |`s` |`r`|`k`|
	|:---|:---|:---|:---|:---|:---|:---|:---|

	

### query-parameter

- `st` : 시작 byte index (default: 0)
- `len` : dword 개수 (default: 8)


### 사용 예

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

Python Script 예제

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