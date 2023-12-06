## 4.1.4 `ucss/ucs_nos`

### Description

`ucss/ucs_nos` (user coordinate system numbers)

- `GET` : Obtains a list of user coordinate systems currently in use.
- Prints a list of user coordinate systems registered through `system > 2: Control parameter > 6: Coordinate registration`.

### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

### Example

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python Script Example

```python
# test.py
import requests

def get_ucs_nos():
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ucss/ucs_nos'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(f"{get_ucs_nos()}")
```
```sh
$python test.py
[1, 2, 3]
```