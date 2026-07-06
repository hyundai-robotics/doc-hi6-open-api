#### 8.2.3 `assign_var_expr`

##### Description

- `POST` : 在当前任务语句中重新分配变量。

##### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

##### request-body

- `名称 (name)` : 变量名
- `expr` : 要替代到变量中的表达式
- `保存 (save)` : 是否保存（true/false）。这是为了保存变量文件中的数据。
- `scope` : 设置变量的有效作用域
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|局部变量|全局变量|完整作用域（局部和全局自动设置）|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

##### Example

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

当上述作业文件被执行，并在任务中声明了一个局部变量 ` (a)`

```python
request url:
POST /project/context/tasks[0]/assign_var_expr

request-body
{
    "name" : "a",
    "scope": "local",
    "expr" : "465 + 312",
    "save" : "true"
}
```

</blockquote>

Python脚本示例

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

def assign_var_expr(var_name: str, scope = None, expression: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_expr"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"name": f"{var_name}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"before: {post_read_var('a', 'local')}")
print(f"response: {assign_var_expr('a', 'local', '465 + 312')}")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
before: 1234
response: 200
after: 777   
```