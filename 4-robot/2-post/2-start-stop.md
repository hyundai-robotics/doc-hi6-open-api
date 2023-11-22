# 4.2.2 start / stop

## 설명

- POST : 로봇 기동(start)과 로봇 정지(stop)를 수행합니다.

## path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

## request-body

```json
{}
```

## 사용 예

```python
POST /project/robot/motor_off
```

<details><summary>Python Script 예시</summary>

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # 자동모드 및 모터 온 설정 필요
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

def post_stop() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/stop'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Start response: {post_start()}")
print(f"Stop  response: {post_stop()}")
```
```sh
$python test.py
Start response: 200
Stop  response: 200
```

</details>