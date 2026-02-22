#### 8.1.3 `file_list`

##### 描述

- `GET` : 获取文件和目录的列表。

##### path-parameter

```python
GET /file_manager/file_list
```

##### query-parameter

必须输入 query-parameter。  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|描述|
|:---|:---|
|`路径 (path)`|您想检查的目标路径|
|`incl_file`|在输出列表时是否包括文件|
|`incl_dir`|在输出列表时是否包括目录|


##### 状态码

- 200 : 请求成功
  - 返回 [文件信息](../../99-schema/file_info) `list`
- 403 : 请求失败
  - 没有文件存在


##### 示例

<blockquote>

```
${cont_model}
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

```python
请求 URL:
GET /file_manager/file_list?path=project&incl_file=true&incl_dir=true

响应主体:
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
</blockquote>

Python 脚本示例

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