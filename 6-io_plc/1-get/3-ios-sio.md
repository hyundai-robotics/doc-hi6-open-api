### 6.1.3 `ios/sio/{sio_val}`

#### 설명

- `GET` : 시스템 IO 값을 얻습니다.

#### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ios/sio/{sio_val}
```

#### path-variable

- `sio_val` :
  - `si_val` : 입력(si) 값을 얻습니다.
  - `so_val` : 출력(so) 값을 얻습니다.

#### query-parameter

- `type` : io 값의 타입
  - si or so : bit
  - sib or sob : signed-byte
  - siw or sow : signed-word (2byte)
  - sil or sol : signed-dword (4yte)
  - sif or sof : float
- `sig_no` : 신호 인덱스 (0~)

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- 정상 응답 시 decimal 값 반환
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : 6}
		```
		</div>
		이를 binary 로 표현하면 0b0110 으로, 시스템 출력의 둘째,셋째 칸에 녹색 불이 들어오게 됨

#### 사용 예

- sob2 값 얻기. (결과값 : 6 = 0x06 = 0b0110)

```python
request url:
GET /project/control/ios/sio/si_val?type=sob&sig_no=2

response-body:
{
    "_type" : "JObject",
    "val" : 2,
}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_sio_val() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ios/sio/so_val"
    query_parameter = {"type": "sob", "sig_no": 2}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_sio_val())
```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': 6})
```
</div>
