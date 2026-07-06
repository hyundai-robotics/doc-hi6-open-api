#### 4.2.3 `tool_no`

##### 설명

- `POST` : 현재 툴 번호를 설정합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /project/robot/tool_no
``` 

##### request-body

- `val` : 툴 번호
  - `로봇 툴` : `0` ~ `31`
  - `정치 툴` : `0` ~ `3`

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	```json
	{ "_type": "JObject"}
	```

##### 사용 예

```json
POST /project/robot/tool_no

request-body
{
	"val": 1
}
```

</div>

Python Script 예시



```python
import requests


def set_tool_no(tool_no: int = 0) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace

    url = f"{base_url}/project/robot/tool_no"
    body = {"val": tool_no}

    response = requests.post(url, json=body)
    return response


print(set_tool_no(tool_no=1))

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>
