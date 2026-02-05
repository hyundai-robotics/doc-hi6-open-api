#### 8.2.2 `mkdir`



##### 설명

- `POST` : 타겟 경로에 디렉토리를 생성합니다.  

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/mkdir
```


##### request-body

<div style="width: fit-content;">

- 생성하려는 디렉토리 타겟 위치
	```json
	{ "path" : "project/jobs/special" }
	```

</div>

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - 변경하려는 타겟 파일이 존재하지 않음
   - 403 : Forbidden
   - 404 : Not Found
   - 500 : Internal Server Error
     - 타겟 위치에 디렉토리 이름이 중복되는 경우

2) response-body
   - 생성하려는 디렉토리 타겟 위치
		<div style="width: fit-content;">

		```json
		{ "path" : "project/jobs/special" }
		```
		</div>

##### 사용 예
<div style="width: fit-content;">

```python
request url:
GET /file_manager/mkdir

request-body:
{
    "path" : "project/jobs/special"
}
```

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- hi6_proj.json
```
</div>


Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_mkdir() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/mkdir"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"path": "project/jobs/special"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


try:
    ret = post_mkdir()
    print(ret.status_code, ret.json())
except:
    print(post_mkdir())
```
```sh
$python test.py
200 {'path': 'project/jobs/special'}
```
</div>
