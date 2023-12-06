## 9.2.3 `set_cur_pc_idx`

### Description

`set_cur_pc_idx`

- `POST` : Function that positions the current cursor at the index line

### path-parameter

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

### request-body
```json
{
    "idx": 1
}
```

### Example

<blockquote>

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
    "idx": 2
}
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def set_cur_pc_idx() -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/set_cur_pc_idx"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"idx": 1}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {set_cur_pc_idx()}")
```
```sh
$python test.py 
response 200 # Cursor position on TP changed
```