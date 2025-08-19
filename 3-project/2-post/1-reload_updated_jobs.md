## 3.2.1 `reload_updated_jobs`

### 설명

- `POST` : 작업 파일들을 갱신하는 요청을 보냅니다.
- FTP 로 job 파일을 제어기에 전송하는 경우, 해당 API 를 통해 reload 요청을 해야 전송된 job 파일이 메모리에 반영이 됩니다.

### path-parameter

<div style="width: fit-content;">

```python
POST /project/reload_updated_jobs
```

### request-body

```json
{}
```

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	```json
	{'_type': 'JObject'}
	```


### 사용 예

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_reload_updated_jobs() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/reload_updated_jobs"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_reload_updated_jobs())
```
```sh
$python test.py
(200, {'_type': 'JObject'})        
```
</div>