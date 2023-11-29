## 8.2.7 `solve_expr`

### 설명

`solve_expr`

- `POST` : 표현식(expression)을 풀어서 나오는 결과 값을 태스크의 지역 또는 전역 변수에 설정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

### request-body
- `expr` : 풀려고 하는 수식(expression)을 입력합니다
- `scope` : `expr` 에 대한 스코프를 설정합니다.

	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|

```json
{
	"expr" : "a",
	"scope" : "local"
}
```

### response-body

```json
13 // 현재 지정된 scope 안의 expr 값을 읽어옵니다.
```

### 사용 예

<blockquote>

```python
# 1. 현재 Task 에서 선언된 "지역" 변수 a 값 읽어오기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
	"expr"  : "a",
	"scope" : "local"
}

response-body:
13
```

</blockquote>

<blockquote>

```python
# 2. 현재 Task 에서 선언된 "전역" 변수 a 값 읽어오기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr"  : "a",
    "scope" : "global"
}

response-body:
10
```

</blockquote>

<blockquote>

```python
# 3. 지역 변수 a 의 값에 대해서 -234 를 더하기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr": "a + (-234)"
}

response-body:
1000
```

</blockquote>

Python Script 예시
- 로봇 제어기의 태스크 영역에 지역 및 전역 변수 a 값이 설정된 상태로 하기 코드 실행

```python
# test.py
import requests

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

print(f"{post_read_var('a', 'local')}")
print(f"{post_read_var('a', 'global')}")
print(f"{post_read_var('a + (-234)')}")
```
```sh
$python test.py 
1234
10
1000
```