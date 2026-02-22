#### 8.3.1 `文件 (files)`

##### 描述

- `DELETE` : 删除目标文件或目录。

##### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

##### 状态码

- 200 : 请求成功
  - 目标删除完成

##### 示例

<blockquote>

```python
请求 URL:
DELETE /file_manager/files/project/jobs/special
```
```
${cont_model}
`-- project
    `-- jobs
        `-- test.job   <- 目标
```

</blockquote>

Python 脚本示例

```python
# test.py
import requests

def delete_file() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    target_file     = '/project/jobs/test.job'

    response = requests.delete(url = base_url + path_parameter + target_file)

    return response.status_code

print(f"response: {delete_file()}")
```
```sh
$python test.py
响应：200
```