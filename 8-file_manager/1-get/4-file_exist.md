## 8.1.4 `file_exist`

### 설명

- `GET` : 타겟 파일의 존재 여부를 반환합니다.

### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/file_exist
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

</div>

### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 파일 존재 여부에 대한 bool 값 (True/False) 반환

### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```  

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_file_contents() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_contents())
```
```sh
$python test.py
True
```

</div>