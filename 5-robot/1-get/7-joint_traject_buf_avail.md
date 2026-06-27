#### 5.1.7 `joint_traject_buf_avail`

##### 描述
- 支持版本 : `60.32-00` &uparrow;
- `GET` : 返回轨迹缓冲区的可用大小。
- 在连续请求轨迹时，您必须使用此函数以确保每个轨迹请求的大小不超过可用缓冲区空间。

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

##### response-body

- val: 可用缓冲槽的数量（最大：2048）

##### 状态码
  - 200 : 请求成功
  - 403 : 请求失败
    - 调用不支持的 API 时返回

##### 示例

```python
request url:
GET /project/robot/trajectory/joint_traject_buf_avail

response-body:
{
    "val": 2048,
}
```
</div>

Python 脚本示例

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
        print(f"[错误] {e}")
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