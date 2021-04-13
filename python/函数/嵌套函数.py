# coding=utf-8

def book(name):
    return "the name of my book is {0}".format(name)

def p_deco(func):
    def warpper(name):
        return "<p>{0}</p>".format(func(name))
    return warpper

test_func = p_deco(book)
reuslt = test_func("~python~")
print(reuslt)
