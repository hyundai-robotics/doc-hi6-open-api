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

### response-body


<div style="width: fit-content;">

|HTTP Status|description|
|:---|:---|
|`200 OK`|`true` (파일 존재)|
|`200 OK`|`false` (파일 없음)|

</div>

### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```  

```text
hi6
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

def is_file_exist() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/file_exist'
    query_parameter = {'pathname': 'project/jobs/0001.job'}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.text

print(is_file_exist())
```
```sh
$python test.py
true
```

</div>