# 编写程序，实现用户输入数字，显示对应的英文
# 如输入“250”，显示 “two five zero”

import re

english_number ={0:'zero', 
                1:'one',
                2:'two',
                3:'three',
                4:'four',
                5:'five',
                6:'six',
                7:'seven',
                8:'eight',
                9:'nine',
                }


str = input('input a number:')
while not re.findall('^[0-9]+$', str):
    str = input('输入的参数必须为数字:')

print(str)

result = ''
for number in str:
    english = english_number.get(int(number))
    result = result+ english + ' '
print(result)    