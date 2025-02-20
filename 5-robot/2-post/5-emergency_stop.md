## 5.2.5 `emergency_stop`

### 설명

- 지원 버전 : `60.30-00` &uparrow;
- `POST` : 비상 정지를 실행합니다.  
- 비상정지 버튼을 눌렀을 때와 동일한 감속 프로파일이 적용됩니다.
- API 호출 시, 네트워크 지연(Latency) 또는 요청 처리 시간 때문에 물리적 버튼보다 늦게 반응할 가능성이 있습니다.


### path-parameter

```python
POST /project/robot/emergency_stop
```

### request-body
```python 
{}
```

### response-body

- 200 : 요청 성공  
- 400 : 요청 실패 (비상정지 시퀀스 호출에 실패)  

### 사용 예

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

Python Script 예시

```python
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {post_emergency_stop()}")
```
```sh
$python test.py
response: 200
```