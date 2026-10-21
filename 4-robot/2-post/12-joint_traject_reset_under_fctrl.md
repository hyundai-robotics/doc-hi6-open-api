#### 4.2.12 `joint_traject_reset_under_fctrl`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `POST` : [joint_traject_init](./7-joint_traject_init.md) 의 `fctrl_mode` 가 `true` 인 모드에서 **궤적을 재실행할 때 필요한 궤적 상태 리셋** API 입니다.
- `fctrl_mode` 값에 따라 재실행 절차가 다릅니다.

<div style="width: fit-content;">

| `fctrl_mode` | 최초 실행 | 재실행 |
| ----- | ------ | ------ |
| `false` | `joint_traject_init` | `joint_traject_init` |
| `true` | `joint_traject_init` | **`joint_traject_reset_under_fctrl`** |

</div>

- [joint_traject_init](./7-joint_traject_init.md) 은 궤적 모드 동작 중([joint_traject_mode](../1-get/10-joint_traject_mode.md) 가 `true`)에는 초기화를 수행하지 않으므로, `fctrl_mode : true` 모드에서는 본 API 로 리셋해야 합니다.

##### 선행 조건

힘 제어 기능은 **단독으로 동작하지 않습니다.** 다음이 모두 필요합니다.

1. 제어기 힘 제어 **환경 설정**
2. 힘 제어 **라이센스**
3. [joint_traject_init](./7-joint_traject_init.md) 을 `fctrl_mode : true` 로 요청하여 진입한 모드

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_reset_under_fctrl
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

{% hint style="warning" %}

- 궤적 **이동 중**에 호출하면 버퍼의 궤적 포인트가 사라져 로봇이 정지하면서 에러가 발생할 수 있습니다. 직전 궤적이 끝난 후 호출하시기 바랍니다.
- 타임아웃 시 자동 재시도하지 말고, 처리 여부를 확인한 후 재실행하시기 바랍니다.

{% endhint %}

##### 사용 예

<div style="width: fit-content;">

```joint_traject_reset_under_fctrl
POST /project/robot/trajectory/joint_traject_reset_under_fctrl

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
uri = f"{base_url}/project/robot/trajectory/joint_traject_reset_under_fctrl"

try:
    response = requests.post(uri, json={}, timeout=5)
    response.raise_for_status()
    print(response.status_code, response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")
```
```sh
$ python test.py
200 {'_type': 'JObject'}
```

200 응답은 궤적 상태 리셋이 완료되어 다음 궤적을 송신할 수 있음을 의미합니다.
</div>
