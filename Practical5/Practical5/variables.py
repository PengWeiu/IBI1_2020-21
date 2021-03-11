#3.1
a=270302
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d>e:
  print("d>e")
elif d<e:
  print("d<e")
else:
  print("d=e")

#3.2
X=True
Y=False
Z=(X and not Y) or (Y and not X)
if Z==True:
  print "Z is True"
else:
  print "Z is False"
W=(X!=Y)
if Z is not W:
  print("Z is not as same as W")
else:
  print("Z is as same as W")
