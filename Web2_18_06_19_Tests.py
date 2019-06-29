# from datetime import
from time import sleep


class BuildingStack:
    def __init__(self):
        self.order = list()

    def pop(self):
        self.order.pop()

    def push(self, value):
        if isinstance(value, str):
            raise ValueError

        self.order.append(value)

    @property
    def head(self):
        try:
            return self.order[-1]
        except IndexError:
            return None
    def __repr__(self):
        return ', '.join(map(str, self.order))

def sort_builds(_list, res_stack):
    for item_value in _list:
        if res_stack.head and res_stack.head <= item_value:
            res_stack.pop()
        res_stack.push(item_value)


if '__main__' == __name__:
    exaple_list = [
        [],
        [1, 1, 1],
        [4, 2, 3, 2, 1],
        [4, 2, 2, 3, 2, 1],
    ]
    for example_item in exaple_list:
        result = BuildingStack()
        sort_builds(example_item,result)
        print(f'{example_item} => {result}')
