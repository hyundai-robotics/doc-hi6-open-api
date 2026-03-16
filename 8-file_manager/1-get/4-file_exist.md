#### 8.1.4 `file_exist`

##### Description

- `GET` : Obtain the existence of the target file.

##### path-parameter

```python
GET /file_manager/file_exist
```

##### query-parameter

query-parameter must be entered.  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : target file path

##### response-body

- `true` (file exists)
- `false` (no file exist)

##### status code

- 200 : Request succeeded
  - return [file information](../../99-schema/file_info) `list`
- 404 : Request failed
  - not allowed path-parameter


##### Example

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```
```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
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
