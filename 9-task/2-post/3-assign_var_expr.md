#### 9.2.3 `assign_var_expr`

##### 描述

- `POST` : 在当前任务语句中重新分配一个变量。

##### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

##### request-body

- `名称 (name)` : 变量名称
- `expr` : 代入变量的表达式
- `保存 (save)` : 是否保存（true/false）。这是为了将数据保存在变量文件中。
- `scope` : 设置变量的有效范围
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|局部变量|全局变量|完整范围（局部和全局自动设置）|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
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

当上述作业文件被执行并在任务中声明一个局部变量 `字母a (a)`

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

def assign_var_expr(var_name: str, scope = None, expression: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_expr"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"name": f"{var_name}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"之前: {post_read_var('a', 'local')}")
print(f"响应: {assign_var_expr('a', 'local', '465 + 312')}")
print(f"之后: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
之前: 1234
响应: 200
之后: 777   
```