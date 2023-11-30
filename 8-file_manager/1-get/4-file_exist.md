## 8.1.4 `file_exist`

### Description

`file_exist`

- `GET` : Obtain the existence of the target file.

### path-parameter

```python
GET /file_manager/file_exist
```

### query-parameter
> query-parameter must be entered.
```
?pathname=project/jobs/0001.job
```
- `pathname` : target file path

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|`true` (file exists)|
|`200 OK`|`false` (no file exist)|


### Example

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```
```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def is_file_exist() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/file_exist'
    query_parameter = {'pathname': 'project/jobs/0001.job'}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.text

print(is_file_exist())
```
```sh
$python test.py
true
```