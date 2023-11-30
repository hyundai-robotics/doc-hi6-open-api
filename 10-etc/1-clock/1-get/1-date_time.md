## 10.1.1.1 `date_time`

### Description

`date_time`

- `GET` : Obtain the set system time.

### response-body

- [date time](../../../99-schema/date_time.md)

### Example

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

Python Script Example

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