def parse_parts(s):
    exec_type = 'program'
    args = ''
    name = ''
    args = []

    assert s[0].startswith('python'), "input must start with python command"

    i = 0
    while i < len(s):
        if s[i].startswith('python'):
            if s[i+1] == '-m':
                exec_type = 'module'
                name_offset = 2
            else:
                name_offset = 1
            name = s[i+name_offset] 
            i += name_offset + 1

        elif s[i].startswith('--'):

            if not s[i+1].startswith('--'):                
                arg_offset = 1
                arg = f'"{s[i]}", "{s[i+arg_offset]}",'
            else:
                arg_offset = 0
                arg = f'"{s[i]}",'

            args.append(arg)
            i += arg_offset + 1

    return exec_type, name, args
            


             
            # args += f'\n            "{s[i]}", '
            
            # if i+1 < len(s) and not s[i+1].startswith('--'):
            #     args += f'"{s[i+1]}",'

    return name, exec_type, args
    # if not name:
    #     raise ValueError('Input must contain python command')

    # launch_profile = f'''
    # {{
    #     "name": "Python: Debug profile",
    #     "type": "python",
    #     "request": "launch",
    #     "{exec_type}": "{name}",
    #     "console": "integratedTerminal",
    #     "cwd": "${{workspaceFolder}}",
    #     "justMyCode": false,
    #     "args": [{args}
    #     ]
    # }},
    # '''
    # return launch_profile

def split_input(s):
    # can we use a regex instead? 🤔
    parts = []
    quote = ''
    part = ''

    for i in range(len(s)):
        if quote:
            part += s[i]
            if s[i] == quote:
                quote = ''
        elif s[i] in ' =':
            if part:
                parts.append(part)
                part = ''
        else:
            part += s[i] 
            if s[i] in '\'"':
                quote = s[i]

    if part:
        parts.append(part)

    return parts

def build_launch_profile(exec_type, name, args):

    args_str = '\n            '.join(args)

    launch_profile = f'''
    {{
        "name": "Python: Debug profile",
        "type": "python",
        "request": "launch",
        "{exec_type}": "{name}",
        "console": "integratedTerminal",
        "cwd": "${{workspaceFolder}}",
        "justMyCode": false,
        "args": [{args_str}
        ]
    }},
    '''
    return launch_profile



def main():
    import sys

    parts = split_input(sys.argv[1])
    exec_type, name, args = parse_parts(parts)
    print(build_launch_profile(exec_type, name, args))


if __name__ == '__main__':
    main()
