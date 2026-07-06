#### 7.1.2 `file_info`

##### 描述

- `GET` : 根据文件路径获取该文件的信息。

##### path-parameter

```python
GET /file_manager/file_info
```

##### query-parameter

query-parameter 必须填写。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### response-body

- [文件信息](../../99-schema/file_info)
- 如果文件不存在，`404 Not Found`

##### 示例

<blockquote>

```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job <- 目标 
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

</blockquote>

Python 脚本示例

```python
# test.py
import requests

def get_file_info() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/file_manager/file_info"
    query_parameter  = {"pathname": "project/${cont_model:lower}_proj.json"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(get_file_info())
```
```sh
$python test.py
{'mday': 31, 'sec': 40, 'fname': '${cont_model:lower}_proj.json', 'wday': 2, 'size': 130551, 'year': 2023, 'hour': 7, 'readonly': False, 'month': 10, 'is_dir': False, 'min': 57}
```