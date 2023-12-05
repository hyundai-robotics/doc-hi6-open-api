## 8.1.3 `file_list`

### 설명

`file_list`

- `GET` : 파일 및 디렉토리 리스트를 반환합니다.

### path-parameter

```python
GET /file_manager/file_list
```

### query-parameter

> query-parameter 를 반드시 입력해야합니다.  
```
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|description|
|:---|:---|
|`path`|확인하려는 대상 폴더 경로|
|`incl_file`|리스트 출력 시 파일 포함 여부|
|`incl_dir`|리스트 출력 시 디렉토리 포함 여부|


### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|[파일 정보](/99-schema/file_info) `리스트`를 반환|
|`404 Not Found`| 파일 없을 때 반환|


### 사용 예

<blockquote>

```text
hi6
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

```python
request url:
GET /file_manager/file_list?path=project&incl_file=true&incl_dir=true

response-body:
[
	{
		"mday": 20,
		"sec": 24,
		"fname": "jobs",
		"wday": 1,
		"size": 8192,
		"year": 2023,
		"hour": 18,
		"readonly": false,
		"month": 11,
		"is_dir": true,
		"min": 12
	},
	{
		"mday": 31,
		"sec": 40,
		"fname": "hi6_proj.json",
		"wday": 2,
		"size": 130551,
		"year": 2023,
		"hour": 7,
		"readonly": false,
		"month": 10,
		"is_dir": false,
		"min": 57
	},
	      ...
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def print_file_list() -> None:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/file_manager/file_list"
    query_parameter = {"incl_file": "true", "incl_dir": "true", "path": "project"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    for x in response.json()[:3]:
        print(x)

print_file_list()
```
```sh
$python final_test.py 
{'mday': 20, 'sec': 8, 'fname': 'jobs', 'wday': 1, 'size': 8192, 'year': 2023, 'hour': 21, 'readonly': False, 'month': 11, 'is_dir': True, 'min': 50}
{'mday': 1, 'sec': 50, 'fname': 'vars', 'wday': 3, 'size': 8192, 'year': 2023, 'hour': 12, 'readonly': False, 'month': 11, 'is_dir': True, 'min': 29}
{'mday': 17, 'sec': 10, 'fname': 'lads', 'wday': 4, 'size': 8192, 'year': 2023, 'hour': 13, 'readonly': False, 'month': 8, 'is_dir': True, 'min': 47}
```