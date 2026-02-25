#### 3.1.2 `jobs_info`

##### 설명

- `GET` : job 프로그램 관련 정보들을 받는 함수입니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/jobs_info
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

   - [job 파일 관련 정보](../../99-schema/jobs_info.md)

##### 사용 예


<div style="width: fit-content;">

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
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_jobs_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/jobs_info"
    res = requests.get(url=base_url + path_parameter)

    return res


print(get_jobs_info())
```
```sh
$python test.py
(200, [
	{'_type': 'JObject', 'fname': '0055.job', 'n_step': 1, 'n_total_ax': 6, 'job_comment': '', 'n_aux_ax': 0},  
	{'_type': 'JObject', 'fname': '0001.job', 'n_step': 2, 'n_total_ax': -1, 'job_comment': '', 'n_aux_ax': -1}, 
	{'_type': 'JObject', 'fname': '9999.job', 'n_step': 1, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	{'_type': 'JObject', 'fname': '1111.job', 'n_step': 13, 'n_total_ax': -1, 'job_comment': '', 'n_aux_ax': -1}, 
	{'_type': 'JObject', 'fname': '0005.job', 'n_step': 0, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	{'_type': 'JObject', 'fname': '0021.job', 'n_step': 3, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	...
])
```
</div>
