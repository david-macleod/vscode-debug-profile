# vscode-debug-profile
Convert command line args to vscode debugger launch profile

**Install**
`pip install git+https://github.com/david-macleod/vscode-debug-profile`

**Run**
`vsdebug 'python myfile.py --arg1 val --arg2 --arg3 val2'`
```
    {
        "name": "Python: Debug profile",
        "type": "python",
        "request": "launch",
        "program": "myfile.py",
        "console": "integratedTerminal",
        "cwd": "${workspaceFolder}",
        "justMyCode": false,
        "args": [
            "--arg1", "val",
            "--arg2",
            "--arg3", "val2",
        ]
    },
```
