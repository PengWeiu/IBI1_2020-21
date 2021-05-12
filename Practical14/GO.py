import re
from xml.dom.minidom import parse
import  xml.dom.minidom
dom = xml.dom.minidom.parse('go_obo.xml')
root = dom.documentElement
collect=root.getElementsByTagName('term')

#test DNA
numberDNA=0
for term in collect:
  defstr=term.getElementsByTagName('defstr')[0]
  is_a=term.getElementsByTagName('is_a')
  if re.search("DNA",(defstr.childNodes[0].data)):
    numberDNA+= is_a.length
print ('DNA:',numberDNA)

#test RNA
numberRNA=0
for term in collect:
  defstr=term.getElementsByTagName('defstr')[0]
  is_a=term.getElementsByTagName('is_a')
  if re.search("RNA",(defstr.childNodes[0].data)):
    numberRNA+= is_a.length
print ('RNA:',numberRNA)

#test Protein
numberProtein=0
for term in collect:
  defstr=term.getElementsByTagName('defstr')[0]
  is_a=term.getElementsByTagName('is_a')
  if re.search("protein",(defstr.childNodes[0].data)):
    numberProtein+= is_a.length
print ('Protein:',numberProtein)

#test Carbohydrate
numberCarbohydrate=0
for term in collect:
  defstr=term.getElementsByTagName('defstr')[0]
  is_a=term.getElementsByTagName('is_a')
  if re.search("carbohydrate",(defstr.childNodes[0].data)):
    numberCarbohydrate+= is_a.length
print ('Carbohydrate:',numberCarbohydrate)

#plot
import matplotlib.pyplot as plt
data={'DNA':numberDNA,'RNA':numberRNA,'Protein':numberProtein,'Carbohydrate':numberCarbohydrate}
labels=data.keys() 
sizes=data.values() 
explode=(0.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.title('GO comparision among DNA, RNA, Protein, Carbohydrate')
plt.axis('equal')
plt.show()
