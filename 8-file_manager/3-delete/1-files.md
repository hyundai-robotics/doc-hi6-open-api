## 8.3.1 `files`

### 설명

`files`

- `DELETE` : 타겟 파일 또는 디렉토리를 삭제합니다.

### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| 타겟 삭제 완료 |


### 사용 예

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

Python Script 예시

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