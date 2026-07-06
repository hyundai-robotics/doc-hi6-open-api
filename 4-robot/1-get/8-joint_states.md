#### 4.1.8 `joint_states`

##### Description
- Supported version: `70.00-00` ↑
- `GET`: Retrieves the robot's current joint states.
- Returns **joint angle (position, °), velocity, and torque (effort)** information for each joint.  
  You can query all axes or selectively query a specified range of axes.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

##### query-parameter

* * If no parameters are specified, all joints are queried.
* jno_start (optional)

  * Joint index to start querying from (1-based)
* jno_n (optional)

  * Number of joints to query

##### response

1. status code

   * 200 : OK
   * 400 : Bad Request

     * Query parameter validation failed
   * 403 : Forbidden
   * 404 : Not Found

2. response-body

   * position : Joint angle array (deg)
   * velocity : Joint velocity array
   * effort : Joint torque array (Nm)

        <div style="width: fit-content;">

     ```json
     {
     	"position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
     	"velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     	"effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
     }
     ```

        </div>

##### Usage Example

<div style="max-width: 60vw;">

```python
request url:
GET /project/robot/joint_states?jno_start=1&jno_n=6

response-body:
{
    "position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
    "velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
}
```

Python Script Example

```python
# test.py
import requests

def get_joint_states() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/joints/joint_states"
    query = {"jno_start": 1, "jno_n": 6}

    res = requests.get(url=base_url + path, params=query)

    print(res.json())

    return res


get_joint_states()


```

```sh
$python test.py
{'_type': 'JObject', 'position': [0.949533, 90.949655, 0.949155, 0.948415, -89.050195, 0.948001], 'effort': [0.0, 93.988759, 93.925036, 0.179785, -5.312434, 0.102171], 'velocity': [-0.0, -0.0
, 0.0, 0.0, -0.0, 0.0]}
```

</div>
