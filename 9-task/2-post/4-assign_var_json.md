## 9.2.5 `assign_var_json`

### Description

`assign_var_json`

- `POST` : Reassigns a variable in the current task statement.  

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

### request-body

- `name` : variable name
- `json` : A json format `string` to be substituted into a variable.
- `save` : Save contents (true/false). That is until you save that data to your activity file.
- `scope` : Setting the effective scope of the variable
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|


```json
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
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

print(f"before: {post_read_var('a', 'local')}")
print(f"""response: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
before: 1234
response: 200
after: {'_type': 'JObject', 'test': 10}
```