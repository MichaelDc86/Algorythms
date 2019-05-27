# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter

inp_string = 'Haffman Algorithm'


class HaffmanTree:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def haffman(string):

    letter_mult = sorted(Counter(string).items(),  key=lambda pair: pair[1], reverse=False)
    print(letter_mult)
    print(len(letter_mult))

    def fill_the_tree(array):

        def insert_tree(arr, vl, tr):
            ins = False
            for j in range(len(arr)):
                if type(arr[j]) == HaffmanTree:
                    if arr[j].value <= vl:
                        arr.insert(j - 1, tr)
                        ins = True
                        break
                else:
                    if arr[j][1] <= vl:
                        arr.insert(j - 1, tr)
                        ins = True
                        break
            if not ins:
                arr.append(tr)

        def delete_counted(arr):
            if len(arr) > 2:
                arr.remove(array[0])
                arr.remove(array[1])

        if len(array) == 1:
            return array

        if type(array[0]) == HaffmanTree and type(array[1]) == HaffmanTree:
            val = array[0].value + array[1].value
            lft = array[0]
            rght = array[1]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree(array, val, tmp_tree)
            delete_counted(array)

        elif type(array[0]) == HaffmanTree and type(array[1]) == tuple:
            val = array[0].value + array[1][1]
            lft = array[0]
            rght = array[1][0]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree(array, val, tmp_tree)
            delete_counted(array)

        elif type(array[0]) == tuple and type(array[1]) == HaffmanTree:
            val = array[0][1] + array[1].value
            lft = array[0][0]
            rght = array[1]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree(array, val, tmp_tree)
            delete_counted(array)

        else:
            val = array[0][1] + array[1][1]
            lft = array[0][0]
            rght = array[1][0]
            tmp_tree = HaffmanTree(val, lft, rght)
            insert_tree(array, val, tmp_tree)
            delete_counted(array)

        fill_the_tree(array)

        return array[0]

    # fill_the_tree(letter_mult)
    # print(array)

    # return fill_the_tree(letter_mult).left.left.left
    # return fill_the_tree(letter_mult)[0].value
    # return fill_the_tree(letter_mult)[0].left.right.left.left
    # return fill_the_tree(letter_mult)[0].right

    # def count_letter_from_tree(t_tree):
    #
    #     if t_tree:
    #
    #         if type(t_tree) == str:
    #             letter_dict[t_tree] = letter_code.copy()
    #             # t_tree = None
    #             letter_code.pop()
    #             return  # t_tree
    #
    #         if t_tree.left:
    #             letter_code.append('0')
    #             count_letter_from_tree(t_tree.left)
    #
    #         if t_tree.right:
    #             letter_code.append('1')
    #             count_letter_from_tree(t_tree.right)
    #
    #     return letter_dict  # , t_tree

    def go_tree(t_tree):

        def del_known_from_tree(tre, pos):
            for i in pos:
                if i == '0':
                    tmp = tre.left
                if i == '1':
                    tmp = tre.right
            tmp = None
            print(tre.left.right.left.right)

        save_tree = t_tree
        while type(t_tree) == HaffmanTree:
            if t_tree.left:
                letter_code.append('0')
                t_tree = t_tree.left
            if t_tree.right:
                letter_code.append('1')
                t_tree = t_tree.right

        letter_dict[t_tree] = letter_code
        del_known_from_tree(save_tree, letter_code)
        return letter_dict


    letter_dict = {}
    # final_let_dict = []
    letter_code = []
    go_tree(fill_the_tree(letter_mult))
    # counted_tree = fill_the_tree(letter_mult)

    # tmp_dict = count_letter_from_tree(fill_the_tree(letter_mult))
    # final_let_dict = count_letter_from_tree(fill_the_tree(letter_mult))
    # final_let_dict.append(tmp_dict)

    print(len(final_let_dict))
    return final_let_dict


    # count_letter_from_tree(fill_the_tree(letter_mult))


print(haffman(inp_string))
