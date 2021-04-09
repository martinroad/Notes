
# 实现对输入字符串的大小写字母翻转（即大写变小写、小写变大写）
word = input('please input an Eglish string:')
new_list =[]
for i in word:
    if i.islower():
        new_list.append(i.upper())
    else:
        new_list.append(i.lower())

print ('new_list=>', new_list)   
new_word = "".join(new_list)
print ('new_list=>', new_word)    # 将列表转换成字符串      
