from vsdebug import parse_parts, split_input


class Test_split_input:

    def test_simple(self):
        input_str = "--a=1 --b 2"
        ref = ["--a", "1", "--b", "2"]
        result = split_input(input_str)
        assert ref == result

    def test_double(self):
        input_str = "--a==1  --b 2"
        ref = ["--a", "1", "--b", "2"]
        result = split_input(input_str)
        assert ref == result

    def test_literal(self):
        input_str = "--a='=' --b 2"
        ref = ["--a", "'='", "--b", "2"]
        result = split_input(input_str)
        assert ref == result

    def test_bracket(self):
        input_str = '--a=$(a b = )'
        ref = ["--a", "$(a b = )"]
        result = split_input(input_str)
        assert ref == result

class Test_parse_parts:

    def test_program(self):
        parts = ["python3", "code.py", "--param1", "1", "--param2", "--param3", "3"]
        ref = ("program", "code.py", ['"--param1", "1",', '"--param2",', '"--param3", "3",'])
        result = parse_parts(parts)
        assert ref == result


    def test_module(self):
        parts = ["python3", "-m", "package.code", "--param1", "1", "--param2", "--param3", "3"]
        ref = ("module", "package.code", ['"--param1", "1",', '"--param2",', '"--param3", "3",'])
        result = parse_parts(parts)
        assert ref == result

    def test_final_single(self):
        parts = ['python3', 'code.py', '--param1']
        ref = ("program", "code.py", ['"--param1",'])
        result = parse_parts(parts)
        assert ref == result