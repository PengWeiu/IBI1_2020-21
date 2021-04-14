class Student():
 def __init__(self,name,code,poster,final):
  self.name=name
  self.code=code
  self.poster=poster
  self.final=final
 def grade(self):
  grades=self.poster*0.3+self.final*0.3+self.code*0.4
  print (self.name,' ','Grade:',grades)

#example
A=Student('Julie',98,90,90)
A.grade()
