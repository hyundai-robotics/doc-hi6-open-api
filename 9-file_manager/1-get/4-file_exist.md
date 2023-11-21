# 9.1.4 `file_exist`

## 설명

`file_exist`

- `GET` : 타겟 파일의 존재 여부를 반환합니다.

## path-parameter

```python
GET /file_manager/file_exist
```

## query-parameter

|key|value type|description|
|:---|:---|:---|
|`pathname`|`str`| 타겟 파일 경로 |

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|`true` (파일 존재)|
|`200 OK`|`false` (파일 없음)|


## 사용 예

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```

</blockquote>

<details><summary>Python Script 예시</summary>

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

</details>
