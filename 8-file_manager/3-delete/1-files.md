## 8.3.1 `files`

### Description

`files`

- `DELETE` : Deletes the target file or directory.

### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

### response-body
|HTTP Status|description|
|:---|:---|
|`200 OK`| Target deletion completed, 200 returned even if there is no target |


### Example

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```
```
hi6
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def delete_file() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    target_file     = '/project/jobs/test.job'

    response = requests.delete(url = base_url + path_parameter + target_file)

    return response.status_code

print(f"response: {delete_file()}")
```
```sh
$python test.py
response: 200
```