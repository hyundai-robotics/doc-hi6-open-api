#### 8.2.1 `rename_file`

##### 描述

- `POST` : 更改目标文件的文件名。

##### 路径参数

```python
POST /file_manager/rename_file
```

##### 请求体

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : 更改前的文件路径
- `pathname_to` : 更改后的文件路径

##### 状态码

- 200 : 请求成功
  - 一切正常
- 400 : 请求失败
  - 没有文件存在可以重命名

##### 示例

<blockquote>

```python
请求网址:
POST /file_manager/rename_file

请求体: 
{
    "pathname_from" : "project/jobs/0001.job",
    "pathname_to"   : "project/jobs/4321.job"
}
```
```
${cont_model}
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def rename_file():
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = { "pathname_from" : "project/jobs/0001.job", 
                        "pathname_to"   : "project/jobs/4321.job" }

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {rename_file()}")
```
```sh
$python test.py
response: 200
```