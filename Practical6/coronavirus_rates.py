#input data to the dictionary
coronavirus_infection={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print (coronavirus_infection)
#add a plot
import matplotlib.pyplot as plt
labels=coronavirus_infection.keys() #determine the labels
sizes=coronavirus_infection.values() #determine the sizes
explode=(0.1,0,0,0,0)
#make the plot
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.title('coronavirus infection rate in different countries')
plt.axis('equal')
plt.show()
