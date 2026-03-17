#### 9.2.2 `task/reset`

##### 描述

- `POST` : 对任务执行重置。  
- 它的操作方式与使用 [RCode 0](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) 相同。
  - <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;"> 任何其他代码都不适用于操作 </span>

##### 路径参数

```python
# 重置所有任务
POST /project/service/r_code/execute
```

##### 请求体

```json
{"code": 0}
```

##### 示例

```python
请求 URL:
POST /project/service/r_code/execute

请求体:
{
    "code":0
}
```

Python 脚本

```python
import requests


def post_rcode_0() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 0}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response.status_code


print(f"response: {post_rcode_0()}")
```
```sh
$python test.py
response: 200
```
