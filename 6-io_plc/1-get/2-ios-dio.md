#### 6.1.2 `ios/dio/{dio_val}`

##### 설명

- `GET` : 사용자 IO 값을 얻습니다.
- 시스템 입출력에 대한 값은 [sio api](./3-ios-sio.md)를 참조하십시오.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ios/dio/{dio_val}
```
</div>

##### path-variable

- `dio_val` :
  - `di_val` : 입력(di) 값을 얻습니다.
  - `do_val` : 출력(do) 값을 얻습니다.

##### query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)

##### response
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


##### 사용 예

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

    # MSB (Most Significant Bit) -> LSB (Least Significant Bit)
    return int(payload["val"]) & 0xFF


def lsb_first(u8: int) -> str:
    # LSB -> MSB
    return format(u8, "08b")[::-1]


do_u8 = extract_u8(get_do_val(2))
di_u8 = extract_u8(get_di_val(1))

print("do value:", lsb_first(do_u8))
print("di value:", lsb_first(di_u8))

```
```sh
# (when fb0.do18 = 1, fb0.do20 = 1 / fb0.di14 = 1)
$python test.py
do value: 00101000
di value: 00000010
```

</div>
