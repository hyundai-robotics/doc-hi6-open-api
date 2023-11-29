## 9.2.2 `task/reset`

### 설명

- `POST` : 태스크에 대해 리셋을 수행합니다. (R.. 0 ENTER 와 같은 동작)

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

### 사용 예

0번 태스크 리셋 하기.

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