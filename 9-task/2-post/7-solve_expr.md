## 9.2.7 `solve_expr`

### Description

`solve_expr`

- `POST` : Solve the expression and set the resulting value to a local or global variable of the task.

### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

### request-body
- `expr` : Enter the expression you want to solve
- `scope` : Sets the scope for `expr`.

	|`local`|`global`|`not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|

```json
{
	"expr" : "a",
	"scope" : "local"
}
```

### response-body

```json
13 // Reads the expr value within the currently specified scope.
```

### Example

<blockquote>

```python
# 1. Read the value of “local” variable a declared in the current Task
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
# 2. Read the value of “global” variable a declared in the current Task
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
# 3. Add -234 to the value of local variable a
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
- Execute the following code with the local and global variable a values set in the task area of the robot controller.

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