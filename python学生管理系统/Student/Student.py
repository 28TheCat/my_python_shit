class Student:
    def __init__(self,no,name,chinese,math,english):
        self.no = no
        self.name = name
        self.chinese=int(chinese)
        self.math=int(math)
        self.english=int(english)

    def setNo(self,no):
        self.no=no

    def setName(self,name):
        self.name=name

    def setChinese(self,chinese):
        self.chinese=chinese

    def setMath(self,math):
        self.math=math

    def setEnglish(self,english):
        self.english=english

    def printStudent(self):
        print()