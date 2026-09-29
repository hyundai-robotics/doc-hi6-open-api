#### 4.2.10 `joint_traject_off`

##### 설명

- 지원 버전 : `70.06-00` ↑ (예정)
- `POST` : 현재 동작 중인 외부 궤적(온라인 트래킹) 모드의 종료를 요청합니다.
- 요청은 종료를 **지시**할 뿐이며, 제어기 내부 종료 처리가 끝날 때까지 시간이 소요됩니다.
  - 종료 완료 여부는 반드시 [joint_traject_mode](../1-get/10-joint_traject_mode.md) 가 `false` 가 되는 것으로 확인해야 합니다.
- 종료가 완료되기 전에 다음 궤적을 송신하면 의도치 않은 에러가 발생할 수 있습니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_off
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

##### 종료 및 복구 절차

1. `joint_traject_off` 를 요청합니다.
2. [joint_traject_mode](../1-get/10-joint_traject_mode.md) 를 폴링하여 `mode == false` 가 될 때까지 대기합니다.
3. 민첩 모드를 사용했다면 모션 종료 후 최소 `0.5 초` 의 제어기 내부 clean-up 이 완료되기를 기다립니다.
4. 에러로 정지한 경우, 다음 궤적 송신 전에 [joint_traject_init](./7-joint_traject_init.md) 으로 남아 있는 버퍼를 초기화합니다.
5. [joint_traject_ready](../1-get/11-joint_traject_ready.md) 로 준비 상태를 다시 확인한 후 궤적 송신을 재개합니다.

{% hint style="warning" %}

민첩 모드 사용 시, 모션 종료 후 `0.5 초` 의 제어기 내부 clean-up 과정이 필요합니다.
이를 어기고 곧바로 궤적을 이어서 보내는 경우, 의도치 않은 에러가 발생할 수 있습니다.

{% endhint %}

##### 사용 예

<div style="width: fit-content;">

```joint_traject_off
POST /project/robot/trajectory/joint_traject_off

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
uri = f"{base_url}/project/robot/trajectory/joint_traject_off"

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

200 응답은 종료 요청이 접수되었다는 의미입니다. 다음 궤적을 보내기 전 [joint_traject_mode](../1-get/10-joint_traject_mode.md) 의 `mode == false` 를 확인해야 합니다.
</div>
