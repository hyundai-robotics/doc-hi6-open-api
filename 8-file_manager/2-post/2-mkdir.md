#### 8.2.2 `mkdir`

##### 描述

- `POST` : 在目标路径中创建目录。

##### 路径参数

```python
GET /file_manager/mkdir
```

##### 请求体

|键|值|描述|
|:---|:---|:---|
|`路径 (path)`|`str`|创建目录的位置|

##### 响应体

- { `路径 (path)`: ${target path} }

##### 状态码

- 200 : 请求成功
  - 目标位置的目录创建完成
- 400 : 请求失败
  - 当目标位置的目录名称重复时

##### 示例

<blockquote>

```python
请求 URL:
GET /file_manager/mkdir

请求体: 
{
	"path" : "project/jobs/special"
}
```

```
${cont_model}
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- ${cont_model:lower}_proj.json
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def post_mkdir() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/mkdir'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = {'path': "project/jobs/special7"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {post_mkdir()}")
```
```sh
$python test.py
response: 200
```
