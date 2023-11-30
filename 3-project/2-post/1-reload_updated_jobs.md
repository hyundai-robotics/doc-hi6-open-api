## 3.2.1 `reload_updated_jobs`

### Description

`reload_updated_jobs`

- `POST` : Send a request to update working files.
- When transmitting a job file to the controller via FTP, a reload request must be made through the corresponding API for the transmitted job file to be reflected in memory.

### path-parameter

```python
POST /project/reload_updated_jobs
```

### request-body

```json
{}
```

### Description

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```

Python Script Example

- Please refer to [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) for the response HTTP status code.
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
