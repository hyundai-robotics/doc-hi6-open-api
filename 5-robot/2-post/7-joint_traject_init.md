## 5.2.7 `joint_traject_init`

### 설명

- 지원 버전 : `60.32-00` &uparrow;
- `POST` : 버퍼를 초기화를 진행합니다.
- 로봇이 정지 상태에서 궤적을 요청할 때, 직전에 저장된 궤적을 지워줍니다.
- 다음과 같은 상황에서도 버퍼 초기화를 진행해주어야 합니다.
  - traj1 요청 &rightarrow; 로봇 이동 중 에러 발생 후 정지 &rightarrow; **버퍼 초기화** &rightarrow; traj2 요청
  - 에러가 발생한 시점의 궤적이 버퍼에 저장되어있어 버퍼 초기화 없이 traj2 요청을 하면 에러가 발생할 수 있습니다.
- [joint_traject_insert_points](./8-joint_traject_insert_points.md) api 로 궤적을 이동중에 <u>해당 함수를 호출하면 그 즉시 버퍼가 갱신</u>이 됩니다.
  - 기존 버퍼에 저장된 궤적 포인트들이 사라지면 로봇이 정지되면서 에러가 발생할 수 있으므로 사용에 주의 하시기 바랍니다.


### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

### request-body

<div style="width: fit-content;">

- {}

</div>



### response

1) status code
   - 200 : OK
   - 400 : Bad Request
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

### 사용 예

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}

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
