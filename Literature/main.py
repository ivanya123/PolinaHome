# -*- coding: utf-8 -*-
from Literature.class_literature import Literature

if __name__ == '__main__':
    string = 'start'
    while string != 'end':
        final_string = ''
        string = ''
        print('Input BibTex')
        while string != '}':
            string = input()
            final_string = final_string + '\n' + string

        literature = Literature(final_string)
        with open('Gost.txt', 'a') as f:
            f.write(literature.gost_literature()+'\n')
        print(f'Записалось в файл Gost.txt\n{literature.gost_literature()}\nПродолжите ввод для выхода введите end')
        string = input()
