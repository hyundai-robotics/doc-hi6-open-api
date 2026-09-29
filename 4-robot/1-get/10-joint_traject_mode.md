#### 4.1.10 `joint_traject_mode`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `GET` : 외부 궤적(온라인 트래킹) 모드의 현재 동작 여부를 조회합니다.
- 다음 중 하나라도 해당되면 `mode` 는 `true` 를 반환합니다.
  - 외부 궤적 모드가 동작 중인 경우
  - 민첩(agility) 모드의 bypass 가 켜져 있는 경우
  - 외부 궤적 모드의 **종료 처리(clean-up)가 진행 중**인 경우
- [joint_traject_off](../2-post/10-joint_traject_off.md) 요청 후 `mode` 가 `false` 가 된 것을 확인한 뒤 다음 궤적 시퀀스를 시작해야 합니다.
- [joint_traject_init](../2-post/7-joint_traject_init.md) 은 `mode` 가 `true` 인 동안에는 버퍼 초기화를 수행하지 않고 그대로 반환하므로, 초기화 전에 본 API 로 상태를 확인하시기 바랍니다.

##### path-parameter

<div style="width: fit-content;">

```text
GET /project/robot/trajectory/joint_traject_mode
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
   - mode : 외부 궤적 모드 동작 또는 종료 처리 여부 (boolean)

<div style="width: fit-content;">

```json
{"mode": true}
```
</div>

{% hint style="warning" %}

민첩 모드 사용 시, 모션 종료 후 `0.5 초` 의 제어기 내부 clean-up 과정이 필요합니다.
이 구간에서도 `mode` 는 `true` 로 유지되며, `false` 를 확인하지 않고 곧바로 궤적을 이어서 보내는 경우 의도치 않은 에러가 발생할 수 있습니다.

{% endhint %}

##### 사용 예

```text
request url:
GET /project/robot/trajectory/joint_traject_mode

response-body:
{
    "mode": true
}
```

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import time
import requests


def wait_traject_mode_off(base_url: str, session: requests.Session, timeout: float = 10.0) -> bool:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_mode"
    deadline = time.time() + timeout

    while time.time() < deadline:
        try:
            ret = session.get(url=uri)
            ret.raise_for_status()
            if ret.json().get("mode") is False:
                return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False
        time.sleep(0.1)

    return False


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        print(wait_traject_mode_off(base_url, session))
```
```sh
$python test.py
True
```
</div>
