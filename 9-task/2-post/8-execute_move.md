#### 9.2.8 `execute_move`

##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : Moves to the specified pose.

{% hint style="warning" %}
HRSpace users only<br>
execute_move may fail due to a Remote Mode validation error on VRC_Hi6 v60.30-10 to v60.32-06<br>
→ Use v60.30-09 or earlier, or v60.32-07 or later (Physical Hi6 controllers are not affected)
{% endhint %}

##### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### request-body
- `stmt` : Key value in the request body, referring to the statement.
- For details on how to write move statements, please refer to [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/en/5-moving-robot/4-move?cont_model=${cont_model}).

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

##### response

1. status code
- 200 : OK
- 400 : Bad Request
    - The request body failed validation.
- 403 : Forbidden
    - An API request was attempted while not in Remote Mode (effective from v60.30-07).
- 404 : Not Found

2. response-body

- Normal response for v60.30 or earlier

```json
{ "err_code" : 0 }
```

- Normal response for v60.32 or later

```json
{ "_type" : "JObject" }
```

3. error code

- -38500 : API request attempted while not in Remote Mode
- -1442071 : API request attempted while the motor is OFF
- -1442080 : API request attempted during automatic program execution
- -1376272 : Robot language syntax error occurred while processing the API request

Python Script Example
- Input pose command when the motor is on and matches the current robot axes.

```python
# test.py
import requests
import time


def post_execute_move(in_pose: str) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


poses = ["[-10, 90, -10, 0, 0, 0]", "[-5, 90, 5, 0, 0, 0]", "[0, 90, 0, 0, 0, 0]"]

for idx, pose in enumerate(poses):
    res = post_execute_move(pose)
    print((res.status_code, res.json()))

    if idx < len(poses) - 1:
        time.sleep(1.5)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```
