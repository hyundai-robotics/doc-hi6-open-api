#### 1.1.1 `api_ver`

##### Description

在极少数情况下，您的 API 的模式版本可能会更改与控制器或其数据结构的通信方式。  
这可能会导致客户端程序出现问题，因此需要通过相应的功能进行确认。  
如果每个 API 功能的模式版本发生变化，将在描述页面上通过单独的标注进行通知。  

- `GET` : 获取开放 API 版本号

##### path-parameter

```python
GET /api_ver
```

##### response-body

- 开放 API 版本号
- 初始 ${cont_model} 开放 API 是基于 `version 5` 编写的文档。

##### Example

```python
request url:
GET /api_ver

response-body:
5
```

Python Script Example

```python
import requests

def get_api_ver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/api_ver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_api_ver())
```
```sh
$python test.py
5
```