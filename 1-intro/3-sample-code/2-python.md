# 1.3.2 예제 코드 - python

```python
# 사용자 IO 출력 값 얻기와 설정하기
import requests

uri='http://192.168.1.150:8888'

head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# fb2.do3 값 얻기 (GET)
resp = requests.get(uri+path, headers=head, params=query)
resp_body = resp.json()
print('fb2.do3=' + str(resp_body['val']))

# fb2.do3에 0xc1 설정하기 (POST)
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : 0xc1 }
resp = requests.post(uri + path, headers=head, json=req_body)
```
