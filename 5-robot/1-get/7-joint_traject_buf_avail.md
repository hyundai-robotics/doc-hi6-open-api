## 5.1.7 `joint_traject_buf_avail`

### 설명
- 지원 버전 : `61.00-00` &uparrow;
- `GET` : 현재 궤적을 저장하는 버퍼의 사용가능한 크기를 반환합니다.
- 궤적을 연속해서 요청을 하는 경우, 해당 함수를 활용해 남은 저장 공간의 크기 이내의 크기의 궤적을 요청해야합니다.

### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

### response-body

- val: 현재 사용 가능한 버퍼의 수 (최대 2048개)


### status code

- 200 : OK
- 400 : Bad Request
	- request body 가 유효성 검사에서 실패한 경우
- 403 : Forbidden
- 404 : Not Found

### 사용 예

```python
request url:
GET /project/robot/trajectory/joint_traject_buf_avail

response-body:
{
    "val": 2048,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_jt_buff_avail_num(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_buf_avail"
    try:
        ret = session.get(url=uri)
        ret.raise_for_status()
        return ret.json()
    except Exception as e:
        print(f"[ERROR] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        ret = get_jt_buff_avail_num(base_url, session)
        print(ret)
```
```sh
$python test.py
{'val': 2048}
```
</div>