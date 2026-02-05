#### 11.1.2.1 `date_time`

<div style = "width: max-content">  

##### 설명

- `PUT` : 시스템 시간을 변경합니다.
- 요청 후 TP > 서비스 > 9: TP 응용 프로그램 종료를 통해 TP 를 재부팅하면 ui에 적용됩니다.

##### request-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response body
	<div style="width: fit-content;">

	```json
	{}
	```
	</div>

##### 사용 예

```python
request url:
PUT /clock/date_time

request-body:
{
    "year": 2025,
    "mon": 10,
    "day": 30,
    "hour": 18,
    "min": 30,
    "sec": 0
}
```

Python Script 예시

```python
# test.py
import requests


def put_system_time() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.18888"  # hrspace
    path_parameter = "/clock/date_time"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"year": 2025, "mon": 8, "day": 19, "hour": 16, "min": 50, "sec": 0}

    response = requests.put(url=base_url + path_parameter, headers=head, json=body)

    return response


print(put_system_time())
```

```sh
$python test.py
(200, {})
```
</div>
