# 8.2.1 `rename_file`

## 설명

`rename_file`

- `POST` : 타겟 파일의 파일 이름을 변경합니다.

## path-parameter

```python
POST /file_manager/rename_file
```

## request-body

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : 변경 전 파일 경로
- `pathname_to` : 변경 후 파일 경로

## response-body

|HTTP Status|description|
|:---|:---|
|`200`| 이름 변경 완료 |
|`400`| 변경하려는 타겟 파일이 존재하지 않음 |


## 사용 예

<blockquote>

```python
request url:
POST /file_manager/rename_file

request-body: 
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
```
hi6
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def rename_file():
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = { "pathname_from" : "project/jobs/0001.job", 
                        "pathname_to"   : "project/jobs/4321.job" }

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {rename_file()}")
```
```sh
$python test.py
response: 200
```