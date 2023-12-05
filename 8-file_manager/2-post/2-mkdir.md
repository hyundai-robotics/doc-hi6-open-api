## 8.2.2 `mkdir`

### 설명

`mkdir`

- `POST` : 타겟 경로에 디렉토리를 생성합니다.

### path-parameter

```python
GET /file_manager/mkdir
```

### request-body

|key|value|description|
|:---|:---|:---|
|`path`|`str`|디렉토리를 생성할 위치|

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| 타겟 위치에 디렉토리 생성 완료 |
|`500 Internal Server Error`| 타겟 위치에 디렉토리 이름이 중복되는 경우 |


### 사용 예

<blockquote>

```python
request url:
GET /file_manager/mkdir

request-body: 
{
	"path" : "project/jobs/special"
}
```

```
hi6
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- hi6_proj.json
```


</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_mkdir() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/mkdir'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = {'path': "project/jobs/special7"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {post_mkdir()}")
```
```sh
$python test.py
response: 200
```