#the infection is incremented with the rate of 1.2
n=84
r=1.2
for i in range(1,6):
#five times means n*(1+r)**5
 m=n*(1+r)**i
 i=i+1
#output the result
print ("the r rate is ",str(r),"and the total number of individuals infected after 5 generations is",str(m))
