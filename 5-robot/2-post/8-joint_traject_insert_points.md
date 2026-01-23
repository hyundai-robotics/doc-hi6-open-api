## 5.2.8 `joint_traject_insert_points`

### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : Sends a trajectory composed of multiple points to the robot controller.
  - Multiple joint trajectory points are stored in the controller's internal buffer and reflected in the robot's motion.

---

### Caution

1. This API is functional only while the program is in a <u>running state</u>.
   - ex) The API only works when the program is being played back in automatic mode.
   - If the request is made without satisfying this condition, the system will return the error.  
	 "[\[E01554\] Not executable state for external command move](https://hr-alarms.web.app/#/hi6/en/E01554)"

2. The maximum number of trajectory points that can be POSTed at once is **<u>2048</u>**.
   - The buffer for storing trajectory points has a maximum size of **<u>2048</u>**.

3. The requested trajectory points are not discarded until they are reflected in the motion, and the robot continues to move until it reaches the corresponding positions.
   - The trajectory in the buffer remains intact until motion execution, unless it is explicitly cleared by the [joint_traject_init](./7-joint_traject_init.md) api.

4. Depending on the trajectory, an "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/hi6/en/E159)" error may occur. If this error occurs, the robot will stop.

5. This API handles trajectories that consist of **<u>two or more points</u>**.

6. When using additional axes, please pay attention to the **<u>units of the axis coordinate values</u>**.

---

### path-parameter

<div style="width: fit-content;">

```joint_traject_insert_points
POST /project/robot/trajectory/joint_traject_insert_points
```
</div>

### request-body

<div style="width: fit-content;">

- 	|               Key |       Type      | Description                          | Remarks                                           |
	| ----------------: | :-----------: | --------------------------- | -------------------------------------------- |
	|     `joint_names` | array(string) | List of joint names for the trajectory          | e.g., for a 6-axis robot: "j1" to "j6", **order must be exact** |
	|          `points` |     object({})    | List of trajectory points to execute      | 	Keys: "point_n", where n starts from 1. **at least 2 points are required**   |
	|       `positions` | array(double) | Target positions for each joint expressed in radians,<br>for **additional axes, be mindful of the coordinate unit**)| Positions must be specified according to the current number of joints. |
	| `time_from_start` |     number    | Start time of the point (in seconds) | Must be **<u>0.0</u>** or **<u>greater</u>**, and greater than the previous point. |


</div>

- ```
	{
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [0, 1.570796, 0.0, 0.0, 0.0, 0.0],
					"time_from_start": 0.0
			},
			"point_2": {
					"positions": [0.049999, 1.570796, 0.0, 0.0, 0.0, 0.0],
					"time_from_start": 0.4
			}
		}
	}

  ```

### status code

- 200 : Request succeeded
- 403 : Request failed
  - Returned when calling an unsupported API

### error code (response 403)

<div style="width: fit-content;">

- 	| error code     | Error constant name     | Description                                           |
	| ---------- | --------------------------- | ----------------------------------------------------- |
	| `-2`       | `ERR_MISSING_JOINT_NAMES`   | If the joint_names field is missing |
	| `-3`       | `ERR_INVALID_JOINT_NAMES`   | If the joint_name format is invalid (e.g., "x1"), the number of requested joints does not match<br>the robot's current number of joints, or the joint names are in the wrong order.<br>(e.g., ["j1", "j3", "j2", ..., "j6"]) |
	| `-4`       | `ERR_MISSING_POINTS`        | If the points field is missing |
	| `-5`       | `ERR_INVALID_POINTS`        | If the value of points is not an object (i.e., not a Python dictionary), such as an integer or a string |
	| `-6`       | `ERR_TOO_FEW_POINTS`        | If the number of trajectory points is less than 2 |
	| `-7`       | `ERR_TOO_MANY_POINTS`       | If a trajectory is requested with more than the allowed 2048 points |
	| `-8`       | `ERR_POINTS_EXCEED_BUFFER`  | If a trajectory is requested with more points than the currently available buffer space |
	| `-9`      | `ERR_INVALID_POINT_OBJECT`  | If the value of point_n is not an object (i.e., not a Python dictionary, e.g., an integer or a string) |
	| `-10`      | `ERR_MISSING_POSITIONS`     | If the positions field is missing |
	| `-11`      | `ERR_INVALID_POSITIONS`     | If positions is not an array, contains non-numeric values, or its length does not match the number of joints |
	| `-12`      | `ERR_MISSING_TIME`          | If time_from_start field is missing        |
	| `-13`      | `ERR_INVALID_TIME`          | If time_from_start is not a number, is less than 0, or is smaller than the previous value while the robot is in motion |

</div>

### Example

**Ex1. Requesting a trajectory while the robot is at rest**

<img src="../../_assets/09_online_trajectory_insert_points_single.png" style="max-height: 280px;">

1) When requesting a trajectory after the robot has stopped, use the [joint_traject_init](./7-joint_traject_init.md) api to clear the buffer that contains the previous trajectory.
2) Before requesting a trajectory, check whether the program is running and ensure there is available buffer.
3) Request a trajectory consisting of **at least two points**.
   - Set the `position of the starting point` (point_1) to the **current position** of the robot.
   - Set the `time_from_start of the starting point` (point_1) to **0.0**.
   - Subsequent points should be configured with positions and time_from_start values that are reachable from the previous point before being posted.
