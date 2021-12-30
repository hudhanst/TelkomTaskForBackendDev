## About
This repository is for work entry selection by backend devloper by telkom
## How To Use
- git clone
- make sure python installed (created on v3.7.4)
- run cmd on currently path
- type "python TelkomCLI.py {Arg}"
## Args
This CLI created base on the task given so the syntx almost the same, for more detail:
- help: help or -h
- Transpose : "{filePath} -t {json/txt/None}"
example: "D:\Users\MyPc\Documents\test.log" -t json
- Output: "{filePath} -o {OutputPath}" OR "{filePath} -t {json/txt/None} -o {OutputPath}"
example:
"D:\Users\MyPc\Documents\test.log" -t json -o "D:\Users\MyPc\Documents\test.json"