#### 5.2.8 `joint_traject_insert_points`

##### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : 发送由多个点组成的轨迹到机器人控制器。
  - 多个关节轨迹点存储在控制器的内部缓冲区，并反映在机器人的运动中。

---

##### Caution

1. 此 API 仅在程序处于 <u>运行状态</u> 时功能正常。
   - 例如) 此 API 只有在程序以自动模式播放时才有效。
   - 如果未满足此条件而提出请求，系统将返回错误。  
	 "[\[E01554\] Not executable state for external command move](https://hr-alarms.web.app/#/${cont_model}/zh/E01554)"

2. 可以一次 POST 的最大轨迹点数是 **<u>2048</u>**。
   - 用于存储轨迹点的缓冲区最大大小为 **<u>2048</u>**。

3. 请求的轨迹点在反映在运动之前不会被丢弃，机器人将继续移动，直到到达相应的位置。
   - 缓冲区中的轨迹在运动执行之前保持不变，除非通过 [joint_traject_init](./7-joint_traject_init.md) api 明确清除。

4. 根据轨迹，可能会发生 "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/${cont_model}/zh/E159)" 错误。如果发生此错误，机器人将停止。

5. 此 API 处理由 **<u>两个或更多点</u>** 组成的轨迹。

6. 使用额外轴时，请注意 **<u>轴坐标值的单位</u>**。

---

##### path-parameter

<div style="width: fit-content;">

```joint_traject_insert_points
POST /project/robot/trajectory/joint_traject_insert_points
```
</div>

##### request-body

<div style="width: fit-content;">

- 	|               Key |       Type      | Description                          | Remarks                                           |
	| ----------------: | :-----------: | --------------------------- | -------------------------------------------- |
	|     `joint_names` | array(string) | 轨迹的关节名称列表          | 例如，对于一个 6 轴机器人: "j1" 到 "j6"， **顺序必须精确** |
	|          `points` |     object({})    | 要执行的轨迹点列表      | 	键: "point_n"，n 从 1 开始。 **至少需要 2 个点**   |
	|       `positions` | array(double) | 每个关节的目标位置，以弧度表示，<br>对于 **额外轴，请注意坐标单位**)| 位置必须根据当前关节数指定。 |
	| `time_from_start` |     number    | 点的起始时间（单位：秒） | 必须是 **<u>0.0</u>** 或 **<u>更大</u>**，并且大于上一个点。 |


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

##### status code

- 200 : 请求成功
- 403 : 请求失败
  - 当调用不支持的 API 时返回

##### error code (response 403)

<div style="width: fit-content;">

- 	| error code     | Error constant name     | Description                                           |
	| ---------- | --------------------------- | ----------------------------------------------------- |
	| `-2`       | `ERR_MISSING_JOINT_NAMES`   | 如果缺少 joint_names 字段 |
	| `-3`       | `ERR_INVALID_JOINT_NAMES`   | 如果 joint_name 格式无效（例如，"x1"），请求的关节数量与<br>机器人的当前关节数量不匹配，或关节名称顺序错误。<br>（例如，["j1", "j3", "j2", ..., "j6"]） |
	| `-4`       | `ERR_MISSING_POINTS`        | 如果缺少 points 字段 |
	| `-5`       | `ERR_INVALID_POINTS`        | 如果 points 的值不是一个对象（即不是 Python 字典），例如整数或字符串 |
	| `-6`       | `ERR_TOO_FEW_POINTS`        | 如果轨迹点数少于 2 |
	| `-7`       | `ERR_TOO_MANY_POINTS`       | 如果请求的轨迹点数超过允许的 2048 |
	| `-8`       | `ERR_POINTS_EXCEED_BUFFER`  | 如果请求的轨迹点数超过当前可用缓冲区空间 |
	| `-9`      | `ERR_INVALID_POINT_OBJECT`  | 如果 point_n 的值不是一个对象（即不是 Python 字典，例如整数或字符串） |
	| `-10`      | `ERR_MISSING_POSITIONS`     | 如果缺少 positions 字段 |
	| `-11`      | `ERR_INVALID_POSITIONS`     | 如果 positions 不是数组，包含非数字值，或其长度与关节数量不匹配 |
	| `-12`      | `ERR_MISSING_TIME`          | 如果缺少 time_from_start 字段        |
	| `-13`      | `ERR_INVALID_TIME`          | 如果 time_from_start 不是数字，小于 0，或在机器人运动时小于前一个值 |

