#### 7.2.3 `文件 (files)`

##### Description

- `POST` : 将文件传输到目标路径。

##### path-parameter

```python
POST /file_manager/files/{target_filepath}
```

##### path-variable

- `target_filepath` : 包含扩展名的目标文件路径。

##### request-body

- `Content-Type` 必须为 `application/octet-stream`。

##### status code

- 200 : 请求成功
  - 传输完成

##### Example

<blockquote>

```
${cont_model}
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
POST /file_manager/files/project/jobs/test.job
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def post_file_transfer() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    path_value      = '/project/jobs/test.job' #### target

    target_file     = base_url + path_parameter + path_value
    source_file     = 'D:\\temp\\test.job' #### source (path for WindowOS)

    with open(source_file, 'rb') as file:
        response = requests.post(url=target_file, 
                                 data=file, 
                                 headers={'Content-Type': 'application/octet-stream'})

    return response.status_code

print(f"response: {post_file_transfer()}")
```
```sh
$python test.py
response: 200
```