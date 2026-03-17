## 3.1.2 `project_info`

### 说明

- `GET` : 接收项目相关信息的函数。

### path-parameter

```python
GET /project/project_info
```

### response-body

- [项目相关信息](../../99-schema/project_info.md)
### 使用示例

<blockquote>

```python
request url:
GET /project/project_info

response-body:
{
  "_type": "JObject",
  "project_file_exist": true,
  "n_files_in_jobs": 9,
  "n_files_in_vars": 2,
  "n_files_in_lads": 0
}
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def get_project_info() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/project_info"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_project_info())
```
```sh
$python test.py
{'_type': 'JObject', 'project_file_exist': True, 'n_files_in_jobs': 9, 'n_files_in_vars': 2, 'n_files_in_lads': 0}
```