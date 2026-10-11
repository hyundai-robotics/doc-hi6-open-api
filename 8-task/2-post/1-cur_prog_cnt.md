#### 8.2.1 `task/cur_prog_cnt`

##### Description

- `POST` : Sets the current program counter for the task.

##### path-parameter

```python
POST /project/context/tasks/0/cur_prog_cnt
```

- `0` is the task index. This path sets the program counter for task 0.

##### request-body

- [cur_prog_cnt request parameter](../../99-schema/cur_prog_cnt.md)
- In remote mode, use external selection (`ext_sel: 1`).
- In manual mode, internal selection (`ext_sel: 0`) is available. Internal selection is prohibited in remote mode.
- Send the request while the program is stopped. This API only sets the program counter; it does not start program execution or robot motion.

##### response

1) Status code
   - 200: OK
   - 400: Bad Request
     - The request body failed validation.
     - Requesting external selection (`ext_sel: 1`) in manual mode may also return 400 with `err_code: -1114208`.
   - 403: Forbidden
     - The request is not permitted. A negative `err_code` is returned.
   - 404: Not Found

2) Response body
   - [cur_prog_cnt response parameter](../../99-schema/cur_prog_cnt.md)

3) Error code
   - -1114208: External selection (`ext_sel: 1`) was requested outside remote mode.
   - -1442080: Cannot apply while the program is playing back.
   - -1245280: Invalid program counter.

   After starting/stopping a program via the API, an invalid program counter error may occur. Move the cursor to the top (`idx: 1`) with `set_cur_pc_idx` before retrying.

##### Example

This example uses internal selection in manual mode. To use external selection in remote mode, set `ext_sel` to `1`.

```python
request url:
POST /project/context/tasks/0/cur_prog_cnt

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
    path_parameter = '/project/context/tasks/0/cur_prog_cnt'
    headers        = { 'Content-Type': 'application/json; charset=utf-8' }
    body           = {"pno":-1, "sno":-1, "fno":-1, "ext_sel":0 }

    response = requests.request("POST", base_url + path_parameter, headers=headers, json=body)

    return response.json()

print(post_cur_prog_cnt())
```
```sh
$ python test.py
{'_type': 'JObject', 'sno_new': 0, 'fno_new': 2, 'ln_new': 2, 'ofs_moved': 0}
```

To select step 2 of program 5 in manual mode, send the following body to the same path. `fno: -1` keeps the current function number.

```json
{
    "pno": 5,
    "sno": 2,
    "fno": -1,
    "ext_sel": 0
}
```