</div>

##### Example

**Ex1. 当机器人处于静止状态时请求轨迹**

<img src="../../_assets/09_online_trajectory_insert_points_single.png" style="max-height: 280px;">

1) 当在机器人停止后请求轨迹时，使用 [joint_traject_init](./7-joint_traject_init.md) api 清除包含先前轨迹的缓冲区。
2) 在请求轨迹之前，检查程序是否在运行，并确保有可用的缓冲区。
3) 请求由 **至少两个点** 组成的轨迹。
   - 将 `起始点的位置信息`（point_1）设置为机器人的 **当前位置**。
   - 将 `起始点的 time_from_start`（point_1）设置为 **0.0**。
   - 后续点应配置以使 `positions` 和 `time_from_start` 值可从前一个点到达，然后再发布。
4) 如果由于错误导致机器人停止，请通过 joint_traject_init 初始化后重新启动，然后按步骤 1 到 3 进行操作。

<br>

**Ex2. 请求具有不连续运动的轨迹（轨迹之间包含停顿时间）**

<img src="../../_assets/10_online_trajectory_insert_points_two.png" style="max-height: 240px;">

1) 必须按照示例 1 中规定的条件发送 traj1 和 traj2。
2) 请注意以下事项：
   - traj2 中的 P1 的位置必须等于 traj1 中的 Pn 的位置。
   - traj2 中的 P1 的 time_from_start 必须为 0.0。

<br>

**Ex3. 请求具有连续运动的轨迹**

<img src="../../_assets/11_online_trajectory_insert_points_continuous.png" style="max-height: 350px;">

1) 根据示例 1 中规定的条件发送 traj1。
2) 当机器人朝 Pn-1 的位置移动时，必须发送 traj2，并注意以下条件。
   - traj1 的 Pn 和 traj2 的 P1 必须配置以使机器人能够平滑和连续地在它们之间移动。
     - traj2 中 P1 的 time_from_start 必须是一个累计值，且 Δ (> 0) 大于 traj1 中最后一个点 Pn 的 time_from_start。
     - traj2 中 P1 的位置必须在时间间隔 Δ 内可以从 traj1 的 Pn 到达。
   - 如果连续请求无法平滑跟随的轨迹，则可能会发生 "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/${cont_model}/zh/E159)" 错误。

<div style="width: fit-content;">

<br>

##### Python Script Example

- 将机器人移动到其默认姿势（基于 6 轴配置，[0, 90, 0, 0, 0, 0]）
- 创建并 `播放` 下面的 0001.job 以进入程序播放状态。
- 0001.job
	```job
	Hyundai Robot Job File; { version: 1.6, mech_type: "-1()", total_axis: -1, aux_axis: -1 }
	  > wait di1
		end
	```
- 运行测试脚本（示例 3：请求两个连续运动的轨迹）

	```
	条件1)
	`traj_2` 中 `point_1` 的 `time_from_start` 必须是一个累计值，且 Δ (> 0) 大于 `traj_1` 中 `point_2` 的值。

	条件2)
	`traj_2` 中 `point_1` 的 `positions` 必须在时间间隔 Δ 内可以从 `traj_1` 中的 `point_2` 到达。

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
			print("程序未在运行中！")
			return None

		n_jt_buff_avail = get_jt_buff_avail_num(base_url)
		if n_jt_buff_avail <= 0:
			print("当前关节轨迹缓冲区已满。")
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
			# 在从静止状态请求轨迹时初始化缓冲区
			post_init_trajectories(base_url)

			# 连续发布轨迹
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