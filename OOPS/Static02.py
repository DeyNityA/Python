class Student:
     __counter = 0
     __studentlist = list()

     def __init__(self, name, age):
          self.__name = name
          self.__age = age
          Student.__counter += 1
          Student.__studentlist.append(self)

     @property
     def email(self) :
          return f"{self.__name}@gmail.com"

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
st1.set_name("guuuu")

print(st1.email)
print(Student._Student__counter)

Student.get_all_students()