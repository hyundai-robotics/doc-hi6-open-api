# file_info

## Description

This parameter is returned when requesting file information.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|file name|
|size|`int`|file size(B, Byte)|
|year|`int`| `year` the file was modified |
|month|`int`| `month` the file was modified` |
|mday|`int`| `day` the file was modified |
|wday|`int`| `Day of the week` on which the file was modified (0: Sun, 1: Mon, 2: Tue, ...) |
|hour|`int`| `hour` the file was modified |
|min|`int`| `minute` the file was modified |
|sec|`int`| `second` the file was modified |
|is_dir|`bool`| Check if current file is a directory |
|readonly|`bool`| Check if the file is read-only |
