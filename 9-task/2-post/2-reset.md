## 9.2.2 `task/reset`

### Description

- `POST` : Perform a reset on the task. (Same operation as R.. 0 ENTER)

### path-parameter

```python
# reset all the tasks
POST /project/context/tasks/reset 

# reset the selected task
POST /project/context/tasks[{task index}]/reset 
```

### request-body

```json
{}
```

### Example

reset task 0

```python
request url:
GET /project/context/tasks[0]/reset
```

Python Script

```python
import requests

def post_task_reset() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/reset'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_task_reset()}")
```
```sh
$python test.py
response: 200
```