#### 9.2.2 `task/reset`

##### Description

<div style="width: fit-content;">

{% hint style="warning" %}

Calling R-code 0 initializes the program counter, which may cause robot malfunctions.<br>
Please use R-code 1 for error reset purposes.<br>
We are not responsible for any issues caused by the indiscriminate calling of R-code 0, ignoring this warning.

{% endhint %}

##### Description

- `POST`: Initializes the step counter and moves to STEP0.
- Utilizes [R-code 1](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/en-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) or [R-code 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/en-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}).  <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;">
    Codes other than R-code 1 and 0 are not intended operations.
</span>
- If program counter manipulation is required after executing R-code 1, explicitly use the [cur_prog_cnt](./1-cur_prog_cnt.md) and [set_cur_pc_idx](./6-set_cur_pc_idx.md) APIs.

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
		- When the request body fails validation
	- 403 : Forbidden
        - When an unauthorized request is made
        - Returns `err_code` (<0). Refer to the error codes below
	- 404 : Not Found

2) response-body
   - code: The requested rcode number is returned
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
