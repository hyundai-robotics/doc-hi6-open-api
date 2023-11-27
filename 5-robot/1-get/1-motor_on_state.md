# 4.1.1 `motor_on_state`

## 설명

`motor_on_state`

- `GET` : 모터 온 상태를 얻습니다.

## path-parameter

```python
GET /project/robot/motor_on_state
```

## response-body

- val :
  - `0` : on
  - `1` : busy (상태 전환 중)
  - `2` : off

## 사용 예
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
	"_type" : "JObject",
	"val" : 1
}
```

Python Script 예시

```python
# test.py
import requests

def get_motor_on_state() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on_state'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(f"Motor On status: {get_motor_on_state()['val']}")
```
```sh
$python test.py
Motor On status: 1
```