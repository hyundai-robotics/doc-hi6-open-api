#### 2.1.2 `jobs_info`

##### Description

- `GET` : Obtain information about job programs.

##### path-parameter

```python
GET /project/jobs_info
```

##### response-body

- [job file information](../../99-schema/jobs_info.md)

##### Example

<blockquote>

```python
request url:
GET /project/jobs_info

response-body:
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
</blockquote>

Python Script Example

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
(200, [
	{'_type': 'JObject', 'fname': '0055.job', 'n_step': 1, 'n_total_ax': 6, 'job_comment': '', 'n_aux_ax': 0},  
	{'_type': 'JObject', 'fname': '0001.job', 'n_step': 2, 'n_total_ax': -1, 'job_comment': '', 'n_aux_ax': -1}, 
	{'_type': 'JObject', 'fname': '9999.job', 'n_step': 1, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6},
	...
])
```
