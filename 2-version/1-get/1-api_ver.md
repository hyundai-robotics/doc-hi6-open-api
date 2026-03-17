#### 2.1.1 `api_ver`

##### 描述

在少数情况下，您的 API 的架构版本可能会更改与控制器的通信方式或其数据结构。  
这可能导致客户端程序出现问题，因此需要通过相应的功能进行确认。  
如果每个 API 函数的架构版本发生更改，将通过描述页面上的单独标注进行通知。  

- `GET` : 获取 Open API 版本号

##### path-parameter

```python
GET /api_ver
```

##### response-body

- Open API 版本号
- 初始 ${cont_model} Open API 是基于 `version 5` 编写的文档。

##### 示例

```python
request url:
GET /api_ver

response-body:
5
```

Python 脚本示例

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