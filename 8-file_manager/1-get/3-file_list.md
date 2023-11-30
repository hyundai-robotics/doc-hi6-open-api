## 8.1.3 `file_list`

### Description

`file_list`

- `GET` : Obtain a list of files and directories.

### path-parameter

```python
GET /file_manager/file_list
```

### query-parameter

> query-parameter must be entered.
```
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|description|
|:---|:---|
|`path`|Target path you want to check|
|`incl_file`|Whether to include files when outputting the list|
|`incl_dir`|Whether to include directories when outputting the list|


### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|return [file information](/99-schema/file_info) `list`|
|`404 Not Found`| no file exists |


### Example

<blockquote>

```
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

Python Script Example

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