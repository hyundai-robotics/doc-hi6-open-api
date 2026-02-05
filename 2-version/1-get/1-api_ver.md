#### 2.1.1 api_ver 

##### 설명

불가피하게 API 의 스키마 버전에 따라 제어기와 통신하는 방법이나 데이터 구조가 변경될 수 있습니다.  
이는 클라이언트 프로그램에 문제를 야기할 수 있으므로 해당 함수를 통해 확인하는 과정이 필요합니다.  
각 API 함수들에 대해 스키마 버전 변경이 생길 경우 설명 페이지에 별도의 표기를 통해 안내됩니다.


- `GET` : Open API 스키마 버전을 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /api_ver
```
##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - Open API 스키마 버전


##### 사용 예

```python
request url:
GET /api_ver

response:
(200, 5)
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests

def get_api_ver() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/api_ver"
    response = requests.get(url=base_url + path_parameter, timeout=5)
    return response

print(get_api_ver())
```
```sh
$python test.py
(200, 5)
```
</div>
