## 8.1.2 `file_info`

### Description

`file_info`

- `GET` : Obtain information about that file based on the file path.

### path-parameter

```python
GET /file_manager/file_info
```

### query-parameter

```
?pathname=project/jobs/0001.job
```
- `pathname` : target file path

### response-body

- [file information](/99-schema/file_info)
- If the file does not exist, `404 Not Found`

### Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job <- target 
    |-- lads
    |-- log
    |-- vars
    |-- ...
    `-- hi6_proj.json
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

</blockquote>

Python Script Example

```python
# test.py
import requests

def get_file_info() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/file_manager/file_info"
    query_parameter  = {"pathname": "project/hi6_proj.json"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(get_file_info())
```
```sh
$python test.py
{'mday': 31, 'sec': 40, 'fname': 'hi6_proj.json', 'wday': 2, 'size': 130551, 'year': 2023, 'hour': 7, 'readonly': False, 'month': 10, 'is_dir': False, 'min': 57}
```