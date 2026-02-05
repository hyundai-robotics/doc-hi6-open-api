### 4.1.4 `ucss/ucs_nos`

#### 설명

- `GET` : 현재 사용 중인 사용자 좌표계들을 리스트로 얻습니다.
- `시스템 > 2: 제어 파라미터 > 6: 좌표계 등록` 을 통해 등록한 사용자 좌표계 리스트를 출력합니다.

#### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ucss/ucs_nos
```

#### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 현재 사용중인 사용자 좌표계(list)  
  	  ex) [1]


#### 사용 예

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
[1]
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_ucs_nos() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ucss/ucs_nos"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_ucs_nos())
```
```sh
$python test.py
(200, [1])
```
</div>
