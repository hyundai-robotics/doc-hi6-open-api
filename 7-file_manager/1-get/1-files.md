#### 7.1.1 `文件 (files)`

##### Description

- `GET` : 从控制器返回文件内容。

##### path-parameter

```python
GET /file_manager/files
```

##### query-parameter

query-parameter 必须输入。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 要获取的文件名

##### status code

- 200 : 请求成功
  - 返回文件内容
- 403 : 请求失败
  - 当文件不存在时返回错误状态码

##### Example

<blockquote>

```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job   <- 目标
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- ${cont_model:lower}_proj.json
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