from xml.dom.minidom import parse
import  xml.dom.minidom
dom = xml.dom.minidom.parse('go_obo.xml') #open and read the xml file
root = dom.documentElement #get the root of xml
terms=root.getElementsByTagName('term') #get the elements with tagname 'term'

#define a function to find all the ids of terms
def id_find(terms):
  dict={} #creat a dictionary to store all of the ids of terms
  for term in terms:
   all_id = term.getElementsByTagName('id')[0].childNodes[0].data
   is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
   for id_a1 in is_a:
      if id_a1 in dict:
         dict[id_a1].append(all_id)
      else:
         dict[id_a1]=[all_id]
  return dict

#define a function to find the specific defstr in terms
def get_terms(terms,macromolecule):
  gene=[]
  for term in terms:
    defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
    id=term.getElementsByTagName('id')[0].childNodes[0].data
    if not macromolecule.isupper():
       defstr=defstr.lower()   #aviod case sensitivity
    if macromolecule in defstr:
       gene.append(id)
  return set(gene) #aviod repeating

#define a function to find all the childnodes
def findnodes(dict,lists):
  nodes=[]
  for i in lists:
    if i in dict:
       nodes+=dict[i]
       nodes+=findnodes(dict,dict[i])
  return nodes

#define a function to calculate the childnodes
def number(terms,macromolecule):
  dict=id_find(terms)
  m=get_terms(terms,macromolecule)
  n=findnodes(dict,m)
  number=len(set(n))
  return number

#test DNA
numberDNA= number(terms,'DNA')
print ('DNA:',numberDNA)
#test RNA
numberRNA= number(terms,'RNA')
print ('RNA:',numberRNA)

#test Protein
numberProtein= number(terms,'protein')
print ('Protein:',numberProtein)

#test Carbohydrate
numberCarbohydrate=number(terms,'carbohydrate')
print ('Carbohydrate:',numberCarbohydrate)

#make a pie plot
import matplotlib.pyplot as plt
data={'DNA':numberDNA,'RNA':numberRNA,'Protein':numberProtein,'Carbohydrate':numberCarbohydrate}
labels=data.keys()
sizes=data.values()
explode=(0.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.title('GO comparision among DNA, RNA, Protein, Carbohydrate')
plt.axis('equal')
plt.show()
