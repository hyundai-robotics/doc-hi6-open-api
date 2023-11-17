# 1.3.2 예제 코드 - python

- 해당 문서는 HTTP 요청을 위해 많이 사용되는 `requests` 라이브러리를 사용합니다.
- `requests` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다. 
	```sh
	pip install requests
	```
	
```python
# test_io_info.py - 사용자 IO 출력 값 얻기와 설정하기
import requests

uri='http://192.168.1.150:8888'

head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) fb2.do3 값 설정하기
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
print('[post]', hex(val), 'to fb2.do3')
resp = requests.post(uri + path, headers=head, json=req_body)

# (GET) fb2.do3 값 가져오기
resp = requests.get(uri+path, headers=head, params=query)
resp_body = resp.json()
print('[get]', hex(resp_body['val']), 'from fb2.do3')
```
```bash
$python test_io_info.py
[post] 0x79 to fb2.do3
[get] 0x79 from fb2.do3
```
