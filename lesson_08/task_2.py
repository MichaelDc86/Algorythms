# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter

inp_string = 'Haffman Algorithm'
# inp_string = 'aaaaaafqqwertyuiop'


class HaffmanTree:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def print_tree(self):
        print(f'  {str(self.value)}\n  /\t\\\n{self.left}\t{self.right}')


def haffman(string):

    letter_mult = sorted(Counter(string).items(),  key=lambda pair: pair[1], reverse=False)
    print(f'Исходный отсортированный массив:\n{letter_mult}')
    print(f'Длина исходного отсортированного массива:{len(letter_mult)}')

    def fill_the_tree(array):

        def insert_tree_(arr, vl, tr):
            ins = False
            for j in range(len(arr)):
                if type(arr[j]) == HaffmanTree:
                    if arr[j].value == vl:
                        arr.insert(j, tr)
                        ins = True
                        break
                else:
                    if arr[j][1] == vl:
                        arr.insert(j, tr)
                        ins = True
                        break
            if not ins:
                arr.append(tr)

        def delete_counted_(arr):
            if len(arr) > 2:
                arr.remove(array[0])
                arr.remove(array[0])

        if len(array) == 1:
            return array

        if type(array[0]) == HaffmanTree and type(array[1]) == HaffmanTree:
            val = array[0].value + array[1].value
            lft = array[0]
            rght = array[1]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree_(array, val, tmp_tree)
            delete_counted_(array)

        elif type(array[0]) == HaffmanTree and type(array[1]) == tuple:
            val = array[0].value + array[1][1]
            lft = array[0]
            rght = array[1][0]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree_(array, val, tmp_tree)
            delete_counted_(array)

        elif type(array[0]) == tuple and type(array[1]) == HaffmanTree:
            val = array[0][1] + array[1].value
            lft = array[0][0]
            rght = array[1]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree_(array, val, tmp_tree)
            delete_counted_(array)

        else:
            val = array[0][1] + array[1][1]
            lft = array[0][0]
            rght = array[1][0]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree_(array, val, tmp_tree)
            delete_counted_(array)

        fill_the_tree(array)

        return array[0]

    def print_tree(tr_ee):

        if type(tr_ee.right) == str and type(tr_ee.left) == str:
            print(f'  {tr_ee.value}\n  /\\\n{tr_ee.left}\t{tr_ee.right}')
            return

        if type(tr_ee.right) == HaffmanTree and type(tr_ee.left) == HaffmanTree:
            print_tree(tr_ee.left)
            print_tree(tr_ee.right)

        if type(tr_ee.left) == HaffmanTree and type(tr_ee.right) == str:
            print(f'  {tr_ee.value}\n  /\\\n{tr_ee.left.value}\t{tr_ee.right}')
            return print_tree(tr_ee.left)

        if type(tr_ee.right) == HaffmanTree and type(tr_ee.left) == str:
            print(f'  {tr_ee.value}\n  /\\\n{tr_ee.left}\t{tr_ee.right.value}')
            return print_tree(tr_ee.right)

    def count_letter_from_tree(t_tree):

        if t_tree:

            if type(t_tree) == str or type(t_tree) == list:
                letter_dict[t_tree] = letter_code.copy()
                letter_code.pop()
                return

            if t_tree.left:
                letter_code.append('0')
                count_letter_from_tree(t_tree.left)

            if t_tree.right:
                letter_code.append('1')
                count_letter_from_tree(t_tree.right)
                if letter_code:
                    letter_code.pop()

        return letter_dict

    letter_dict = {}
    letter_code = []
    counted_tree = fill_the_tree(letter_mult)
    # print(counted_tree.right.right.right)
    # print(counted_tree.value)
    # print_tree(counted_tree)
    final_let_dict = count_letter_from_tree(counted_tree)

    print(f'Длина финального массива:\t\t\t\t {len(final_let_dict)}')
    print(f'Финальный массив:\n{final_let_dict}')
    return final_let_dict


def print_result(raw_dict, init_string):
    rez_string = ''
    for i in init_string:
        rez_string += ''.join(raw_dict[i])

    return print(f'Исходная строка:\t\t{init_string}\nЗакодированная строка:\t{rez_string}')


rez = haffman(inp_string)
print_result(rez, inp_string)
