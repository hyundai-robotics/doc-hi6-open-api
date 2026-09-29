#### 4.1.12 `joint_traject_log`

##### 설명

- 지원 버전 : `70.04-00` ↑
- `GET` : 조인트 궤적 로그 저장 기능의 활성화 여부를 조회합니다.
- 로그 활성화 / 비활성화 설정은 [POST joint_traject_log](../2-post/11-joint_traject_log.md) 를 사용합니다.
- 외부 궤적 지령이 동작 가능 상태가 아니어서 제어기가 지령을 거부한 경우, 로그 저장은 제어기에 의해 자동으로 비활성화됩니다. 이 경우 본 API 는 `0` 을 반환합니다.

##### path-parameter

<div style="width: fit-content;">

```text
GET /project/robot/trajectory/joint_traject_log
```
</div>

##### query-parameter

- 없음

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val : 로그 저장 활성화 여부 (integer, `1` : 활성화 / `0` : 비활성화)

<div style="width: fit-content;">

```json
{"val": 1}
```
</div>

##### 사용 예

```text
request url:
GET /project/robot/trajectory/joint_traject_log

response-body:
{
    "val": 1
}
```

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_joint_traject_log(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
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
        print(get_joint_traject_log(base_url, session))
```
```sh
$python test.py
{'val': 1}
```
</div>
