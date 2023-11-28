## 9.2.1.1 `date_time`

### 설명

`date_time`

- `GET` : 설정된 시스템 시간을 가져옵니다.

### response-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

### 사용 예

<blockquote>

```python
request url:
GET /clock/date_time

response-body:
{
	"_type": "JObject",
	"year": 2023,
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

def get_system_time() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'
	
    response = requests.get(url = base_url + path_parameter).json()

    t = f'[{response["mon"]}/{response["day"]}] {response["hour"]}:{response["min"]}'

    return t

print(get_system_time())
```
```sh
$python test.py
[11/20] 19:55
```