# 8.2.3 `files`

## Description

`files`

- `POST` : Transfer the file to the target path.

## path-parameter

```python
POST /file_manager/files/{target_filepath}
```

## path-variable

- `target_filepath` : Target file path including extension.

## request-body

- `Content-Type` must be `application/octet-stream`.

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| Transfer completed |


## Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- hi6_proj.json
```

```python
request url:
POST /file_manager/files/project/jobs/test.job
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def post_file_transfer() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    path_value      = '/project/jobs/test.job' # target

    target_file     = base_url + path_parameter + path_value
    source_file     = 'D:\\temp\\test.job' # source (path for WindowOS)

    with open(source_file, 'rb') as file:
        response = requests.post(url=target_file, 
                                 data=file, 
                                 headers={'Content-Type': 'application/octet-stream'})

    return response.status_code

print(f"response: {post_file_transfer()}")
```
```sh
$python test.py
response: 200
```