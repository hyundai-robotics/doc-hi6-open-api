#### 4.1.11 `joint_traject_ready`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `GET` : 제어기가 외부 궤적 지령을 받을 수 있는 준비 상태인지 조회합니다.
- 아래 두 조건을 **모두** 만족할 때만 `ready` 가 `true` 입니다.
  - 기본 태스크의 모션 상태가 지령 출력 대기(`MotMoveReadyState`) 상태인 경우
  - 프로그램 재생이 정지되지 않은 경우 (자동 모드에서 Job 이 실행 중)
- `ready` 가 `false` 인 상태에서 궤적 지령을 보내면 제어기가 `외부지령 동작 가능상태가 아닙니다` 에러를 발생시키고 내부 버퍼를 클리어합니다. 이때 궤적 로그 저장 기능도 함께 자동 해제됩니다.

##### path-parameter

<div style="width: fit-content;">

```text
GET /project/robot/trajectory/joint_traject_ready
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
   - ready : 외부 궤적 지령 시작 가능 여부 (boolean)

<div style="width: fit-content;">

```json
{"ready": true}
```
</div>

##### 사용 절차

1. 로봇을 안전한 기준 자세로 이동시킵니다.
2. Job 에 `wait di1` 등의 대기 구문을 두고 자동 모드에서 프로그램을 재생합니다.
3. 본 API 로 `ready == true` 를 확인합니다.
4. [joint_traject_init](../2-post/7-joint_traject_init.md) 으로 버퍼를 초기화한 후 궤적 포인트를 송신합니다.
5. `ready == false` 이면 포인트를 보내지 말고 프로그램 재생 상태와 제어기 에러 상태를 먼저 확인합니다.

{% hint style="info" %}

프로그램이 실행 중이 아닌 상태에서 궤적 API 를 호출하면 [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) 가 발생할 수 있습니다.
제한 속도를 초과하는 궤적은 [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) 를 발생시키며 로봇이 정지할 수 있습니다.

{% endhint %}

##### 사용 예

```text
request url:
GET /project/robot/trajectory/joint_traject_ready

response-body:
{
    "ready": true
}
```

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import time
import requests


def wait_traject_ready(base_url: str, session: requests.Session, timeout: float = 10.0) -> bool:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_ready"
    deadline = time.time() + timeout

    while time.time() < deadline:
        try:
            ret = session.get(url=uri)
            ret.raise_for_status()
            if ret.json().get("ready") is True:
                return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False
        time.sleep(0.1)

    return False


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        print(wait_traject_ready(base_url, session))
```
```sh
$python test.py
True
```
</div>
