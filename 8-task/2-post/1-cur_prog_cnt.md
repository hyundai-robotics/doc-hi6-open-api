#### 8.2.1 `task/cur_prog_cnt`

<div style="width: fit-content;">

##### 설명

- `POST` : 태스크의 현재 프로그램 카운터를 설정합니다.

##### path-parameter

```python
POST /project/context/tasks/0/cur_prog_cnt
```

- `0`은 태스크 인덱스입니다. 위 경로는 태스크 0의 프로그램 카운터를 설정합니다.

##### request-body

- [cur_prog_cnt 요청 파라미터](../.././99-schema/cur_prog_cnt.md)
- 원격모드에서는 외부선택(`ext_sel: 1`)을 사용합니다.
- 수동모드에서는 내부선택(`ext_sel: 0`)을 사용할 수 있습니다. 원격모드에서는 내부선택이 금지됩니다.
- 프로그램이 정지된 상태에서 요청하십시오. 이 API는 프로그램 카운터만 설정하며, 프로그램 실행이나 로봇 이동을 시작하지 않습니다.

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
     - 수동모드에서 외부선택(`ext_sel: 1`)을 요청한 경우 (`err_code: -1114208`)도 400 응답이 반환될 수 있습니다.
   - 403 : Forbidden
     - 허용되지 않는 요청을 한 경우
     - `err_code` (<0) 반환. 하기 에러코드 참조
   - 404 : Not Found

2) response-body
   - [cur_prog_cnt 응답 파라미터](../.././99-schema/cur_prog_cnt.md)

3) error code

	<div style="width: fit-content;">

     - -1114208 : 외부선택(`ext_sel: 1`)을 요청했으나 원격모드가 아닌 경우
   	- -1442080 : 프로그램 재생 중 적용 불가
   	- -1245280 : 유효하지 않은 프로그램 카운터

   		> api 로 프로그램을 start/stop 한 뒤 cur_prog_cnt 를 호출 하는 경우  
   		> '유효하지 않은 프로그램 카운터' 에러가 발생할 수 있습니다.  
   		> set_cur_pc_idx api 로 현재 커서 위치를 상단(idx: 1)으로 옮기고 호출하면 정상 동작합니다.

	</div>

##### 사용 예

원격모드에서 외부선택으로 프로그램을 선택하는 예입니다.

```python
request url:
POST /project/context/tasks/0/cur_prog_cnt

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


def post_cur_prog_cnt() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks/0/cur_prog_cnt"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {"pno": 1, "sno": 0, "fno": 0, "ext_sel": 1}

    response = requests.request(
        "POST", base_url + path_parameter, headers=headers, json=body
    )

    return response


ret = post_cur_prog_cnt()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$ python test.py
(200, {'_type': 'JObject', 'sno_new': 0, 'ofs_moved': 0, 'fno_new': 0, 'ln_new': 0})
```

수동모드에서 프로그램 5의 스텝 2를 선택하려면 같은 경로에 아래 본문을 전송합니다. `fno: -1`은 현재 펑션 번호를 유지합니다.

```json
{
    "pno": 5,
    "sno": 2,
    "fno": -1,
    "ext_sel": 0
}
```
</div>
