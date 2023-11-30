### 1.3.2 예제 코드 - python

예제 코드는 크게 `a. 동기식 요청(blocking & 동기식)`방식과 `b. 비동기식 요청(non-blocking & 비동기식)` 두 가지 방식에 대해서 설명합니다.

||동기식|비동기식|
|:---|:---|:---|
|blocking|`a. 동기식 요청`||
|non-blocking||`b. 비동기식 요청`|

두 가지 방법의 차이점은 TP와 컨트롤러에 다음과 같은 심각한 결과를 초래할 수 있습니다.
1. UI 스레드에서 빈번한 동기 함수 호출로 인해 UI가 원활하게 실행되지 않고 정지될 수 있습니다(`Hanging problem`).
2. 서버(컨트롤러) 측의 문제로 인해 응답을 받지 못하는 경우, 애플리케이션 UI가 정지될 수 있습니다(`Hanging problem`).

따라서 실제 애플리케이션을 개발할 때에는 비동기식 요청 기반으로 작성하시기 바랍니다.
- Hi6 Open API 설명에 작성된 Python 스크립트 예시는 이해하기 쉽도록 동기적으로 작성되었으니 유의하시기 바랍니다.

<br>

## a. 동기식 요청
- 동기식은 하나의 요청이 끝나고 응답이 올 때까지 다른 task 의 실행이 불가능한 blocking 상태의 요청 방식 입니다.
- 코드가 간단하지만, 통신 시 응답이 오지 않거나 응답을 받는데 오랜 시간이 걸리는 경우 제어기에 문제가 생길 가능성이 매우 커집니다.
- python 에서 `동기식` HTTP 요청을 위해 많이 사용되는 라이브러리는 `requests` 입니다.
- `requests` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다. 
	```sh
	$pip install requests
	```

```python
# sync.py - 동기식, 사용자 IO 출력 값 얻기와 설정하기
import requests
import time

url='http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) fb2.do3 값 설정하기
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
start_time = time.time()
resp = requests.post(url + path, headers=head, json=req_body)
end_time = time.time()
print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

# (GET) fb2.do3 값 가져오기
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")
```
```bash
$python sync.py
[post] 0x79 to fb2.do3 Time taken: 0.00599980354309082 seconds
[get] 0x79 from fb2.do3 Time taken: 0.004000186920166016 seconds
```

## b. 비동기식 요청
- 이를 보완한 방식이 비동기식 통신으로, 요청 시 콜백 함수를 동작시켜 해당 콜백 함수에서 요청 사항을 처리하여 도중에 다른 task 가 실행가능한 방식입니다.
- 비동기식은 동기식과 다르게, 작업 완료 순서를 보장하지 않는 다는 점이 차이가 있지만, 모든 요청이 거의 동시에 시작되므로, 전체적인 응답 시간이 짧아질 수 있습니다.
- python 은 `asyncio` 라는 비동기 프로그래밍 구현 용 빌트인 라이브러리를 제공하고 있습니다. 이를 통해 CPU 작업과 I/O를 병렬로 처리하게 해줍니다.
- 추가로, `비동기식` HTTP 요청을 위해 많이 사용되는 라이브러리는 `aiohttp` 입니다.
- `aiohttp` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다.
	```sh
	$pip install aiohttp
	```

```python
# async.py - 비동기식, 사용자 IO 출력 값 얻기와 설정하기
import asyncio
import aiohttp
import time

url = 'http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3}

async def set_value(session):
    val = 0x60
    req_body = {'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val': val}
    start_time = time.time()
    async with session.post(url + path, headers=head, json=req_body) as resp:
        pass  # 필요한 경우 여기서 응답 처리
    end_time = time.time()
    print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def get_value(session):
    start_time = time.time()
    async with session.get(url + path, headers=head, params=query) as resp:
        resp_body = await resp.json()
    end_time = time.time()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def main():
    async with aiohttp.ClientSession() as session:
        await set_value(session)
        tasks = [get_value(session) for _ in range(10)]
        await asyncio.gather(*tasks)

asyncio.run(main())
```
```bash
$python async.py
[post] 0x79 to fb2.do3 Time taken: 0.0039997100830078125 seconds
[get] 0x79 from fb2.do3 Time taken: 0.0029997825622558594 seconds
```