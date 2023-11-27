##  9.3.2.1 `date_time`

### 설명

`date_time`

- `PUT` : 시스템 시간을 변경합니다.

### request-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

### 사용 예

<blockquote>

```python
request url:
PUT /clock/date_time

response-body:
{
  "year": 2023,
  "mon": 10,
  "day": 30,
  "hour": 18,
  "min": 30,
  "sec": 0
}
```
</blockquote>

Python Script 예시

```python
# test.py
import requests

def put_system_time() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body 			= {"year": 2023, "mon": 11, "day": 20, "hour": 21, "min": 2, "sec": 0}
	
    response = requests.put(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {put_system_time()}")
```
```sh
$python test.py
response: 200
```