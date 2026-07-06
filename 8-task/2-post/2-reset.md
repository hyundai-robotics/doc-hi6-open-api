#### 8.2.2 `task/reset`

##### Description

<div style="width: fit-content;">

{% hint style="warning" %}

调用 R-code 0 会初始化程序计数器，这可能导致机器人故障。<br>
请使用 R-code 1 进行错误重置。<br>
我们对因不加选择地调用 R-code 0 而导致的任何问题不承担责任，忽视此警告。

{% endhint %}

##### Description

- `POST`: 初始化步进计数器并移动到 STEP0。
- 利用 [R-code 1](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) 或 [R-code 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}).  <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;">
    R-code 1 和 0 以外的代码不是预期的操作。
</span>
- 如果在执行 R-code 1 后需要操作程序计数器，请明确使用 [cur_prog_cnt](./1-cur_prog_cnt.md) 和 [set_cur_pc_idx](./6-set_cur_pc_idx.md) APIs。

##### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

##### request-body

```json
{"code": 0}
```

##### response

1) status code
	- 200 : OK
	- 400 : Bad Request
		- 当请求体验证失败时
	- 403 : Forbidden
        - 当进行未经授权的请求时
        - 返回 `err_code` (<0)。请参阅下面的错误代码
	- 404 : Not Found

2) response-body
   - code: 返回请求的 rcode 编号
        <div style="width: fit-content;">

		```json
		{"code": 1, ... })
		```

		</div>


##### Example

```python
request url:
POST /project/service/r_code/execute

request-body:
{
    "code":0
}
```

Python Script

```python
import requests


def post_rcode_0() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 0}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response.status_code


print(f"response: {post_rcode_0()}")
```
```sh
$python test.py
response: 200
```