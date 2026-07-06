#### 7.2.2 `mkdir`

##### Description

- `POST` : Create a directory in the target path.

##### path-parameter

```python
GET /file_manager/mkdir
```

##### request-body

|key|value|description|
|:---|:---|:---|
|`path`|`str`|Where to create the directory|

##### response-body

- { `path`: ${target path} }

##### status code

- 200 : Request succeeded
  - Directory creation completed in target location
- 400 : Request failed
  - When directory names are duplicated in the target location

##### Example

<blockquote>

```python
request url:
GET /file_manager/mkdir

request-body: 
{
	"path" : "project/jobs/special"
}
```

```
${cont_model}
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- ${cont_model:lower}_proj.json
```


</blockquote>

Python Script Example

```python
# test.py
import requests

def post_mkdir() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/mkdir'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = {'path': "project/jobs/special7"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {post_mkdir()}")
```
```sh
$python test.py
response: 200
```
