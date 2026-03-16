#### 8.1.2 `file_info`

##### 설명

- `GET` : 파일 경로를 기반으로 해당 파일에 대한 정보를 반환합니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/file_info
```

##### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

</div>

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [파일 정보](../../99-schema/file_info.md)
   - 	e.g.
		<div style="width: fit-content;">

		```json
		{"mday": 11, "fname": "${cont_model:lower}_proj.json", "month": 8, "is_dir": False, "min": 51, "size": 144513, "nfiles": 0, "year": 2025, "readonly": False, "sec": 38, "nfolders": 0, "hour": 14, "wday": 1}
		```
		</div>
   - 파일이 없을 시 `404 Not Found`

##### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job <- target 
    |-- lads
    |-- log
    |-- vars
    |-- ...
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
GET /file_manager/file_info?pathname=project/jobs/0001.job

response-body:
{
    "mday": 10,
    "sec": 52,
    "fname": "0001.job",
    "wday": 5,
    "size": 40,
    "year": 2023,
    "hour": 8,
    "readonly": false,
    "month": 11,
    "is_dir": false,
    "min": 35
}
```
</div>


<div style="width: fit-content;">

Python Script 예시

```python
# test.py
import requests


def get_file_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/file_info"
    query_parameter = {"pathname": "project/${cont_model:lower}_proj.json"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_info())
```
```sh
$python test.py
(200, {'mday': 11, 'fname': '${cont_model:lower}_proj.json', 'month': 8, 'is_dir': False, 'min': 51, 'size': 144513, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 38, 'nfolders': 0, 'hour': 14, 'wday': 1})
```

</div>
