#### 6.2.1 `set relay values`

##### 설명

- `POST` : relay 값 설정합니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/plc/set_relay_value
```

##### request-parameter

- `name` : 설정하려는 릴레이명을 [표기법](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/ko/3-relay/2-relay-expression?cont_model=${cont_model})에 맞춰 입력합니다.
- `value` : 상기 표기법의 `data-type` 에 유의하여 설정하려는 값을 입력합니다.
```json
{
    "name": "fb3.dof14",
    "value": "2.718"
}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{ "_type":"JObject" }
	```
	</div>
</div>

##### 사용 예

<div style="width: fit-content;">

```json
request url:
POST /project/plc/set_relay_value

request-body:
{
    "name": "fb1.do0",
    "value": "1"
}

response-body:
{ "_type":"JObject" }
```
</div>

<div style="width: fit-content;">

Python Script 예제

```python
# test.py
import requests


def get_relay_value() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/plc/fb1_do/val_s32"

    response = requests.get(url=base_url + path_parameter)

    return response


# @measure_api
def post_set_relay_value() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/plc/set_relay_value"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"name": "fb1.do0", "value": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret1 = get_relay_value()
ret2 = post_set_relay_value()
ret3 = get_relay_value()

print((ret1.status_code, ret1.json()))
print((ret2.status_code, ret2.json()))
print((ret3.status_code, ret3.json()))

```
```sh
$python test.py
(200, [0, 0, 0, 0, 0, 0, 0, 0])
(200, {'_type': 'JObject'})
(200, [1, 0, 0, 0, 0, 0, 0, 0])
```
</div>
