#### 9.2.4 `assign_var_json`

##### 描述

- `POST` : 在当前任务语句中重新分配变量。  

##### 路径参数

```python
POST /project/context/tasks[0]/assign_var_json
```

##### 请求体

- `名称 (name)` : 变量名称
- `json` : 要替换为变量的 json 格式 `string`。
- `保存 (save)` : 保存内容 (true/false)。即在您将该数据保存到活动文件之前。
- `范围 (scope)` : 设置变量的有效作用域
	|`local`|`global`|`未设置`|
	|:---|:---|:---|
	|局部变量|全局变量|完整作用域（局部和全局会自动设置）|


```json
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```

##### 示例

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

当上述作业文件被执行并在任务中声明了一个局部变量 `字母a (a)`

```python
request url:
POST /project/context/tasks[0]/assign_var_json

request-body
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

def assign_var_json(var_name: str, scope = None, var_json: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_json"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {
                         "name" : f"{var_name}",
                         "scope": f"{scope}",
                         "json" : f"{var_json}",
                         "save" : "true"
                       }

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"之前: {post_read_var('a', 'local')}")
print(f"""响应: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"之后: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
之前: 1234
响应: 200
之后: {'_type': 'JObject', 'test': 10}
```