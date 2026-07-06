#### 4.1.1 `motor_on_state`

##### 설명

- `GET` : 모터 온 상태를 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/motor_on_state
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val :
     - `0` : on
     - `1` : off
     - `2` : busy (상태 전환 중)

##### 사용 예
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
    "_type" : "JObject",
    "val" : 1
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_motor_on_state() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/motor_on_state"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_motor_on_state())

```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': 1})
```

</div>
