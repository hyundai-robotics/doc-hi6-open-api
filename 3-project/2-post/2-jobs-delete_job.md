#### 3.2.2 `delete_job`

##### 설명

- `POST` : 작업 파일을 제거하는 요청을 보냅니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/jobs/delete_job
```

##### request-body

```json
{
  "fname": "0001.job"
}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   ```json
	{}
	```

##### 사용 예

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
	"fname": "0001.job"
}
```

</div>

Python Script 예시


<div style="width: fit-content;">

```python
#test.py
import requests


def post_delete_job(file_name: str = "0001.job") -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/jobs/delete_job"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"fname": file_name}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_delete_job())
```
```sh
$python test.py
(200, {})
```
</div>
