### 8.3.1 `files`

<div style="width: fit-content;">

#### 설명

- `DELETE` : 타겟 파일 또는 디렉토리를 삭제합니다.

#### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 없음. status code 만 반환
   - 삭제할 대상의 파일이 없어도 통신상에 문제가 없으면 상태코드 200 응답

#### 사용 예

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```

```text
${cont_model}
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python Script 예시

```python
# test.py
import requests


def delete_file() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    target_file = "/project/jobs/0001.job"

    response = requests.delete(url=base_url + path_parameter + target_file)

    return response


ret = delete_file()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)
```
```sh
$python test.py
<Response [200]>
```
</div>
