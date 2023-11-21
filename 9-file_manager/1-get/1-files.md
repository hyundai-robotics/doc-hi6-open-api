# 9.1.1 `files`

## 설명

`files`

- `GET` : 제어기로부터 파일 내용을 응답 받습니다.

## path-parameter

```python
GET /file_manager/files
```

## query-parameter

- `pathname` : 가져올 파일 이름

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|파일 내용 반환|
|`404 Not Found`| 파일 없을 때 에러 상태 코드 반환|


## 사용 예

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job   <- target
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- hi6_proj.json
```

```python
request url:
GET /file_manager/files?pathname=project/jobs/0001.job

response-body:
{
	Hyundai Robot Job File; { version: 2.0 }
}
```

</blockquote>

<details><summary>Python Script 예시</summary>

```python
# test.py
import requests

def print_file_contents() -> None:
	base_url	    = "http://192.168.1.150:8888"
	path_parameter  = "/file_manager/files"
	query_parameter = {"pathname": "project/jobs/0001.job"}

	response = requests.get(url=base_url + path_parameter, params=query_parameter)
	
	print(f'response: {response.status_code}')
	print(response.text)
```
```sh
$python test.py
response: 200
Hyundai Robot Job File; { version: 2.0 }
```

</details>
