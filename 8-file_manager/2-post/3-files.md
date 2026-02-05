### 8.2.3 `files`

#### 설명

- `POST` : 타겟 경로에 파일을 전송합니다.

#### path-parameter


<div style="width: fit-content;">

```python
POST /file_manager/files/{target_filepath}
```

#### path-variable

- `target_filepath` : 확장자를 포함한 타겟 파일 경로

#### request-body

- binary 형식의 파일
- `Content-Type` 은 `application/octet-stream` 이어야합니다.

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	<div style="width: fit-content;">

	```json
	{"_text": ""})
	```
	</div>

#### 사용 예

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- hi6_proj.json
```

```python
request url:
POST /file_manager/files/project/jobs/test.job
```

</div>

Python Script 예시

```python
# test.py
import requests


def post_file_transfer() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    path_value = "/project/jobs/3344.job"  # target

    target_file = base_url + path_parameter + path_value
    source_file = "D:\\temp\\test.job"  # source (path for WindowOS)

    with open(source_file, "rb") as file:
        response = requests.post(
            url=target_file,
            data=file,
            headers={"Content-Type": "application/octet-stream"},
        )

    return response


print(post_file_transfer())
```
```sh
$python test.py
(200, {'_text': ''})
```
