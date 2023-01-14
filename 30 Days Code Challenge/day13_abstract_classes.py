from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    """
    Task:
    Given a Book class and a Solution class,
    write a MyBook class that does the following:
    - Inherits from Book
    - Has a parameterized constructor taking these 3 parameters:
        1. string title
        2. string author
        3. int price
    - Implements the Book class' abstract display() method so it prints these 3 lines:
        1. Title:, a space, and then the current instance's .
        2. Author:, a space, and then the current instance's .
        3. Price:, a space, and then the current instance's .
    """
    def __init__(self,
                title : str,
                author : str,
                price : int):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: {}\nAuthor: {}\nPrice: {}"\
                .format(self.title,
                        self.author,
                        self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()