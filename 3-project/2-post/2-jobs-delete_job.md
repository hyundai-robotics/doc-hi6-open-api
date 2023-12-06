## 3.2.2 `delete_job`

### Description

`delete_job`

- `POST` : Send a request to remove a working file.

### path-parameter

```python
POST /project/jobs/delete_job
```

### request-body

```json
{
    "fname": "0001.job"
}
```

### Example

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
    "fname": "0001.job"
}
```

Python Script Example

```python
# test.py
import requests 

def post_delete_job(file_name: str = "0001.job") -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/jobs/delete_job'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"fname": file_name}
 
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.status_code

print(f"response: {post_delete_job('0002.job')}")
```
```sh
$python test.py
response: 200 
```