class Student:
 studCount = 0
 def __init__(self,rollnumber,name):
  self.rollnumber = rollnumber
  self.name = name
  Student.studCount += 1
 def totalCount(self):
  print ("Total number of students are::", Student.studCount)
 def student(self):
  print ("Roll number ", self.rollnumber, "\nName: ", self.name)

stud1 = Student(2015115086,"Mani")
stud1.student()
stud2 = Student(2015115087,"Gopal")
stud2.student()
stud2.totalCount()
print ("Student count is",Student.studCount)
