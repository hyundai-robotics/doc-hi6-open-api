<link rel="stylesheet" href="../../_assets/style.css">

## 9.2.2 `task/reset`

<div style="width: fit-content;">


{% hint style="warning" %}

R코드 0 호출 시 프로그램 카운터가 초기화되어 로봇 오작동의 원인이 될 수 있습니다.<br>
에러 초기화 용도로는 반드시 R코드 1을 사용하십시오.<br>
주의사항을 무시한 R코드 0 호출로 발생한 문제에 대해 당사는 책임지지 않습니다.

{% endhint %}

### 설명

- `POST`: 스텝 카운터를 초기화하여 STEP0으로 이동합니다.
- [R코드 1](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/korean-tp630/8-r-code/1-use-r-code) 또는 [R코드 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/korean-tp630/8-r-code/1-use-r-code)를 활용합니다.  <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;">
    R코드 1, 0 이외의 코드는 예정된 동작이 아닙니다.
</span>
- R코드 1을 진행한 이후에 프로그램 카운터 조작이 필요한 경우는 명시적으로 [cur_prog_cnt](./1-cur_prog_cnt.md), [set_cur_pc_idx](./6-set_cur_pc_idx.md) api 를 활용하십시오.


### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

### request-body

```json
{"code": 1}
```

### 사용 예

```python
request url:
POST /project/service/r_code/execute

request-body:
{
    "code":1
}
```

Python Script

```python
import requests


def post_rcode_0() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response.status_code


print(f"response: {post_rcode()}")

```
```sh
$python test.py
response: 200
```

</div>