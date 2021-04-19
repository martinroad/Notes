# encoding=utf-8

class Book:
    def __init__(self, year):
        if str(year) == '2020':
            self.book = 'ABC Mouse'
        else:
            self.book = 'Python Test'

    def get_book_name(self):
        return self.book            