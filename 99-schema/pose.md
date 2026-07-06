### `姿势 (Pose)`

#### Description

姿势数据。

|key|description|
|:---|:---|
|x|X 位置 (mm)|
|y|Y 位置 (mm)|
|z|Z 位置 (mm)|
|rx|RX 角度 (deg.)|
|ry|RY 角度 (deg.)|
|rz|RZ 角度 (deg.)|
|j1~j16|1~16 轴值(mm 或 deg.)|
|crd|[坐标系统](./crdsys.md)|
|mechinfo|[机制信息](./mechinfo.md)|
|nsync|传感器同步值数量 (0~2)|
|sync|传感器同步值 (字符串). 例如 `"sync(220.5,195.3)"`|