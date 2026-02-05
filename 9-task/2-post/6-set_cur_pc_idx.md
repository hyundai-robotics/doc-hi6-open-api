#### 9.2.6 `set_cur_pc_idx`

<div style="width: fit-content;">

##### 설명

- `POST` : 현재 커서를 index 라인(>=0)에 위치 시키는 함수

##### path-parameter

```python
POST /project/context/tasks[{task index}]/set_cur_pc_idx
```

##### request-body
-
	<div style="width: fit-content;">

	```json
	{ "idx": 1 }
	```
	</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>



##### error code

- -38501 : 재생 중인 task 가 있을 때는 적용이 되지 않습니다.

##### 사용 예

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
  "idx": 2
}
```


Python Script

```python
# test.py
import requests


def set_cur_pc_idx() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/set_cur_pc_idx"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"idx": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(set_cur_pc_idx())
```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>
