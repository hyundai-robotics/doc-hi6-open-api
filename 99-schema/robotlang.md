### CLI Robot Language Commands

#### Description

This is a list of robot language commands that can be executed from the ${cont_model} controller console.  

|option|description|example|
|:---|:---|:---|
|`reinit`| Executes the robot language restart command. |rl.reinit|
|`i`| Inserts robot language commands into the job file. |rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|`start`|Executes the robot language when the `motor is on` and in `remote mode`.|rl.start|
|`stop`|Performs `external stop` when the robot language is currently running.|rl.stop|
|`exit`|Terminates the currently running robot language.|rl.exit|
