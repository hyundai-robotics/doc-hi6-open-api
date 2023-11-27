# 4.2.1 motor_on / motor_off

## 설명

- POST : 모터 ON과 모터 OFF를 수행합니다.

## path-parameter

```python
POST /project/robot/motor_on
POST /project/robot/motor_off
```

## request-body

```json
{}
```

## 사용 예

```python
POST /project/robot/motor_off
```

Python Script 예시

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

def post_motor_off() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_off'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
print(f"Motor-OFF response: {post_motor_off()}")
```
```sh
$python test.py
Motor-ON  response: 200
Motor-OFF response: 200
```