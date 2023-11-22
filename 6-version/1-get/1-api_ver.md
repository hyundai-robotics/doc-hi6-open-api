# 6.1.1 api_ver

## 설명

- GET : Open API version 번호를 얻습니다.

## path-parameter

```python
GET /api_ver
```

## response-body

- Open API version 번호

## 사용 예

```python
request url:
GET /api_ver

response-body:
5
```

<details><summary>Python Script 예시</summary>

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

</details>