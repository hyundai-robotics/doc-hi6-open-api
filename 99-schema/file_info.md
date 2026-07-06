### `file_info`

#### 描述

此参数在请求文件信息时返回。

|key|type|description|
|:---:|:---|:---|
|fname|`str`|文件名|
|size|`int`|文件大小(B, Byte)|
|year|`int`|文件修改的 `年份` |
|month|`int`|文件修改的 `月份` |
|mday|`int`|文件修改的 `日期` |
|wday|`int`|文件修改的 `星期几` (0: 周日, 1: 周一, 2: 周二, ...) |
|hour|`int`|文件修改的 `小时 (hour)` |
|min|`int`|文件修改的 `分钟` |
|sec|`int`|文件修改的 `秒` |
|is_dir|`bool`|检查当前文件是否为目录 |
|readonly|`bool`|检查文件是否为只读 |