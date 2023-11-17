# 4. robot

- 로봇 관련 기능과 로봇 파라미터를 처리합니다.
- `robot` 의 path parameter 는 `/project/robot/{command}` 입니다.
- `{command}` 리스트는 아래와 같습니다.

<br>


<blockquote>

| command | API method | description |
|:----|:----:|:----|
|motor_on_state|[`get`](/4-robot/1-robot-get/1-motor_on_state.md)|모터 온 상태 반환|
|po_cur|[`get`](/4-robot/1-robot-get/2-po_cur.md)|현재 로봇의 자세 반환|
|cur_tool_data|[`get`](/4-robot/1-robot-get/3-cur_tool_data.md)|현재 툴 정보 반환|
|tools|[`get`](/4-robot/1-robot-get/4-tools.md)|툴 정보 반환|
|motor_on|[`post`](/4-robot/2-robot-post/1-motor-on-off.md)|모터 온 설정|
|motor_off|[`post`](/4-robot/2-robot-post/1-motor-on-off.md)|모터 오프 설정|
|start|[`post`](/4-robot/1-robot-get/3-cur_tool_data.md)|로봇 기동 설정|
|stop|[`post`](/4-robot/1-robot-get/4-tools.md)|로봇 정지 설정|
|tool_no|[`post`](/4-robot/3-robot-tools-get/1-t.md)|선택할 툴 번호 선택|
|crd_sys|[`post`](/4-robot/2-robot-post/4-crd_sys.md)|조그 좌표계 선택|

</blockquote>