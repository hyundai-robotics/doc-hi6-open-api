#### 4.2.11 `joint_traject_log`

##### 설명

- 지원 버전 : `70.04-00` ↑
- `POST` : 조인트 궤적 로그 저장 기능을 활성화하거나 비활성화합니다.
- 활성화 시 제어기는 궤적 링버퍼의 동작(`RECV`, `WRTE`, `READ`, `INTP`, `SEND`, `EMPTY`)과 각 시점의 조인트 위치, 버퍼 인덱스를 로그로 기록합니다.
- 현재 활성화 상태는 [GET joint_traject_log](../1-get/12-joint_traject_log.md) 로 확인합니다.
- 궤적 디버깅 용도의 API 이며, 상시 활성화하는 것은 권장하지 않습니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_log
```
</div>

##### request-body

<div style="width: fit-content;">

```json
{"enable": true}
```

| 파라미터명| 속성 | 타입 | 기본값 | 설명 및 제약 조건|
| ----- | ------ | ------ | ------ | ------|
| `enable` | Required | boolean | false | `true` : 로그 저장 활성화, `false` : 비활성화. 파라미터를 생략하거나 boolean 이 아닌 타입을 대입하면 요청이 실패합니다. |

</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - `enable` 파라미터가 없는 경우
     - `enable` 값이 boolean 타입이 아닌 경우
   - 404 : Not Found

2) response-body

<div style="width: fit-content;">

```json
{ "_type": "JObject"}
```
</div>

{% hint style="info" %}

실패한 경우에도 response-body 는 `{"_type": "JObject"}` 로 동일하게 반환됩니다.
설정이 실제로 반영되었는지는 [GET joint_traject_log](../1-get/12-joint_traject_log.md) 의 `val` 값으로 확인하시기 바랍니다.

{% endhint %}

{% hint style="warning" %}

외부 궤적 지령이 동작 가능 상태가 아니어서 제어기가 지령을 거부한 경우, 로그 저장은 제어기에 의해 자동으로 비활성화됩니다.
에러 발생 후 로그를 계속 남기려면 재시작 시 본 API 로 다시 활성화해야 합니다.

{% endhint %}

##### 사용 예

<div style="width: fit-content;">

```joint_traject_log
POST /project/robot/trajectory/joint_traject_log

request-body
{"enable": true}

response-body
{'_type': 'JObject'}
```

Python Script 예시

```python
# test.py
from typing import Union

import requests


def set_joint_traject_log(
    base_url: str, session: requests.Session, enable: bool
) -> Union[requests.Response, None]:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = session.post(url=uri, headers=headers, json={"enable": enable})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to set trajectory log: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    uri = f"{base_url}/project/robot/trajectory/joint_traject_log"

    with requests.Session() as session:
        response = set_joint_traject_log(base_url, session, True)
        if response is None:
            return
        print(response.status_code, response.json())

        # 반영 여부 확인
        print(session.get(url=uri).json())


if __name__ == "__main__":
    main()
```
```sh
$python test.py
200 {'_type': 'JObject'}
{'val': 1}
```
</div>
