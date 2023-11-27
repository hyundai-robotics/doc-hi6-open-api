# file_info

## 설명

파일 정보 요청 시 반환되는 파라미터 입니다.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|파일 이름|
|size|`int`|파일 크기(B, Byte)|
|year|`int`| 파일이 수정된 `년` |
|month|`int`| 파일이 수정된 `월` |
|mday|`int`| 파일이 수정된 `일` |
|wday|`int`| 파일이 수정된 `요일` (0:일, 1:월, 2:화, ...) |
|hour|`int`| 파일이 수정된 `시` |
|min|`int`| 파일이 수정된 `분` |
|sec|`int`| 파일이 수정된 `초` |
|is_dir|`bool`| 현재 파일이 디렉토리인지 확인 |
|readonly|`bool`| 읽기 전용 파일 여부 확인 |
