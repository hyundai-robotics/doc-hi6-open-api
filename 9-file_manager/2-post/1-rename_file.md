# 9.2.1 `rename_file`

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
|`200 OK`| 타겟 파일이 없어도 동작함 |
|`1 Unknown`| 타겟 파일의 이름 변경 완료 |


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

<details><summary>Python Script 예시</summary>

```python
# test.py
import requests

def rename_file() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    query_parameter = { "pathname_from" : "project/jobs/0001.job", 
                       "pathname_to"   : "project/jobs/4321.job" }

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.status_code

print(rename_file())
```
```sh
$python test.py
파일 이름이 정상적으로 변경되면, 에러 로그가 출력됨
없는 파일의 이름을 바꾸려고 시도하면 200 OK 가 출력됨
```

</details>
