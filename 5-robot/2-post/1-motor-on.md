## 5.2.1 `motor_on`

- <b style="color:orange"> `motor_off` API 는 [v60.30-00](../../1-release-note/60-30.md)부터 지원되지 않습니다.</b>

<div style="width: fit-content;">
### 설명

- `POST` : 모터 ON을 수행합니다.

### path-parameter


```python
POST /project/robot/motor_on
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### 사용 예

```python
POST /project/robot/motor_on

request-body:
{}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code


print(f"Motor-ON  response: {post_motor_on()}")
```
```sh
$python test.py
Motor-ON  response: 200
```

</div>