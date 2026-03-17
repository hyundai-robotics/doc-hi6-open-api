#### 8.1.1 `文件 (files)`

##### 描述

- `GET` : 文件内容由控制器返回。

##### 路径参数

```python
GET /file_manager/files
```

##### 查询参数

查询参数必须输入。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 要获取的文件名

##### 状态码

- 200 : 请求成功
  - 返回文件内容
- 403 : 请求失败
  - 当文件不存在时返回错误状态码

##### 示例

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
请求 URL:
GET /file_manager/files?pathname=project/jobs/0001.job

响应主体:
{
    Hyundai Robot Job File; { version: 2.0 ... }
    ...
}
```
</blockquote>

Python 脚本示例

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
现代机器人作业文件; { version: 2.0, mech_type: "576(HH020-03)", total_axis: 6, aux_axis: 0 }
     位姿 P1 =po1 = 位姿(10, 90, 0, 0, -30, 0, -1240.8)
     位姿 P2
     位姿 P3
     位姿 P4
S1   move P,tg=po1,spd=100%,accu=0,tool=1
S2   move P,tg=po1,spd=100%,accu=0,tool=1
S3   move P,tg=po1,spd=100%,accu=0,tool=1
S4   move P,tg=po1,spd=100%,accu=0,tool=1
     end
```
