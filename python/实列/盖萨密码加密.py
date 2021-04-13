'''
盖萨密码它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推
利用 “凯撒密码” 方案，实现对用户输入文字的加密操作
'''

letter = input('Please input an English letter:')
n = 3
pwd = ord(letter) + n  # ord函数将输入的字母转换成ACSII码
new_letter = chr(pwd) # chr将ASCII码转换成字母
print('new_letter=>', new_letter)
