#### 9.2.6 `set_cur_pc_idx`

##### 描述

- `POST` : 定位当前光标在索引行的功能

##### 路径参数

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

##### 请求主体
```json
{
    "idx": 1
}
```

##### 示例

<blockquote>

```python
请求 URL:
POST /project/context/tasks[0]/set_cur_pc_idx

请求主体
{
    "idx": 2
}
```

</blockquote>

Python 脚本示例

```python
# test.py
import requests

def set_cur_pc_idx() -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/set_cur_pc_idx"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"idx": 1}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {set_cur_pc_idx()}")
```
```sh
$python test.py 
响应 200 # 光标位置在 TP 上改变
```