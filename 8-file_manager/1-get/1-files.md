## 8.1.1 `files`

### 설명

- `GET` : 제어기로부터 파일 내용을 응답 받습니다.

### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/files
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 가져올 파일 이름

### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- "_text" 를 키값으로 요청한 job 파일의 내용을 반환
	- e.g.
		<div style="width: fit-content;">

		```json
		{ "_text": "Hyundai Robot Job File; { version: 2.0, mech_type: "458(HA006B-01)", total_axis: 6, aux_axis: 0 }\nS1   move P,spd=60%,accu=0,tool=1  [0.000,90.000,0.000,0.000,0.000,0.000]\n     wait di1\n     end\n" }
		```
		</div>
</div>

### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
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
</div>

Python Script 예시


<div style="width: fit-content;">


```python
# test.py
import requests


def get_file_contents() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_contents())
```
```sh
$python test.py
(200, {'_text': 'Hyundai Robot Job File; { version: 2.0, mech_type: "458(HA006B-01)", total_axis: 6, aux_axis: 0 }\nS1   move P,spd=60%,accu=0,tool=1  [0.000,90.000,0.000,0.000,0.000,0.000]\n     wait di1\n     end\n'})
```  

</div>