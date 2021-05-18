import os
import re
os.chdir("/Users/彭伟昱/PycharmProjects/pythonProject1")
function=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') #open and read the file
lines=function.readlines()
unknown_function=[]

for i in range(len(lines)):
  if re.findall('unknown function',lines[i]):
    name=re.search(r'(>.+?)(?:_| )',lines[i])#find and add the name of unknown function DNA in the list
    name=name.group()
    name=name.replace('_','')
    unknown_function.append(name)

    sequence=''
    preseq=''
    sequence+='\n'
    for x in range(len(lines[i:len(lines)])):
        if lines[i+x+1].startswith('>'):
            break
        else:
            preseq+=lines[i+x+1]#find and add the sequence of unknown function DNA in the list
    sequence+=preseq.replace('\n','')
    unknown_function.append(sequence)


    length=''
    unknown_function.append(length)
dictionary={}
for i in range(len(unknown_function)):
     m=unknown_function[i]
     if m.startswith('>'):
        length=str(len(unknown_function[i+1])-1)#calculate and add the length of unknown function DNA in the list
        unknown_function[i]+='\nLength:'
        unknown_function[i]+=length
        unknown_function[i+2]+='.\n'

unknown=open('unknown_function.fa','w') #add the context of the list'unknown_function' into the file
for i in unknown_function: 
 n=str(i)
 m=str(n)
 unknown.write(m)
unknown.close()
