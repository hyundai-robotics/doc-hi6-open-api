#### 7.2.1 `rename_file`

##### Description

- `POST` : 更改目标文件的文件名。

##### path-parameter

```python
POST /file_manager/rename_file
```

##### request-body

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : 更改前的文件路径
- `pathname_to` : 更改后的文件路径

##### status code

- 200 : 请求成功
  - 工作正常
- 400 : 请求失败
  - 找不到要重命名的文件


##### Example

<blockquote>

```python
request url:
POST /file_manager/rename_file

request-body: 
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

Python Script Example

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