class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        '''Проверка стека на пустоту. Метод возвращает True если не пустой и False если пустой '''
        if len(self.stack) > 0 :
            return True
        else:
            return False
        
    def push(self, item):
        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.stack.append(item)

    def pop(self):
        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        self.stack.pop()
        return element

    def peek(self):
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element

    def size(self):
        '''Возвращает количество элементов в стеке.'''
        return len(self.stack)
    
    def check_ballance(self,myStr):
        '''Метод на проверку сбалансированости скобок в строеке.'''
        stack = Stack()
        open_list = ["[","{","("]
        close_list = ["]","}",")"]

        if myStr[0] in close_list:
            return "Несбалансированно"
        for item in myStr:
            if item in open_list:
                stack.push(item)
            elif item in close_list:
                index_open = open_list.index(stack.peek())
                index_close = close_list.index(item)
                if index_close == index_open :
                    stack.pop()
                else:
                    return "Несбалансированно"
        if stack.size() == 0 :
            return "Сбалансированно"
        else:
            return "Несбалансированно"


def test_check_ballance(string, expected):
    """"Тест проверяет работу метода check_ballance."""
    s = Stack()
    result = s.check_ballance(string)
    try:
        assert result == expected
        print (f'Тест функции успешен. Строка примера {string}')
    except AssertionError:
        print(f'Тест не пройден на примере {string}')


if __name__ == '__main__':

    test_check_ballance('(((([{}]))))', "Сбалансированно")
    test_check_ballance('[([])((([[[]]])))]{()}', "Сбалансированно")
    test_check_ballance('{{[()]}}', "Сбалансированно")
    test_check_ballance('}{}', "Несбалансированно")
    test_check_ballance('{{[(])]}}', "Несбалансированно")
    test_check_ballance('[[{())}]', "Несбалансированно")