
def parse_input(input_str):
    exec_type = 'program'
    args = ''
    name = ''

    s = input_str.split(' ')

    for i in range(len(s)):
        
        if s[i].startswith('python'):
            if s[i+1] == '-m':
                exec_type = 'module'
                name = s[i+2]
            else:
                name = s[i+1]
                
        elif s[i].startswith('--'):
            args += f'\n            "{s[i]}", '
            
            if not s[i+1].startswith('--'):
                args += f'"{s[i+1]}",'

    if not name:
        raise ValueError('Input must contain python command')

    launch_profile = f'''
    {{
        "name": "Python: Debug profile",
        "type": "python",
        "request": "launch",
        "{exec_type}": "{name}",
        "console": "integratedTerminal",
        "cwd": "${{workspaceFolder}}",
        "justMyCode": false,
        "args": [{args}
        ]
    }},
    '''
    return launch_profile

def main():
    import sys
    print(parse_input(sys.argv[1]))


if __name__ == '__main__':
    main()
