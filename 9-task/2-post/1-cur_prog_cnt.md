## 9.2.1 `task/cur_prog_cnt`

<div style="width: fit-content;">

### 설명

- `POST` : 태스크의 현재 프로그램 카운터를 설정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

### request-body

- [cur_prog_cnt 요청 파라미터](../.././99-schema/cur_prog_cnt.md)
- api 는 원격모드에서 동작하므로 외부선택 옵션(ext_sel: 1)을 선택해야합니다.

### response-body

- [cur_prog_cnt 응답 파라미터](../.././99-schema/cur_prog_cnt.md)

### status code

- 200 : 정상 동작
- 403 : 허용되지 않은 요청

### error code

<div style="width: fit-content;">

- -1442080 : 프로그램 재생 중 적용 불가
- -1245280 : 유효하지 않은 프로그램 카운터
  > api 로 프로그램을 start/stop 한 뒤,  
  > cur_prog_cnt 를 호출 하는 경우 -1245280 에러가 발생할 수 있습니다.  
  > set_cur_pc_idx api 로 현재 커서 위치를 최상단(idx: 0)으로 옮기고 호출해야합니다.

</div>

### 사용 예

```python
request url:
POST /project/context/tasks[0]/cur_prog_cnt

request-body:
{
    "pno":1,
    "sno":-1,
    "fno":-1,
    "ext_sel":1
}
```

Python Script 예시

```python
import requests

def post_cur_prog_cnt() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/cur_prog_cnt'
    headers        = { 'Content-Type': 'application/json; charset=utf-8' }
    body           = { "pno":1, "sno":-1, "fno":-1, "ext_sel":1 }

    response = requests.request("POST", base_url + path_parameter, headers=headers, json=body)

    return response.json()

print(post_cur_prog_cnt())
```
```sh
$python python test.py
{'_type': 'JObject', 'sno_new': 0, 'fno_new': 2, 'ln_new': 2, 'ofs_moved': 0}
```
</div>