#### 5.1.7 `joint_traject_buf_avail`

##### Description
- Supported Version : `60.32-00` &uparrow;
- `GET` : Returns the available size of the trajectory buffer.
- When requesting trajectories consecutively, you must use this function to ensure that the size of each trajectory request does not exceed the available buffer space.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

##### response-body

- val: Number of available buffer slots (maximum: 2048)

##### status code
  - 200 : Request succeeded
  - 403 : Request failed
    - Returned when calling an unsupported API

##### Example

```python
request url:
GET /project/robot/trajectory/joint_traject_buf_avail

response-body:
{
    "val": 2048,
}
```
</div>

Python Script Example

<div style="width: fit-content;">

```python
# test.py
import requests


def get_jt_buff_avail_num(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_buf_avail"
    try:
        ret = session.get(url=uri)
        ret.raise_for_status()
        return ret.json()
    except Exception as e:
        print(f"[ERROR] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        ret = get_jt_buff_avail_num(base_url, session)
        print(ret)
```
```sh
$python test.py
{'val': 2048}
```
</div>
