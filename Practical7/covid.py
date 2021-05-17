import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/彭伟昱/PycharmProjects/pythonProject1/Practical7") #open the file
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:11:2,:])
print (covid_data.loc[(covid_data.loc[:,"location"] == "Afghanistan"),"total_cases"])

#print(covid_data.loc[(covid_data.loc[:,"location"] == "World"), "new_cases"].mean())
#print(covid_data.loc[(covid_data.loc[:,"location"] == "World"), "new_cases"].median())

a=np.array(covid_data.loc[(covid_data.loc[:,"location"] == "World"),"new_cases"])
b=np.mean(a) #get the mean
c=np.median(a) #get the median
print (b)
print (c)

#creat a boxplot of new cases worldwide
worldnewcases = covid_data.loc[(covid_data.loc[:,"location"] == "World"),"new_cases"]
score1 = worldnewcases
color = ['pink']
plt.title("new cases worldwide")
plt.xlabel("world")
plt.ylabel("new cases") 
plt.boxplot(score1,notch= False, vert = True,whis=1.5, patch_artist = True, meanline = True, showbox = True, showcaps= True,showfliers= True)
plt.show()

#creat a plot of new cases and new deaths worldwide
worldnewdeaths = covid_data.loc[(covid_data.loc[:,"location"] == "World"),"new_deaths"]
plt.title("the plot of world new cases and world new deaths")
plt.xlabel("world new cases")
plt.ylabel("world new deaths")
plt.plot(worldnewcases,worldnewdeaths,'b+')
plt.show()

#question code
Spainnewcases = covid_data.loc[(covid_data.loc[:,"location"] == "Spain"),"new_cases"]
Spaintotalcases = covid_data.loc[(covid_data.loc[:,"location"] == "Spain"),"total_cases"]
time = covid_data.loc[(covid_data.loc[:,"location"] == "Spain"), "date"]
plt.title("new cases and total cases developed over time in Spain")
plt.xlabel("time")
plt.ylabel("cases")
plt.plot(time,Spainnewcases,'r+')
plt.plot(time,Spaintotalcases,'b+')
plt.legend(['Spainnewcases','Spaintotalcases'],loc='upper left')
plt.show()
