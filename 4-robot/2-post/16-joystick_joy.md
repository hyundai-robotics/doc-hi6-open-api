#### 4.2.16 `joystick/joy`

##### 설명

- 지원 버전 : `70.04-00` ↑
- `POST` : 외부 장치에서 전달한 방향 입력으로 로봇을 조그합니다.
- 본 API는 **방향 조그**용입니다. 스틱 기울기에 비례한 연속 속도 제어나 JOB 실행 중 경로 수정 API가 아닙니다.

##### 사전 조건

1. **조이스틱 가능**에 입력 신호를 할당하고, 조이스틱 모드를 사용하는 동안 해당 신호를 **ON**으로 유지합니다.
   - **TP630:** 시스템 → 4: 응용 파라미터 → 16: 조이스틱 모드 → 일반 설정 → 조이스틱 가능 신호 번호 입력 → 확인
   - **조이스틱 가능** 입력란에 신호 번호 `0`을 입력하면 `di0`이 할당됩니다. 조이스틱을 사용하려면 `di0`이 **ON** 상태여야 합니다.
2. 같은 화면에서 **실행 타입**을 **Open-api**로 설정합니다.
3. **모터 온** 및 **원격 자동 모드** 상태에서 해당 API를 사용할 수 있습니다.
4. 실행 중인 **JOB이나 태스크**가 없어야 합니다.

참고: [조이스틱 모드](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/ko-tp630/7-system/5-application-parameter/16-joystick-mode/README?cont_model=Hi6)


##### path-parameter

<div style="max-width: fit-content;">

```text
POST /project/robot/joystick/joy
```

##### request-body

```json
{
  "axes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

</div>

`axes`는 10개 값을 모두 전송하고, 사용하지 않는 축은 `0`으로 보냅니다.

메커니즘, [조그 좌표계](./4-crd_sys.md), [툴](./3-tool_no.md), 조그 속도는 기존 설정을 따릅니다.

###### 인덱스별 방향 매핑

| index | `-1` | `0` | `1` |
|:---:|:---|:---:|:---|
| 0 | Left | 중립 | Right |
| 1 | Forward | 중립 | Backward |
| 2 | Down | 중립 | Up |
| 3 | R2- | 중립 | R2+ |
| 4 | B- | 중립 | B+ |
| 5 | R1- | 중립 | R1+ |
| 6 | R3- | 중립 | R3+ |
| 7 | J8- | 중립 | J8+ |
| 8, 9 | 사용하지 않음 | **0으로 전송** | 사용하지 않음 |

표는 조그키 기준이며, 실제 이동 방향은 설정과 기종에 따라 달라질 수 있습니다.

##### 주의 사항

첫 사용 시 승인된 안전 절차에 따라 저속으로 이동 방향을 확인하십시오.

{% hint style="warning" %}
**빈 배열이나 짧은 배열은 이전 조그 입력을 남길 수 있습니다. 모든 조그 입력을 중립으로 바꾸려면 `0`을 10개 보내십시오.**

중립 요청만으로 로봇이 실제로 정지했는지 확인할 수는 없습니다.
{% endhint %}

###### 수신 타임아웃

- 조그 입력의 수신 타임아웃은 **300 ms**입니다. 조그 동작 조건이 유지된 상태에서 이 시간 동안 정상 요청이 없으면 조그 입력이 해제됩니다.
- 통신이나 조그 동작 조건이 복구되면, 이전 방향을 자동으로 다시 보내지 말고 중립 상태와 재가동 조건을 확인하십시오.

{% hint style="warning" %}
300 ms는 로봇의 정지 시간이 아닙니다. 이 API는 비상정지나 인명 보호 장치를 대신하지 않습니다.
{% endhint %}

##### response

1) status code
   - 200 : OK
     - 요청 처리 성공을 뜻하며, 로봇의 이동 또는 정지 완료를 뜻하지 않습니다.
   - 400 : Bad Request
     - 요청 본문을 해석할 수 없거나 동작 조건 또는 `axes` 입력이 올바르지 않은 경우
   - 404 : Not Found

2) response-body

<div style="max-width: fit-content;">

   ```json
   {}
   ```

3) error code
   - -39010: 사전 조건을 충족하지 않은 경우
   - -39011: `axes` 입력이 올바르지 않은 경우

##### 사용 예

```json
POST /project/robot/joystick/joy

request-body
{
  "axes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

Python Script 예시

```python
import requests


def post_joystick_joy() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    url = f"{base_url}/project/robot/joystick/joy"
    body = {"axes": [0] * 10}

    return requests.post(url, json=body)


response = post_joystick_joy()
print((response.status_code, response.json()))
```

```sh
$python test.py
(200, {})
```

</div>
