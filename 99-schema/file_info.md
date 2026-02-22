### `file_info`

#### 描述

请求文件信息时返回此参数。

|key|type|描述|
|:---:|:---|:---|
|fname|`str`|文件名|
|size|`int`|文件大小(B, Byte)|
|year|`int`|`文件修改年份`|
|month|`int`|`文件修改月份`|
|mday|`int`|`文件修改日期`|
|wday|`int`|`文件修改的星期几` (0: 日, 1: 一, 2: 二, ...) |
|hour|`int`|`文件修改的小时`|
|min|`int`|`文件修改的分钟`|
|sec|`int`|`文件修改的秒数`|
|is_dir|`bool`|检查当前文件是否为目录|
|readonly|`bool`|检查该文件是否为只读|