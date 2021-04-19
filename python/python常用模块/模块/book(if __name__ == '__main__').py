
# //! 在其他模块中如果引入了本文件，不想看到调试print 日志信息，可以加上 if __name__ == '__main__' 这个判断

class Book:
    book_name = 'test python'

    def __init__(self, author):
        self.author = author
    
    def get_author(self):
        return self.author    

def new_book():
    return 'book.py--python test... '


print('__name__:', __name__)

if __name__ == '__main__':
    book = Book('test')
    author = book.get_author()
    print('book.py--author->:', author)

    published = new_book()
    print('book.py--published->:', published)

