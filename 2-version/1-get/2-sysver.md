## 2.1.2 sysver

### Description

`sysver`

- `GET` : Obtain the software version of the robot controller system.

### path-parameter

```python
GET /versions/sysver
```

### response-body

modules : Array of module version information
  - module version information :
    - `name` : module name
		|module name|description|
		|---:|:---|
		|com|robot controller|
		|tp|teaching pendant|
    - `ver` : version number
    - `build-date` : build date
    - `build-time` : build time
    - `commit-id` : Commit ID of source code

### Example

```python
request url:
GET /versions/sysver

response-body:
{
    "modules" : [
        {
            "build-date": ...
            "build-time": ...
                 ...
            "ver": ...
        }
    ] 
}
```

Python Script Example

```python
import requests

def get_sysver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/versions/sysver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_sysver())
```
```sh
$python test.py
{'modules': [{'build-date': 'Jan 00 2000', 'build-time': '00:00:00' ...
```