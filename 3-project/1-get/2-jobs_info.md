#### 3.1.2 `jobs_info`

##### 描述

- `GET` : 获取作业程序的信息。

##### 路径参数

```python
GET /project/jobs_info
```

##### 响应主体

- [作业文件信息](../../99-schema/jobs_info.md)

##### 示例

<blockquote>

```python
请求 URL:
GET /project/jobs_info

响应主体:
{
    {
        "_type": "JObject",
        "fname": "0001.job",
        "job_comment": "",
        "n_step": 0,
        "n_aux_ax": 0,
        "n_total_ax": 6
    },
    {
        "_type": "JObject",
        "fname": "0002.job",
        "job_comment": "",
        "n_step": 9,
        "n_aux_ax": -1,
        "n_total_ax": -1
    },
    {
        "_type": "JObject",
        "fname": "0003.job",
        "job_comment": "",
        "n_step": 0,
        "n_aux_ax": -1,
        "n_total_ax": -1
    },
            ...
}
```
Python脚本示例

```python
# test.py
import requests

def get_jobs_info() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/jobs_info"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_jobs_info())
```
```sh
$python test.py
[{'_type': 'JObject', 'job_comment': '', 'fname': '0001.job', 'n_step': 0, 'n_aux_ax': 0, 'n_total_ax': 6}, 
{'_type': 'JObject', 'job_comment': '', 'fname': '0002.job', 'n_step': 9, 'n_aux_ax': -1, 'n_total_ax': -1}, 
{'_type': 'JObject', 'job_comment': '', 'fname': '0003.job', 'n_step': 0, 'n_aux_ax': -1, 'n_total_ax': -1}]
```