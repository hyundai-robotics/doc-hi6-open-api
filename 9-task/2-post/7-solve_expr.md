#### 9.2.7 `solve_expr`

##### 描述

- `POST` : 求解表达式并将结果值设置为任务的本地或全局变量。

##### 路径参数

```python
POST /project/context/tasks[0]/solve_expr
```

##### 请求体
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

##### 响应体

```json
13 // 读取当前指定作用域内的 expr 值。
```

##### 示例

<blockquote>

```python
# 1. 读取当前任务中声明的 "local" 变量 a 的值
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr"  : "a",
    "scope" : "local"
}

响应体:
13
```
</blockquote>

<blockquote>

```python
# 2. 读取在当前任务中声明的 "global" 变量 a 的值
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr"  : "a",
    "scope" : "global"
}

响应体:
10
```

</blockquote>

<blockquote>

```python
# 3. 将 -234 加到局部变量 a 的值上
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr": "a + (-234)"
}

响应体:
1000
```

</blockquote>

Python 脚本示例
- 在机器人控制器的任务区域中设置局部和全局变量 a 的值，执行以下代码。

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