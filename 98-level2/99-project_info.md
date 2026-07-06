#### 3.1.2 `project_info`

##### 描述

- `GET` : 检索关于项目的信息。

##### path-parameter

```python
GET /project/project_info
```

##### request-body

```json
{}
```

##### response

1. 状态码

* 200 : OK
* 400 : 错误请求
* 404 : 未找到

2. response-body

```json
{
  "_type": "JObject",
  "project_file_exist": true,
  "n_files_in_jobs": 9,
  "n_files_in_vars": 2,
  "n_files_in_lads": 0
}
```

3. 错误代码

* 无

##### 示例

```python
GET /project/project_info

request-body:
{}
```

Python 脚本示例

```python
import requests

def get_project_info() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/project_info'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.get(url = base_url + path_parameter, headers = head, json = body).json()
    return response

print(get_project_info())
```

```sh
$python test.py
{'_type': 'JObject', 'project_file_exist': True, 'n_files_in_jobs': 9, 'n_files_in_vars': 2, 'n_files_in_lads': 0}
```