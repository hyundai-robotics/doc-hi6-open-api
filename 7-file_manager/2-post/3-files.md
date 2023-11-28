# 7.2.3 `files`

## 설명

`files`

- `POST` : 타겟 경로에 파일을 전송합니다.
- binary형식으로 file전송만 가능합니다.

## path-parameter

```python
POST /file_manager/files/{target_filepath}
```

## path-variable

- `target_filepath` : 확장자를 포함한 타겟 파일 경로

## request-body

- binary 형식의 파일


## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| 전송 완료 |


## 사용 예

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

Python Script 예시

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