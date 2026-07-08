#### 4.1.9 `joint_traject_agility_info`

##### Description

* Supported version : `70.04-00` ↑
* `GET` : 查询当前控制器中设置的敏捷（agility）模式激活状态及工作频率信息。


##### path-parameter

```python
GET /project/robot/trajectory/joint_traject_agility_info
```

##### query-parameter

* 无

##### response

1. status code
* 200 : OK
* 400 : Bad Request
* 403 : Forbidden
* 404 : Not Found

2. response-body
* `agility_mode` : 敏捷模式激活状态 (boolean)
* `agility_freq` : 敏捷模式工作频率 (integer, Hz)

    <div style="width: fit-content;">

    ```json
    {
        "agility_mode": false,
        "agility_freq": 30
    }
    ```
    </div>

<div style="width: fit-content;">

##### Example

```python
request url:
GET /project/robot/trajectory/joint_traject_agility_info

response-body:
{
    "agility_mode": false,
    "agility_freq": 30
}

```

Python 脚本示例

```python
# test.py
import requests

def get_joint_traject_agility_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/trajectory/joint_traject_agility_info"

    res = requests.get(url=base_url + path)

    print(res.json())

    return res


get_joint_traject_agility_info()

```

```sh
$ python test.py
{'agility_mode': False, 'agility_freq': 30}
```

</div>
