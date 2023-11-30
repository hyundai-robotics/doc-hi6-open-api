## 8.1.1 `files`

### Description

`files`

- `GET` : The file contents are responded to from the controller.

### path-parameter

```python
GET /file_manager/files
```

### query-parameter

```
?pathname=project/jobs/0001.job
```
- `pathname` : File name to get

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|Return file contents|
|`404 Not Found`| Return error status code when file does not exist|


### Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job   <- target
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- hi6_proj.json
```

```python
request url:
GET /file_manager/files?pathname=project/jobs/0001.job

response-body:
{
	Hyundai Robot Job File; { version: 2.0 ... }
	...
}
```

</blockquote>

Python Script Example

```python
# test.py
import requests

def print_file_contents() -> None:
    base_url	    = "http://192.168.1.150:8888"
    path_parameter  = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)
	
    print(f'response: {response.status_code}')
    print(response.text)

print_file_contents()
```
```sh
$python test.py
response: 200
Hyundai Robot Job File; { version: 2.0, mech_type: "576(HH020-03)", total_axis: 6, aux_axis: 0 }
     Pose P1 =po1 = Pose(10, 90, 0, 0, -30, 0, -1240.8)
     Pose P2
     Pose P3
     Pose P4
S1   move P,tg=po1,spd=100%,accu=0,tool=1
S2   move P,tg=po1,spd=100%,accu=0,tool=1
S3   move P,tg=po1,spd=100%,accu=0,tool=1
S4   move P,tg=po1,spd=100%,accu=0,tool=1
     end
```