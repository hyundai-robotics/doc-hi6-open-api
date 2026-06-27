#### 2.1.2 `sysver`

##### 描述

- `GET` : 获取机器人控制器系统的软件版本。

##### 路径参数

```python
GET /versions/sysver
```

##### 响应主体

modules : 模块版本信息数组
  - 模块版本信息 :
    - `名称 (name)` : 模块名称
		|module name|description|
		|---:|:---|
		|com|机器人控制器|
		|tp|教学挂件|
    - `ver` : 版本号
    - `build-date` : 构建日期
    - `build-time` : 构建时间
    - `commit-id` : 源代码的提交 ID

##### 示例

```python
request url:
GET /versions/sysver

response-body:
{
    "modules" : [
        {
            "build-date": ...
            "build-time": ...
                 ...
            "ver": ...
        }
    ] 
}
```

Python 脚本示例

```python
import requests

def get_sysver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/versions/sysver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_sysver())
```
```sh
$python test.py
{'modules': [{'build-date': 'Jan 00 2000', 'build-time': '00:00:00' ...
```