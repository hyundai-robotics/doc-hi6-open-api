## 2.1.1 api_ver

### Description

- GET : Optain the Open API version number

### path-parameter

```python
GET /api_ver
```

### response-body

- Open API version number
- The initial Hi6 Open API is a document written based on `version 5`.

### Example

```python
request url:
GET /api_ver

response-body:
5
```

Python Script Example

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