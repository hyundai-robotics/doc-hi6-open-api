## cur_prog_cnt

### Description
Sets the current program counter for the task.

### request body
|key|type|description|
|:---|:---|:---|
|`pno`|int|Program number (if -1, keep current number)|
|`sno`|int|Step number (if -1, keep current number)|
|`fno`|int|Function number (if -1, keep current number)|
|`ext_sel`|int|`0` : Internal selection (prohibited in remote mode) <br> `1` : External selection (only allowed in remote mode)|

### response body
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|Newly moved step number|
|`fno_new`|int|Newly moved function number|
|`ln_new`|int|Newly moved line number (program header is 0, first statement is 1)|