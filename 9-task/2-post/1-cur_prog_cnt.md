﻿## 9.2.1 `task/cur_prog_cnt`

### Description

`cur_prog_cnt` (current program counter)

- `POST` : Sets the current program counter for the task.

### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

### request-body

- [cur_prog_cnt request parameter](../../99-schema/cur_prog_cnt.md)

### response-body

- [cur_prog_cnt response parameter](../../99-schema/cur_prog_cnt.md)

### Example

```python
request url:
POST /project/context/tasks[0]/cur_prog_cnt

request-body:
{
    "pno":-1,
    "sno":-1,
    "fno":-1,
    "ext_sel":0
}
```

Python Script Example

```python
import requests

def post_cur_prog_cnt() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/cur_prog_cnt'
    headers        = { 'Content-Type': 'application/json; charset=utf-8' }
    body           = {"pno":-1, "sno":-1, "fno":-1, "ext_sel":0 }

    response = requests.request("POST", base_url + path_parameter, headers=headers, json=body)

    return response.json()

print(post_cur_prog_cnt())
```
```sh
$python python test.py
{'_type': 'JObject', 'sno_new': 0, 'fno_new': 2, 'ln_new': 2, 'ofs_moved': 0}
```