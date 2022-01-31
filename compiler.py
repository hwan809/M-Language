import sys

TYPE_IF = 'IF'
TYPE_DEF = 'DEF'
TYPE_CALL = 'CALL'
TYPE_INPUT = 'INPUT'
TYPE_PRINT = 'PRINT'
TYPE_PRINT_ASCII = 'PRINT_ASCII'
TYPE_GOTO = 'GOTO'
TYPE_END = 'END'
TYPE_BLANK = 'BLANK'

class LanguageM:
    def __init__(self):
        self.index = 0
        self.data = [0] * 256

    def get_int(self, code):
        plus = code.count('.')
        minus = code.count('-')

        code = code.replace('.', '')
        code = code.replace(',', '')

        if not code.empty():
            raise SyntaxError(f'index {self.index + 2}, 이게 어떻게 정수냐?')

        return plus - minus

    def get_number(self, code):
        output = 0
        now_add = True

        while len(code) != 0:
            if code.startswith('엉?'):
                if now_add:
                    output += int(input())
                else:
                    output *= int(input())
                    now_add = True

                code = code.split('?', maxsplit=1)[1]
            elif code.startswith('빅'):
                if now_add:
                    output += self.data[0]
                else:
                    output *= self.data[0]
                    now_add = True

                code = code[1:]
            elif code.startswith('비'):
                now_call = code.split('익')[0] + '익'

                now_num = self.get_variable(now_call)
                if now_add:
                    output += now_num
                else:
                    output *= now_num
                    now_add = True

                #print(code)
                code = code[len(now_call):]
            elif code.startswith('.') or code.startswith(','):
                now_char = code[0]
                now_num = 0

                while now_char == '.' or now_char == ',':
                    if not code:
                        break

                    now_char = code[0]

                    if now_char == '.':
                        now_num += 1
                    elif now_char == ',':
                        now_num -= 1
                    else:
                        break

                    code = code[1:]

                if now_add:
                    output += now_num
                else:
                    output *= now_num
                    now_add = True
            elif code.startswith(' '):
                now_add = False
                code = code[1:]

        return output

    def get_variable(self, code):
        index = -1

        if code == '빅':
            index = 0
        elif code == '비익':
            index = 1

        else:
            if code[0] == '비' \
                    and code[-1] == '익':
                for char in code[1:-1]:
                    if char != '이':
                        raise SyntaxError(f'index {self.index + 2}, 어떻게 ' + code + '가 변수 호출이냐?')

                index = len(code) - 1
            else:
                raise SyntaxError(f'index {self.index + 2}, 어떻게 이게 변수 호출이냐?')

        return self.data[index]

    def variable_index_to_number(self, code):
        if code == '롱':
            return 0
        elif code == '뽈롱':
            return 1
        elif code == '뽀올롱':
            return 2
        else:
            if code[0] == '뽀' \
                    and code[-2] == '올' \
                    and code[-1] == '롱':

                for char in code[1:-2]:
                    if char != '오':
                        raise SyntaxError(f'index {self.index + 2}, 어떻게 ' + code + '이 변수 인덱스냐?')

                return len(code) - 1

            else:
                raise SyntaxError(f'index {self.index + 2}, 어떻게 이게 변수 인덱스냐')

    @staticmethod
    def get_type(self, code):
        if not code:
            return TYPE_BLANK
        elif code.startswith('이민수'):
            return TYPE_IF
        elif code.startswith('마'):
            return TYPE_DEF
        elif code.startswith('엉!'):
            return TYPE_PRINT
        elif code.startswith('무빙'):
            return TYPE_GOTO
        elif code.startswith('훌륭'):
            return TYPE_PRINT_ASCII
        elif code.startswith('고소'):
            return TYPE_END
        else:
            raise SyntaxError('이게 어떻게 마랭이냐..')

    def compileLine(self, code):
        if code == '':
            return None

        TYPE = self.get_type(self, code)

        if TYPE == TYPE_BLANK:
            return

        if TYPE == TYPE_DEF:
            index, number = code[1:].split('롱', maxsplit=1)
            index += '롱'

            index_num = self.variable_index_to_number(index)

            number_int = self.get_number(number)

            self.data[index_num] = number_int

            #print('data added in index ' + str(index_num) + '. value : ' + str(number_int))
        elif TYPE == TYPE_PRINT:
            number = code[2:]

            if not number:
                print('\n', end='')
            else:
                number_int = self.get_number(number)
                print(number_int, end='')
        elif TYPE == TYPE_PRINT_ASCII:
            number = code[2:]
            number_int = self.get_number(number)
            number_ascii = chr(number_int)

            print(number_ascii, end='')
        elif TYPE == TYPE_END:
            number = code[2:]

            if number == '이민수':
                print('150000', end='')
            else:
                number_int = self.get_number(number)

                print(number_int, end='')
                sys.exit()
        elif TYPE == TYPE_IF:
            command = code[3:] #이민수 후.

            check_val, wish = command.split('ㅋ', maxsplit=1)
            check_val_int = self.get_number(check_val)

            if check_val_int == 0:
                return wish
        elif TYPE == TYPE_GOTO:
            number = code[2:]
            number_int = self.get_number(number)

            return number_int - 2

    def compile(self, code):
        self.index = 0

        if code[0] != '마임 엉덩이 뽈록' or code[-1] != '마이 엉덩이는 뽈록이냐 ㄹㅇ':
            raise SyntaxError('어떻게 마이 엉덩이가 뽈록이 아니냐 ㄹㅇ')

        del code[0]
        del code[-1]

        now_moving = False

        while self.index < len(code):
            #print(f'compiling line {self.index + 2}... {code[self.index]}')

            goto = self.compileLine(code[self.index])

            self.index += 1

            if isinstance(goto, int):
                if now_moving:
                    now_moving = False
                    del code[self.index - 1]
                    #print(f'moving to, {code[self.index]}')

                self.index = goto
            elif isinstance(goto, str):
                code.insert(self.index, goto)
                now_moving = True
                #print(now_moving)

    def compile_file(self, path):
        with open(path, encoding='utf-8-sig') as mxb_file:
            code = mxb_file.read().splitlines()
            self.compile(code)

if __name__ == '__main__':
    compiler = LanguageM()

    compiler.compile_file('E:/workspaces/python_workspace/python_/m_language/gugudan.mxb')