4) If the robot stops due to an error, restart by initializing with joint_traject_init, then proceed with steps 1 to 3.

<br>

**Ex2. Requesting a trajectory with discontinuous motion (includes stop time between trajectories)**

<img src="../../_assets/10_online_trajectory_insert_points_two.png" style="max-height: 240px;">

1) You must send traj1 and traj2 according to the conditions specified in Example 1.
2) Please note the following:
   - positions of P1 in traj2 must be equal to the positions of Pn in traj1.
   - time_from_start of P1 in traj2 must be 0.0.

<br>

**Ex3. Requesting a trajectory with continuous motion**

<img src="../../_assets/11_online_trajectory_insert_points_continuous.png" style="max-height: 350px;">

1) Send traj1 according to the conditions specified in Example 1.
2) While the robot is moving toward the position of Pn-1, you must send traj2 with attention to the following conditions.
   - Pn of traj1 and P1 of traj2 must be configured so that the robot can move between them smoothly and continuously.
     - The time_from_start of P1 in traj2 must be a cumulative value that is Δ (> 0) greater than the time_from_start of the last point Pn in traj1.
     - The position of P1 in traj2 must be reachable from Pn of traj1 within the time interval Δ.
   - If trajectories that cannot be followed continuously are requested in succession, an "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/hi6/en/E159)" error may occur.

<div style="width: fit-content;">

<br>

#### Python Script Example

- Move the robot to its default pose (based on a 6-axis configuration, [0, 90, 0, 0, 0, 0])
- Create and `play` the following 0001.job in `automatic mode` to enter the program play state.
- 0001.job
	```job
	Hyundai Robot Job File; { version: 1.6, mech_type: "-1()", total_axis: -1, aux_axis: -1 }
	  > wait di1
		end
	```
- Run the test script (Example 3: Requesting two trajectories in continuous motion)

	```
	Condition 1)
	The `time_from_start` of `point_1` in `traj_2` must be a cumulative value that is Δ (> 0) greater than `point_2` in `traj_1`.

	Condition 2)
	The `positions` of `point_1` in `traj_2` must be reachable from `point_2` in `traj_1` within the time interval Δ.

	```

	```python
	import requests
	import time
	import math

	session = requests.Session()


	traj_2 = {
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [
						math.radians(2.89),
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 5.0,
			},
			"point_2": {
					"positions": [
						0,
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 7,
			},
		},
	}

	traj_1 = {
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [
						0,
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 0.0,
			},
			"point_2": {
					"positions": [
						math.radians(2.86),
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [
						math.radians(5.73),
						0.0,
						0.0,
						0.0,
						0.0,
						0.0,
					],
					"accelerations": [0.0] * 6,
					"time_from_start": 3.0,
			},
		},
	}

	post_cnt = 0


	def is_prog_running(base_url: str) -> bool:
		uri = f"{base_url}/project/rgen"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.get(url=uri, headers=headers)
			return ret.json()["is_playback"]
		except Exception as e:
			print(f"Error in is_prog_running")
			return None


	def get_jt_buff_avail_num(base_url) -> int:
		uri = f"{base_url}/project/robot/trajectory/joint_traject_buf_avail"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.get(url=uri, headers=headers)
			return ret.json()["val"]
		except Exception as e:
			print(f"Error in get_jt_buff_avail_num: {e}")
			return None


	def post_trajectories(base_url: str, trajects: dict):
		global post_cnt
		uri = f"{base_url}/project/robot/trajectory/joint_traject_insert_points"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		if is_prog_running(base_url) == False:
			print("Program is not running!")
			return None

		n_jt_buff_avail = get_jt_buff_avail_num(base_url)
		if n_jt_buff_avail <= 0:
			print("Current joint trajectory buffer is full.")
			return None

		try:
			start = time.time()
			ret = session.post(url=uri, headers=headers, json=trajects)
			end = time.time()
			elapsed_ms = (end - start) * 1000

			print(
					f"[{post_cnt}] elapsed_ms: {elapsed_ms:.3f} ms. available jt buff: {n_jt_buff_avail - 1}/2048"
			)
			post_cnt += 1

			print(ret, ret.json())

			ret.raise_for_status()
			return ret
		except Exception as e:
			print(f"Error in post_trajectories: {e}")
			return None


	def post_init_trajectories(base_url: str):
		uri = f"{base_url}/project/robot/trajectory/joint_traject_init"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.post(url=uri, headers=headers)
			ret.raise_for_status()
			return ret
		except Exception as e:
			print(f"Error in post_init_trajectories: {e}")
			return None


	if __name__ == "__main__":
		base_url = f"http://192.168.1.150:8888"

		while True:
			# Initialize the buffer when requesting a trajectory from a stopped state
			post_init_trajectories(base_url)

			# Post trajectories consecutively
			ret = post_trajectories(base_url, trajectories_go)
			time.sleep(1)
			ret = post_trajectories(base_url, trajectories_back)
			time.sleep(8)

	```

- ```sh
		$python test.py
		[0] elapsed_ms: 6.122 ms. available jt buff: 2047/2048
		<Response [200]> {'_type': 'JObject'}
		[1] elapsed_ms: 3.997 ms. available jt buff: 2046/2048
		<Response [200]> {'_type': 'JObject'}
		...
	```


</div>


