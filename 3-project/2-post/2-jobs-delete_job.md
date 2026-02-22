#### 3.2.2 `delete_job`

##### 描述

- `POST` : 发送请求以删除工作文件。

##### 路径参数

```python
POST /project/jobs/delete_job
```

##### 请求体

```json
{
    "fname": "0001.job"
}
```

##### 示例

```json
请求 URL:
POST /project/jobs/delete_job

请求体: 
{
    "fname": "0001.job"
}
```

Python 脚本示例

```python
# test.py
import requests 

def post_delete_job(file_name: str = "0001.job") -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/jobs/delete_job'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"fname": file_name}
 
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.status_code

print(f"response: {post_delete_job('0002.job')}")
```
```sh
$python test.py
响应：200 
```