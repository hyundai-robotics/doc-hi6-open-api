## 10.1.1 `cur_local_vars`

### 설명

`cur_local_vars`

- `GET` : 현재 작업 구문(Task context)의 변수를 반환합니다.

### path-parameter

```python
GET /project/context/tasks[0]/cur_local_vars
```

### response-body

```json
{
	"_type": "JObject",
	"변수1" : 값1,
	"변수2" : 값2,
	   ...
}
```

### 사용 예

<blockquote>


```text
Hyundai Robot Job File;
    a = 1234
    b = 5678
    end
```
TP 에서 상기 0001.job 을 실행한 경우

```python
request url:
GET /project/context/tasks[0]/cur_local_vars

response-body:
{
  "_type": "JObject"
}
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_cur_local_var() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/cur_local_vars"

    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_cur_local_var())
```
```sh
$python test.py 
{'_type': 'JObject'} # 현재 작업 구문에 지역 변수가 없음
```