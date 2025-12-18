## CLI 로봇 언어 명령어

### 설명

${cont_model} 제어기 콘솔에서 실행 가능한 로봇언어의 명령어 리스트입니다.

<div style="width: fit-content;">  

|option|description|example|
|:---|:---|:---|
|`reinit`| 로봇언어 재시작 명령을 수행합니다. |rl.reinit|
|`i`|job 파일에 로봇언어 명령문을 삽입(insert)합니다.|rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|`start`|`모터 온` 상태이고 `원격모드` 일때 해당 옵션 수행 시 로봇언어가 실행됩니다.|rl.start|
|`stop`|현재 로봇언어가 실행 중일 때, `외부정지` 진행됩니다.|rl.stop|
|`exit`|현재 실행 중인 로봇언어를 종료합니다.|rl.exit|

</div>