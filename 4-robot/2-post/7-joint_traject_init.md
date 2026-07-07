#### 4.2.7 `joint_traject_init`

##### 설명

- 지원 버전 : `60.32-00` ↑
- `POST` : 버퍼를 초기화를 진행합니다.
- 로봇이 정지 상태에서 궤적을 요청할 때, 직전에 저장된 궤적을 지워줍니다.
- 다음과 같은 상황에서도 버퍼 초기화를 진행해주어야 합니다.
  - traj1 요청 &rightarrow; 로봇 이동 중 에러 발생 후 정지 &rightarrow; **버퍼 초기화** &rightarrow; traj2 요청
  - 에러가 발생한 시점의 궤적이 버퍼에 저장되어있어 버퍼 초기화 없이 traj2 요청을 하면 에러가 발생할 수 있습니다.
- [joint_traject_insert_points](./8-joint_traject_insert_points.md) api 로 궤적을 이동중에 <u>해당 함수를 호출하면 그 즉시 버퍼가 갱신</u>이 됩니다.
  - 기존 버퍼에 저장된 궤적 포인트들이 사라지면 로봇이 정지되면서 에러가 발생할 수 있으므로 사용에 주의 하시기 바랍니다.

##### `70.04-00` ↑ 변경 사항

`joint_traject_insert_point` 의 민첩 모드가 추가 되었습니다.  

<div style="width: fit-content;">

```json
{ "agility_mode": true, "agility_freq": 30 }
```
</div>

<div style="width: fit-content;">


|설정 항목|  설명 |
| ----- |  ------ |
| `agility_mode` | 타겟 지령으로 도달하는 로봇의 초기 제어 반응 속도를 비약적으로 향상 시키는 모드입니다. |
| `agility_freq` | 민첩 모드의 대역폭 동작 주파수를 지정합니다. 설정된 주파수 값이 높을수록 로봇의 응답 속도가 빨라지고 민첩성이 증가합니다. |


민첩성 관련 파라미터가 포함되지 않거나 빈 중괄호({})로 요청하는 경우, 민첩성 모드는 자동으로 비활성화(false)됩니다

</div>

{% hint style="info" %}

`진동 및 소음 유의`: 주파수 값을 크게 설정할수록 제어계의 응답성이 급격히 정밀해지지만, 로봇의 기계적 강성 및 환경 조건에 따라 고주파 소음이나 시스템 진동을 유발할 수 있습니다.  
`안전 구동 팁`: 최초 설정 시에는 시스템 안정성을 위해 낮은 주파수 대역에서 시작하여, 로봇의 거동과 소음을 모니터링하면서 점진적으로 주파수를 높여 최적의 제어 포인트를 찾으십시오.

{% endhint %}


##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

##### request-body

<div style="width: fit-content;">

```
{} : 일반 모드
```

`70.04-00` 이후 추가 된 속성

```
{"agility_mode": True, "agility_freq": 30} : 민첩 모드
```


| 파라미터명| 속성 | 타입 | 기본값 | 설명 및 제약 조건|
| ----- | ------ | ------ | ------ | ------|
| `agility_mode` | Optional | boolean |  false | string 등 잘못된 타입 대입 시 400 Bad Request 에러를 반환 |
| `agility_freq` | Optional | integer | 20 | 생략 시 기본 디폴트 주파수로 자동 적용. 제어기 물리 허용 범위(0 ~ 500)를 벗어나거나 잘못된 타입 대입 시 400 Bad Request 에러를 반환 |


</div>



##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - V70.04-00 ↑
        - `err_msg` : 에러 내용 반환
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
     - `err_code` (<0) : 초기화 실패
   - 404 : Not Found

2) response body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```

</div>

##### 사용 예

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
ex1)
{}

ex2) V70.04-00 ↑
{"agility_mode": true, "agility_freq": 30}

response-body
{'_type': 'JObject'}
```

Python Script 예시
```python
# test.py
from typing import Union
import requests


def post_init_trajectories(
    base_url: str, session: requests.Session
) -> Union[requests.Response, None]:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_init"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = session.post(url=uri, headers=headers)
        response.raise_for_status()
        print(f"[INFO] Initialization successful: status={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to initialize trajectory buffer: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace

    with requests.Session() as session:
        response = post_init_trajectories(base_url, session)
        print(response)


if __name__ == "__main__":
    main()

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>
