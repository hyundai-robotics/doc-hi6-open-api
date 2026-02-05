#### 6.2.2 `ios/dio/{do_val}`

##### 설명

- `POST` : 디지털 출력을 변경합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /project/control/ios/dio/do_val
```
</div>

##### request-body


<div style="width: fit-content;">

```json
{
  "type": "do",
  "blk_no": 1,
  "sig_no": 1,
  "val": 1
}
```
</div>

##### query-parameter

- `type` : io 값의 타입
  - do : bit
  - dob : signed-byte
  - dow : signed-word (2byte)
  - dol : signed-dword (4yte)
  - dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)
- `val` : 변경하고자 하는 설정값


##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_text": ""}
	```
	</div>


##### 사용 예

<div style="width: fit-content;">

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
</div>

Python Script 예시

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.


<div style="width: fit-content;">

```python
# test.py
import requests


def post_do_val() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ios/dio/do_val"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"type": "dob", "blk_no": 2, "sig_no": 3, "val": -99}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_do_val())
```
```sh
$python test.py
(200, {'_text': ''})
```
</div>
