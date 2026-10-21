#### 4.2.15 `fctrl_stop`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `POST` : **힘 제어 및 동작 중단(Halt)** 을 요청합니다.
- [fctrl_run](./13-fctrl_run.md) 으로 시작한 힘 제어 동작을 중단합니다.
- 요청은 중단을 **지시**할 뿐이며, 제어기 내부 종료 처리가 끝날 때까지 시간이 소요됩니다.
- 입력 파라미터는 없습니다.

{% hint style="danger" %}

본 API 는 **하드웨어 비상 정지를 대체하지 않습니다.**

네트워크를 경유하는 소프트웨어 중단 요청이므로, 통신 지연이나 단절 시 즉시 정지가 보장되지 않습니다.
안전이 요구되는 정지에는 반드시 하드웨어 비상 정지 장치를 사용하시기 바랍니다.

{% endhint %}

##### 선행 조건

힘 제어 기능은 **단독으로 동작하지 않습니다.** 본 API 를 사용하기 전에 다음 조건이 **모두** 충족되어야 합니다.

<div style="width: fit-content;">

| 선행 조건 | 내용 |
| ----- | ------ |
| 힘 제어 환경 설정 | 제어기에 힘 제어 관련 **환경 설정이 완료**되어 있어야 합니다. |
| 힘 제어 라이센스 | 제어기에 **힘 제어 라이센스가 등록**되어 있어야 합니다. |
| 힘 제어 궤적 모드 | [joint_traject_init](./7-joint_traject_init.md) 을 `fctrl_mode : true` 로 요청하여 진입한 모드여야 합니다. |

</div>

{% hint style="danger" %}

위 조건 중 하나라도 충족되지 않으면 힘 제어 기능은 동작하지 않습니다.

- 제어기 **환경 설정이 되어 있지 않거나 힘 제어 라이센스가 없는 경우** 동작하지 않습니다.
- [joint_traject_init](./7-joint_traject_init.md) 의 `fctrl_mode` 가 `true` 로 설정된 모드가 **아닌 상태에서는 본 API 를 단독으로 사용할 수 없습니다.**

{% endhint %}

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/force_control/ctrl/stop
```
</div>

##### request-body

<div style="width: fit-content;">

```
{} : 입력 파라미터 없음
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
   - 404 : Not Found

2) response-body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```
</div>

##### 관련 API

<div style="width: fit-content;">

| API | 용도 |
| ----- | ------ |
| [fctrl_run](./13-fctrl_run.md) | 힘 제어 동작 **시작** |
| [fctrl_control](./14-fctrl_control.md) | 힘 제어 조건(`cnd`) **변경** |
| `fctrl_stop` | 힘 제어 및 동작 **중단** |
| [joint_traject_off](./10-joint_traject_off.md) | 외부 궤적 모드 **종료** |
| [emergency_stop](./5-emergency_stop.md) | 비상 정지 |

</div>

{% hint style="warning" %}

- 힘 제어 궤적 모드([joint_traject_init](./7-joint_traject_init.md) 의 `fctrl_mode : true`)를 함께 사용한 경우, 궤적 모드 종료는 [joint_traject_off](./10-joint_traject_off.md) 로 별도 수행해야 합니다. 종료 완료 여부는 [joint_traject_mode](../1-get/10-joint_traject_mode.md) 가 `false` 가 되는 것으로 확인하시기 바랍니다.
- 상태를 변경하는 요청이므로 **자동 재시도를 적용하지 마십시오.** 타임아웃이 발생해도 제어기가 이미 중단을 수행했을 수 있습니다. 제어기 상태를 확인한 후 재실행 여부를 판단하시기 바랍니다.
- 클라이언트 프로그램이 오류나 `Ctrl+C` 로 종료되어도, **이미 접수된 로봇 동작은 계속될 수 있습니다.** 프로그램 종료가 곧 로봇 정지를 의미하지 않습니다.
- 리다이렉트(3xx) 응답은 정상 응답으로 처리하지 말고 오류로 처리하시기 바랍니다.

{% endhint %}

##### 사용 예

<div style="width: fit-content;">

```fctrl_stop
POST /project/force_control/ctrl/stop

request-body
{}

response-body
{'_type': 'JObject'}
```

Python Script 예시

```python
# test.py
import requests

base_url = "http://192.168.1.150:8888"
# base_url = "http://127.0.0.1:8888"  # hrspace

# 연결 / 읽기 타임아웃을 분리해서 지정합니다. 실시간 보장 값이 아닙니다.
REQUEST_TIMEOUT = (3.05, 10.0)


def post_json(session, path, body):
    """상태 변경 POST. 실패를 전파하여 후속 명령이 이어지지 않도록 합니다."""
    response = session.post(
        base_url + path,
        json=body,
        timeout=REQUEST_TIMEOUT,
        allow_redirects=False,
    )
    response.raise_for_status()
    if 300 <= response.status_code < 400:
        raise requests.HTTPError(f"Unexpected redirect: {response.status_code}")
    print(f"[INFO] {path} OK: status={response.status_code}")
    response.close()


def fctrl_stop(session):
    """힘 제어 및 동작 중단 요청 (Halt). 하드웨어 비상 정지를 대체하지 않습니다."""
    post_json(session, "/project/force_control/ctrl/stop", {})


def main():
    with requests.Session() as session:
        print("[ACTION] 힘 제어 정지 (Halt)...")
        fctrl_stop(session)


if __name__ == "__main__":
    main()
```
```sh
$ python test.py
[ACTION] 힘 제어 정지 (Halt)...
[INFO] /project/force_control/ctrl/stop OK: status=200
```

200 응답은 중단 요청이 접수되었다는 의미입니다. 중단 완료 여부는 제어기 상태로 확인해야 합니다.
</div>
