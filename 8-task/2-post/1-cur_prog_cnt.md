#### 8.2.1 `task/cur_prog_cnt`

##### Description

- `POST` : 设置任务的当前程序计数器。

##### path-parameter

```python
POST /project/context/tasks/0/cur_prog_cnt
```

- `0` 是任务索引。此路径用于设置任务 0 的程序计数器。

##### request-body

- [cur_prog_cnt request parameter](../../99-schema/cur_prog_cnt.md)
- 在远程模式下，请使用外部选择（`ext_sel: 1`）。
- 在手动模式下，可以使用内部选择（`ext_sel: 0`）。远程模式下禁止使用内部选择。
- 请在程序停止时发送请求。此 API 仅设置程序计数器，不会启动程序执行或机器人运动。

##### response

1) 状态码
   - 200：OK
   - 400：Bad Request
     - 请求体未通过有效性检查。
     - 在手动模式下请求外部选择（`ext_sel: 1`）时，也可能返回 400，且 `err_code` 为 `-1114208`。
   - 403：Forbidden
     - 请求不被允许。返回负值 `err_code`。
   - 404：Not Found

2) 响应体
   - [cur_prog_cnt 响应参数](../../99-schema/cur_prog_cnt.md)

3) 错误代码
   - -1114208：请求了外部选择（`ext_sel: 1`），但控制器不处于远程模式。
   - -1442080：程序正在运行，无法应用。
   - -1245280：无效的程序计数器。

   通过 API 启动或停止程序后，可能出现无效程序计数器错误。请先使用 `set_cur_pc_idx` 将光标移至顶部（`idx: 1`），再重试。

##### Example

此示例在手动模式下使用内部选择。在远程模式下使用外部选择时，请将 `ext_sel` 设置为 `1`。

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

在手动模式下选择程序 5 的步骤 2 时，请向同一路径发送以下请求体。`fno: -1` 表示保持当前功能编号。

```json
{
    "pno": 5,
    "sno": 2,
    "fno": -1,
    "ext_sel": 0
}
```