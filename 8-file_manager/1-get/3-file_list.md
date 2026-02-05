### 8.1.3 `file_list`

#### 설명

- `GET` : 파일 및 디렉토리 리스트를 반환합니다.

#### path-parameter


<div style="width: fit-content;">

```python
GET /file_manager/file_list
```

#### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```  
</div>


<div style="width: fit-content;">

|key|description|
|:---|:---|
|`path`|확인하려는 대상 폴더 경로|
|`incl_file`|리스트 출력 시 파일 포함 여부|
|`incl_dir`|리스트 출력 시 디렉토리 포함 여부|

</div>

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 파일 리스트를 반환
   - 	e.g.
		<div style="width: fit-content;">

		```json
		{"mday": 11, "fname": "hi6_proj.json", "month": 8, "is_dir": False, "min": 51, "size": 144513, "nfiles": 0, "year": 2025, "readonly": False, "sec": 38, "nfolders": 0, "hour": 14, "wday": 1}
		```
		</div>
   - 파일이 없을 시 `404 Not Found`


#### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
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
]
```

</div>

<div style="width: fit-content;">

Python Script 예시

```python
import requests


def print_file_list() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/file_list"
    query_parameter = {"incl_file": "true", "incl_dir": "true", "path": "project/jobs"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(print_file_list())
```
```sh
$python final_test.py
(200, [{'mday': 18, 'fname': '0002.job', 'month': 7, 'is_dir': False, 'min': 8, 'size': 543, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 44, 'nfolders': 0, 'hour': 14, 'wday': 5}, {'mday': 18, 'fname': '0003.job', 'month': 7, 'is_dir': False, 'min': 8, 'size': 1043, 
                                ...
, {'mday': 19, 'fname': '0001.job', 'month': 8, 'is_dir': False, 'min': 42, 'size': 198, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 6, 'nfolders': 0, 'hour': 7, 'wday': 2}])

```
</div>
