
#### 4.1.9 `joint_traject_agility_info`

##### 설명

* 지원 버전 : `70.04-00` ↑
* `GET` : 현재 제어기에 설정된 민첩(agility) 모드 활성화 여부 및 구동 주파수 정보를 조회합니다.


##### path-parameter

```python
GET /project/robot/trajectory/joint_traject_agility_info

```

##### query-parameter

* 없음

##### response

1. status code
    * 200 : OK
    * 400 : Bad Request
    * 403 : Forbidden
    * 404 : Not Found

2. response-body
    * agility_mode : 민첩 모드 활성화 여부 (boolean)
    * agility_freq : 민첩 모드 동작 주파수 (integer, Hz)

```json
{
    "agility_mode": false,
    "agility_freq": 30
}
```

##### 사용 예

```python
request url:
GET /project/robot/trajectory/joint_traject_agility_info

response-body:
{
    "agility_mode": false,
    "agility_freq": 30
}

```

Python Script 예시

```python
# test.py
import requests

def get_joint_traject_agility_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/trajectory/joint_traject_agility_info"

    res = requests.get(url=base_url + path)

    print(res.json())

    return res


get_joint_traject_agility_info()

```

```sh
$ python test.py
{'agility_mode': False, 'agility_freq': 30}

```
