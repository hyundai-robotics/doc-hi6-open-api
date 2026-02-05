#### 8.3.1 `files`

##### Description

- `DELETE` : Deletes the target file or directory.

##### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

##### status code

- 200 : Request succeeded
  - Target deletion completed

##### Example

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```
```
${cont_model}
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
