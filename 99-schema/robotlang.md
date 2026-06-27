### CLI Robot Language Commands

#### Description

这是可以从 ${cont_model} 控制器控制台执行的机器人语言命令列表。  

|option|description|example|
|:---|:---|:---|
|`reinit`| 执行机器人语言重启命令。 |rl.reinit|
|` (i)`| 将机器人语言命令插入到作业文件中。 |rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|` (start)`| 当`电机开启`且处于`远程模式`时执行机器人语言。|rl.start|
|` (stop)`| 当机器人语言正在运行时执行`外部停止`。|rl.stop|
|`exit`| 终止当前正在运行的机器人语言。|rl.exit|