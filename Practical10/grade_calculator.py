class Student():
 def __init__(self,name,code,poster,final): #initialize the class
  self.name=name
  self.code=code
  self.poster=poster
  self.final=final
 def grade(self):  #define a function to calculate and output the grade
  grades=self.poster*0.3+self.final*0.3+self.code*0.4
  print (self.name,' ','Grade:',grades)

#example
A=Student('Julie',98,90,90)
A.grade()
