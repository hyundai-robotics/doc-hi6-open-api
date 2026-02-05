### 11.1.1.1 `date_time`

<div style="width: fit-content;">

#### 설명

- `GET` : 설정된 시스템 시간을 가져옵니다.

#### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response body
   - [시스템 시간 정보](../../../99-schema/date_time.md)
		<div style="width: fit-content;">

		```json
		{"_type": "JObject", "year": 2025, "min": 43, "sec": 39, "hour": 15, "wday": 2, "mon": 8, "day": 19}
		```
		</div>


#### 사용 예

<blockquote>

```python
request url:
GET /clock/date_time

response-body:
{
    "_type": "JObject",
    "year": 2025,
    "mon": 11,
    "day": 20,
    "min": 40,
    "hour": 19,
    "sec": 54
}
```
</blockquote>

Python Script 예시

```python
# test.py
import requests
import time


def get_system_time() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/clock/date_time"
    res = requests.get(url=base_url + path_parameter)

    return res


for idx in range(5):
    res = get_system_time()
    print((res.status_code, res.json()))
    time.sleep(1)
```
```sh
$python test.py
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 39, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 40, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 41, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 42, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 43, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
```
</div>
