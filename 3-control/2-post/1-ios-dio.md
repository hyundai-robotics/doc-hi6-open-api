# 3.1.2 `ios/dio/{do_val}`

## 설명

`do` (digital output)

- `POST` : 디지털 출력을 변경합니다.

## path-parameter

```python
POST /project/control/ios/dio/do_val
```

## request-body

```json
{
  "type": "do",
  "blk_no": 1,
  "sig_no": 1,
  "val": 1
}
```


## query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)
- `val` : 변경하고자 하는 설정값


## 사용 예

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
<details><summary>Python Script 예시</summary>

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.
```python
# test.py
import requests 

def post_do_val() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ios/dio/do_val'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"type": "dob", "blk_no": 2, "sig_no": 3,"val": -99}

    response = requests.post(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {post_do_val()}")
```
```sh
$python test.py
response: 200 
```
</details>
