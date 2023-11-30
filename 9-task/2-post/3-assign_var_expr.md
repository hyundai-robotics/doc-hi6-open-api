## 9.2.4 `assign_var_expr`

### Description

`assign_var_expr`

- `POST` : Reassigns a variable in the current task statement.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

### request-body

- `name` : variable name
- `expr` : expression to substitute into variable
- `save` : Whether to save (true/false). This is to save the data in the variable file.
- `scope` : Setting the effective scope of the variable
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

### Example

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

When the above job file is executed and a local variable `a` is declared in the task

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

Python Script Example

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