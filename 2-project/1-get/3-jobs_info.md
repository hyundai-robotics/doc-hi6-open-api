# 2.1.3 `jobs_info`

## 설명

`jobs_info`

- `GET` : 프로젝트 관련 정보를 받는 함수입니다.

## path-parameter

```python
GET /project/jobs_info
```

## response-body

- [job 파일 관련 정보](/99-schema/jobs_info.md)
## 사용 예

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

<details><summary>Python Script 예시</summary>

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
</details>
