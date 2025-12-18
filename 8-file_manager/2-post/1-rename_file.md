## 8.2.1 `rename_file`

<div style="width: fit-content;">

### 설명

- `POST` : 타겟 파일의 파일 이름을 변경합니다.

### path-parameter

```python
POST /file_manager/rename_file
```

### request-body

```json
{
    "pathname_from" : "project/jobs/0001.job",
    "pathname_to"   : "project/jobs/4321.job"
}
```


- `pathname_from` : 변경 전 파일 경로
- `pathname_to` : 변경 후 파일 경로

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - 변경하려는 타겟 파일이 존재하지 않음
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 변경하려는 파일 경로와 변경되었을 때의 파일 경로를 응답
	 <div style="width: fit-content;">

		```json
		{"pathname_from": "project/jobs/0001.job", "pathname_to": "project/jobs/0882.job"}
		```
	</div>


### 사용 예

<div style="width: fit-content;">

```python
request url:
POST /file_manager/rename_file

request-body: 
{
    "pathname_from" : "project/jobs/0001.job",
    "pathname_to"   : "project/jobs/4321.job"
}
```

```text
${cont_model}
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests

def rename_file() -> requests.Response:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = { "pathname_from" : "project/jobs/0001.job",
                        "pathname_to"   : "project/jobs/4321.job" }

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

try:
    ret = rename_file()
    print(ret.status_code, ret.json())
except:
    print(rename_file())
```
```sh
$python test.py
(200, {'pathname_from': 'project/jobs/0001.job', 'pathname_to': 'project/jobs/4321.job'})
```

</div>