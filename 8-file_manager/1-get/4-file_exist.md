#### 8.1.4 `file_exist`

##### 描述

- `GET` : 获取目标文件的存在性。

##### path-parameter

```python
GET /file_manager/file_exist
```

##### query-parameter

query-parameter 必须输入。

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### response-body

- `true` (文件存在)
- `false` (没有文件存在)

##### 状态码

- 200 : 请求成功
  - 返回 [file information](../../99-schema/file_info) `list`
- 404 : 请求失败
  - 不允许的 path-parameter


##### 示例

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```
```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
```

</blockquote>

Python 脚本示例

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