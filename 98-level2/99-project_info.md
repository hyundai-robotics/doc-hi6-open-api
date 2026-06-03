## 3.1.2 `project_info`

### Description

- `GET`: Retrieves information regarding the project.

### path-parameter

```python
GET /project/project_info

```

### response-body

* [Project Information Schema](../99-schema/project_info.md)


### Example

<blockquote>

```python
Request URL:
GET /project/project_info

Response Body:
{
  "_type": "JObject",
  "project_file_exist": true,
  "n_files_in_jobs": 9,
  "n_files_in_vars": 2,
  "n_files_in_lads": 0
}
```

</blockquote>

Python Script Example

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
$ python test.py
{'_type': 'JObject', 'project_file_exist': True, 'n_files_in_jobs': 9, 'n_files_in_vars': 2, 'n_files_in_lads': 0}

```
