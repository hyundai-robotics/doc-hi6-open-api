## CLI 로봇언어 함수

### 설명

Hi6 제어기 콘솔에서 실행 가능한 로봇언어의 옵션들 입니다.

|option|description|example|
|:---|:---|:---|
|`reinit`| 로봇언어 재시작 명령을 수행하는 옵션입니다. |rl.reinit|
|`i`|job 파일에 로봇언어 명령문을 삽입(insert)하는 옵션입니다.|rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|`start`|`모터 온` 상태이고 `원격모드` 일때 해당 옵션 수행 시 로봇언어가 실행됨|rl.start|
|`stop`|현재 로봇언어가 실행 중일 때, `외부정지` 진행|rl.stop|
|`exit`|현재 실행 중인 로봇언어를 종료함|rl.exit|