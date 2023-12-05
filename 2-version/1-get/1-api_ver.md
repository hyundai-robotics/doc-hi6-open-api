## 2.1.1 api_ver

### 설명

`api_ver`

- `GET` : Open API version 번호를 얻습니다.

### path-parameter

```python
GET /api_ver
```

### response-body

- Open API version 번호
- 초기 Hi6 Open API 는 `version 5`를 기준으로 작성된 문서입니다. 

### 사용 예

```python
request url:
GET /api_ver

response-body:
5
```

Python Script 예시

```python
import requests

def get_api_ver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/api_ver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_api_ver())
```
```sh
$python test.py
5
```