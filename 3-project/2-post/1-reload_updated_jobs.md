#### 3.2.1 `reload_updated_jobs`

##### 描述

- `POST` : 发送请求以更新工作文件。
- 在通过 FTP 将作业文件传输到控制器时，必须通过相应的 API 发起重载请求，以使传输的作业文件在内存中反映。

##### 路径参数

```python
POST /project/reload_updated_jobs
```

##### 请求体

```json
{}
```

##### 描述

```python
请求 URL:
POST /project/reload_updated_jobs

请求体: {}
```

Python 脚本示例

- 请参考 [here](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200) 以获取响应的 HTTP 状态码。
```python
# test.py
import requests 

def post_reload_updated_jobs() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/reload_updated_jobs'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_reload_updated_jobs()}")
```
```sh
$python test.py
response: 200 
```