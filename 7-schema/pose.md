# Pose

## 설명

포즈(pose) 데이터입니다.

- x : X위치 (mm)
- y : Y위치 (mm)
- z : Z위치 (mm)
- rx : RX각도 (deg.)
- ry : RY각도 (deg.)
- rz : RZ각도 (deg.)
- j1~j16 : 1~16축 값 (mm or deg.)

- crd : [좌표계](crdsys.md)
- mechinfo : [메커니즘정보](mechinfo.md)
- nsync : 센서동기 값의 개수 (0~2)
- sync : 센서동기 값 (문자열). e.g. `"sync(220.5,195.3)"`
