# 3. control

- 제어기(controller)의 설정값 적용 및 입출력 값을 처리합니다.
- `control` 의 path parameter 는 `/project/control/{command}` 입니다.
- `{command}` 리스트는 아래와 같습니다.

<br>



<blockquote>

| command | API method | description |
|:----|:----:|:----|
| op_cnd | [`get`](/3-control/1-get/1-op_cnd.md) , [`post`](/3-control/2-post/1-op_cnd.md) | 로봇 구동 상태 정보 반환 및 변경 |
| ios/dio/{dio_val} | [`get`](/3-control/1-get/2-ios-dio.md) | 제어기의 디지털 입출력값 반환 |
| ios/dio/do_val | [`post`](/3-control/2-post/2-ios-dio.md) | 제어기의 디지털 출력값 변경 |
| ios/sio/{sio_val} | [`get`](/3-control/1-get/3-ios-sio.md) | 제어기의 시스템 입출력값 반환 |

</blockquote>
