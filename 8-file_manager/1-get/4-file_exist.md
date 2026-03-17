#### 8.1.4 `file_exist`

##### 描述

- `GET` : 获取目标文件的存在性。

##### 路径参数

```python
GET /file_manager/file_exist
```

##### 查询参数

必须输入查询参数。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### 响应主体

- `true` （文件存在）
- `false` （文件不存在）

##### 状态码

- 200 : 请求成功
  - 返回 [文件信息](../../99-schema/file_info) `list`
- 404 : 请求失败
  - 不允许的路径参数


##### 示例

<blockquote>

```python
请求网址：
GET /file_manager/file_exist?pathname=project/jobs/1234.job

响应主体: 
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

Python脚本示例

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
