#### 4.2.14 `fctrl_control`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `POST` : 적용 중인 **힘 제어 조건(`cnd`)을 변경**합니다.
- [fctrl_run](./13-fctrl_run.md) 으로 힘 제어 동작을 시작한 이후, 동작을 중단하지 않고 조건만 교체할 때 사용합니다.
- 요청은 조건 변경을 **지시**할 뿐이며, 제어기 내부 처리가 완료될 때까지 시간이 소요됩니다.

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
POST /project/force_control/ctrl/control
```
</div>

##### request-body

<div style="width: fit-content;">

```json
{ "cnd": 2 }
```

| 파라미터명 | 속성 | 타입 | 기본값 | 설명 및 제약 조건 |
| ----- | ------ | ------ | ------ | ------ |
| `cnd` | Required | integer | - | 변경할 힘 제어 조건 번호. 잘못된 타입이나 등록되지 않은 조건 번호를 대입하면 400 Bad Request 를 반환 |

</div>

{% hint style="warning" %}

`cnd` 는 제어기에 **미리 등록된 힘 제어 조건**을 가리키는 번호입니다.
등록되지 않은 번호를 지정하면 의도치 않은 동작이나 에러가 발생할 수 있으므로, 사용 전에 해당 조건이 등록되어 있는지 확인하시기 바랍니다.

{% endhint %}

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - `cnd` 가 누락되었거나 타입이 잘못된 경우
     - 등록되지 않은 힘 제어 조건 번호를 지정한 경우
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
   - 404 : Not Found

2) response-body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```
</div>

##### `fctrl_run` 과의 차이

<div style="width: fit-content;">

| 구분 | [fctrl_run](./13-fctrl_run.md) | `fctrl_control` |
| ----- | ------ | ------ |
| 역할 | 힘 제어 동작 **시작** | 적용 중인 힘 제어 조건 **변경** |
| 사용 시점 | 힘 제어 미동작 상태 | [fctrl_run](./13-fctrl_run.md) 으로 동작을 시작한 이후 |
| path | `/project/force_control/ctrl/run` | `/project/force_control/ctrl/control` |
| request-body | `{"cnd": <조건 번호>}` | `{"cnd": <조건 번호>}` |

</div>

{% hint style="warning" %}

- 힘 제어 **동작 중** 조건을 변경하면 로봇의 거동이 즉시 달라집니다. 조건 변경에 따른 힘/속도 변화를 사전에 확인한 후 사용하시기 바랍니다.
- 상태를 변경하는 요청이므로 **자동 재시도를 적용하지 마십시오.** 타임아웃이 발생해도 제어기가 이미 명령을 수행했을 수 있습니다. 제어기 상태를 확인한 후 재실행 여부를 판단하시기 바랍니다.
- 클라이언트 측에서 요청을 병렬화하지 말고, 하나의 세션을 재사용하여 **명령 순서를 유지**하시기 바랍니다.
- 리다이렉트(3xx) 응답은 정상 응답으로 처리하지 말고 오류로 처리하시기 바랍니다.

{% endhint %}

##### 사용 예

<div style="width: fit-content;">

```fctrl_control
POST /project/force_control/ctrl/control

request-body
{"cnd": 2}

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


def fctrl_run(session, cnd):
    """힘 제어 기반 동작 시작 (Run). 요청 실패 시 예외를 전달합니다."""
    post_json(session, "/project/force_control/ctrl/run", {"cnd": cnd})


def fctrl_control(session, cnd):
    """힘 제어 조건 변경 (Control). 요청 실패 시 예외를 전달합니다."""
    post_json(session, "/project/force_control/ctrl/control", {"cnd": cnd})


def main():
    # 같은 세션을 재사용하여 명령 순서를 유지합니다.
    with requests.Session() as session:
        print("[ACTION] 힘 제어 시작 (Run)...")
        fctrl_run(session, 1)

        print("[ACTION] 힘 제어 cnd 변경...")
        fctrl_control(session, 2)


if __name__ == "__main__":
    main()
```
```sh
$ python test.py
[ACTION] 힘 제어 시작 (Run)...
[INFO] /project/force_control/ctrl/run OK: status=200
[ACTION] 힘 제어 cnd 변경...
[INFO] /project/force_control/ctrl/control OK: status=200
```

200 응답은 힘 제어 조건 변경 요청이 접수되었다는 의미입니다.
</div>
