class Student:
     __counter = 0
     __studentlist = list()

     def __init__(self, name, age):
          self.__name = name
          self.__age = age
          Student.__counter += 1
          Student.__studentlist.append(self)

     def set_name(self, name):
          self.__name = name

     def get_name(self):
          return self.__name

     def set_age(self, age):
          self.__age = age

     def get_age(self):
          return self.__age

     @classmethod
     def get_all_students(cls):
          print("Total no of students :- ", cls.__counter)
          for std in cls.__studentlist :
              print(std.__name, " -> ", std.__age)


st1 = Student("Hero", 13)
st2 = Student("Zero", 56)

Student.get_all_students()