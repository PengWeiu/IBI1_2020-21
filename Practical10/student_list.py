class Student():
#initialize the class
 def __init__(self,first_name,last_name,undergraduate_programme): 
  self.first_name=first_name
  self.last_name=last_name
  self.undergraduate_programme=undergraduate_programme

#define a function to output student list
 def stu(self): 
  return print ('full name:',self.first_name,'',self.last_name,'    ','programe:',self.undergraduate_programme)

#example
A=Student('Weiyu','Peng','BMS')
A.stu()
