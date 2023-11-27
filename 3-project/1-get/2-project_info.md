## 2.1.2 `project_info`

### 설명

`project_info`

- `GET` : 프로젝트 관련 정보를 받는 함수입니다.

### path-parameter

```python
GET /project/project_info
```

### response-body

- [프로젝트 관련 정보](../../99-schema/project_info.md)
### 사용 예

<blockquote>

```python
request url:
GET /project/project_info

response-body:
{
  "_type": "JObject",
  "project_file_exist": true,
  "n_files_in_jobs": 9,
  "n_files_in_vars": 2,
  "n_files_in_lads": 0
}
```
</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_project_info() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/project_info"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_project_info())
```
```sh
$python test.py
{'_type': 'JObject', 'project_file_exist': True, 'n_files_in_jobs': 9, 'n_files_in_vars': 2, 'n_files_in_lads': 0}
```
