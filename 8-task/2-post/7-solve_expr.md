#### 8.2.7 `solve_expr`

##### Description

- `POST` : 解决表达式并将结果值设置为任务的本地或全局变量。

##### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

##### request-body
- `expr` : 输入您想要求解的表达式
- `scope` : 设置 `expr` 的作用域。

	|`local`|`global`|`not set`|
	|:---|:---|:---|
	|本地变量|全局变量|完整作用域（本地和全局自动设置）|

```json
{
    "expr" : "a",
    "scope" : "local"
}
```

##### response-body

```json
13 // 在当前指定作用域内读取 expr 值。
```

##### Example

<blockquote>

```python
# 1. 读取当前任务中声明的"local"变量 a 的值
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr"  : "a",
    "scope" : "local"
}

response-body:
13
```

</blockquote>

<blockquote>

```python
# 2. 读取当前任务中声明的"global"变量 a 的值
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr"  : "a",
    "scope" : "global"
}

response-body:
10
```

</blockquote>

<blockquote>

```python
# 3. 将 -234 加到本地变量 a 的值
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr": "a + (-234)"
}

response-body:
1000
```

</blockquote>

Python Script Example
- 执行以下代码时，任务区域的本地和全局变量 a 值已设置在机器人控制器中。

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

print(f"{post_read_var('a', 'local')}")
print(f"{post_read_var('a', 'global')}")
print(f"{post_read_var('a + (-234)')}")
```
```sh
$python test.py 
1234
10
1000
```