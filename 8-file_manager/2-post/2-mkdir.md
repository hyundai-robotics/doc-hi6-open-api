#### 8.2.2 `mkdir`

##### Description

- `POST` : 在目标路径中创建目录。

##### path-parameter

```python
GET /file_manager/mkdir
```

##### request-body

|key|value|description|
|:---|:---|:---|
|`路径 (path)`|`str`|创建目录的位置|

##### response-body

- { `路径 (path)`: ${target path} }

##### status code

- 200 : 请求成功
  - 在目标位置完成目录创建
- 400 : 请求失败
  - 当目标位置的目录名称重复时

##### Example

<blockquote>

```python
request url:
GET /file_manager/mkdir

request-body: 
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

Python Script Example

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