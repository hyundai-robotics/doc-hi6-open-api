## 5.2.4 `crd_sys`

### 설명

- `POST` : 현재 조그(jog) 좌표계를 설정합니다.

### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/crd_sys
```

### request-body

- [좌표계](../../99-schema/crdsys.md)

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{
		"_type": "JObject",
		"cur_crd": 1,
		"ucrd_no": 1
	}
	```
	</div>

### 사용 예

```json
POST /project/robot/crd_sys

request-body
{
	"val": 1
}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
import requests


def post_crd_sys(x: int = 0) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/crd_sys"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"val": x}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_crd_sys(1))
```
```sh
$python test.py
(200, {'_type': 'JObject', 'cur_crd': 1, 'ucrd_no': 0})
```

</div>