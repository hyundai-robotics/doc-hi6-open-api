## 6.1.2 `ios/dio/{dio_val}`

### 설명

- `GET` : 사용자 IO 값을 얻습니다.
- 시스템 입출력에 대한 값은 [sio api](./3-ios-sio.md)를 참조하십시오.

### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ios/dio/{dio_val}
```  
</div>

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

### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- 정상 응답 시 signed decimal 값 반환
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : -99}
		```
		</div>
	- 값은 내부적으로 2의 보수로 처리되며, TP 화면에는 해당 값의 하위 8비트로 표시됩니다.
    	- TP 창조정 > 범용 출력 화면에서는 1은 녹색 신호, 0은 신호 없음을 뜻합니다.


### 사용 예

- fb2.dob3 값 얻기. (결과값 : 0b11001000 = 0xc8 = -56)

<div style="width: fit-content;">

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_dio_val() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ios/dio/do_val"
    query_parameter = {"type": "dob", "blk_no": 2, "sig_no": 3}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


ret = get_dio_val()
print(ret)
print(format(ret[1]["val"] & 0xFF, "08b"))
```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': -99})
10011101 # TP > fb2/9.do's 4th row => 1011001
```
</div>