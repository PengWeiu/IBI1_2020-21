#Python fibonacci,py
#print n1 n2 first
n1=1
n2=1
print (n1)
print (n2)
#n3=n1+n2 n4=n2+n3 ... n13=n11+n12
for i in range(3,14):
#n1=1 n2=1 let n1 and n2 be assigned
 n=n1+n2
 n1=n2
 n2=n
#print n3 n4 ......n13
print (n)
 i=i+1
