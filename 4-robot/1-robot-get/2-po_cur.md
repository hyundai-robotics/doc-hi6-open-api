# 4.1.2 `po_cur`

## 설명

`po_cur` (`po`se `cur`rent)

- `GET` : 현재 로봇이 취하고 있는 pose(자세)를 얻습니다.

## path-parameter

```python
GET /project/robot/po_cur
```

## query-parameter

- task_no : task 번호 (0~7).
  - 미지정 : task 0으로 적용됨.
  - &gt;=0 : mechinfo 미지정 시, task의 현재 mechinfo가 적용됨.
- crd :  
  - 미지정 : tcp, axis, encoder를 모두 얻음.
  - <0 : 현재 기록 좌표계를 따름.
  - &gt;=0 : [좌표계](/7-schema/crdsys.md)
- ucrd_no : 사용자좌표계 번호 (crd가 user일 때만 지정함.)
- mechinfo : [메커니즘 정보](/7-schema/mechinfo.md)

## response-body

- [포즈 정보](/7-schema/pose.md)


## 사용 예

로봇 6축(j1~j6) + 주행 1축(j7) + 포지셔너 2축(j8, j9)인 시스템의 사례.

- 로봇의 base 좌표만 얻기

```python
request url:
GET /project/robot/po_cur?crd=0&mechinfo=1

response-body:
{
	"nsync" : 0,
	"_type" : "Pose",
	"rx" : 0.000000,
	"x" : 1782.000000,
	"ry" : 90.000000,
	"y" : 0.000000,
	"rz" : 0.000000,
	"z" : 1938.000000,
	"mechinfo" : 1,
	"crd" : "base"
}
```

- 전 축의 축좌표 얻기

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=-1

response-body:
{
	"nsync" : 0,
	"_type" : "Pose",
	"mechinfo" : 65535,
	"j9" : 0.000000,
	"crd" : "joint",
	"j1" : 0.000000,
	"j2" : 90.000000,
	"j3" : 0.000000,
	"j4" : 0.000000,
	"j5" : 0.000000,
	"j6" : 0.000000,
	"j7" : 0.000000,
	"j8" : 0.000000
}
```

- 포지셔너 2축 (즉, 메커니즘 M2)의 축좌표 얻기

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=4

response-body:
{
	"nsync" : 0,
	"_type" : "Pose",
	"mechinfo" : 4,
	"j9" : 0.000000,
	"crd" : "joint",
	"j8" : 0.000000
}
```

<details><summary>Python Script 예시</summary>

```python
# test.py
import requests

def get_base_coordinate() -> dict:
	base_url        = 'http://192.168.1.150:8888'
	path_parameter  = '/project/robot/po_cur'
	query_parameter = {'crd': 0, 'mechinfo': 1}

	response = requests.get(url = base_url + path_parameter, params = query_parameter).json()

	return response

print(get_base_coordinate())
```
```sh
$python test.py
{'nsync': 0, '_type': 'Pose', 'rx': 0.0, 'x': 1067.366, 'ry': 73.248, 'y': -12.859, 'rz': -0.69, 'z': 1609.909, 'mechinfo': 1, 'crd': 'base', 'j1': 0.0, 'j2': 0.0, 'j3': 0.0, 'j4': 0.0, 'j5': 0.0, 'j6': 0.0}
```

</details>