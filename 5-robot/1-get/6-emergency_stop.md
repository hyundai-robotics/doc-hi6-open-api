## 5.1.6 `emergency_stop`

### 설명

- `GET` : 비상정지 버튼이 눌려져있는 상태에 대해서 정보를 얻습니다.
-  API 로 비상정지를 요청하는 경우에 대해서는 API 가 들어오는 시점에 1이 반환됩니다.  

### path-parameter

```python
GET /project/robot/emergency_stop
```

### response-body

- 0: released 상태
- 1: pressed 상태

### 사용 예

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "val": 0,
}
```

Python Script 예시

```python
# test.py
import requests

def get_emergency_stop() -> Optional[dict]:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = requests.get(url=base_url + path_parameter, headers=head)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error in get_emg_state: {e}")
        return None

print(f"{get_emergency_stop()}")
```
```sh
$python test.py
{'_type': 'JObject', 'val': 0}
```