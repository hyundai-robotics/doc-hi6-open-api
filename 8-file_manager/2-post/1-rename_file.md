# 8.2.1 `rename_file`

## Description

`rename_file`

- `POST` : Change the file name of the target file.

## path-parameter

```python
POST /file_manager/rename_file
```

## request-body

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : File path before change
- `pathname_to` : File path after change

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| Works even if there is no target file |
|`http.client.BadStatusLine: HTTP/1.1 1 Unknown`| Rename of target file completed. |


## Example

<blockquote>

```python
request url:
POST /file_manager/rename_file

request-body: 
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
```
hi6
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def rename_file() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    query_parameter = { "pathname_from" : "project/jobs/0001.job", 
                       "pathname_to"   : "project/jobs/4321.job" }

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.status_code

print(rename_file())
```
```sh
$python test.py
# If the file name is changed normally, an error log(HTTP/1.1 1 Unknown) is output.
# If you try to rename a file that does not exist, 200 OK is output.
```