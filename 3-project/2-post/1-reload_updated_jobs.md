## 3.2.1 `reload_updated_jobs`

### 설명

`reload_updated_jobs`

- `POST` : 작업 파일들을 갱신하는 요청을 보냅니다.

### path-parameter

```python
POST /project/reload_updated_jobs
```

### request-body

```json
{}
```

### 사용 예

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```

Python Script 예시

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.
```python
# test.py
import requests 

def post_reload_updated_jobs() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/reload_updated_jobs'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_reload_updated_jobs()}")
```
```sh
$python test.py
response: 200 
```
