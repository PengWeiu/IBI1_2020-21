import os
import re
os.chdir("/Users/彭伟昱/PycharmProjects/pythonProject1")
unknown=open('unknown_function.fa','r') #open and read the file
lines=unknown.readlines()

codetable={'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
 'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
 'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
 'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
 'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
 'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
 'TAT':'Y','TAC':'Y','TAA':'Y','TAG':'U',
 'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
 'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
 'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
 'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
 'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
 'AGT':'S','AGC':'S','AGA':'A','AGG':'R',
 'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}

unknown_protein=[]
for i in range(0,len(lines)):
  if lines[i].startswith('>'):
    unknown_protein.append(lines[i]) #find and add the name of unknown function DNA in the list
  elif lines[i].startswith('Length'):
    continue #skip the length line
  else:
    protein=''
    line=lines[i].strip()
    line=line.replace('.','')
    for u in range(0,len(line),3):
     if line[u:u+3] != "TAA" or "TAG" or "TGA":
      protein+=codetable[line[u:u+3]]
     else:
      break
    protein+='\n'
    unknown_protein.append(protein)#find and add the sequence of unknown function protein in the list

for i in range(len(unknown_protein)):
     m=unknown_protein[i]
     if m.startswith('>'): #find, calculate and add the length of protein in the list
        unknown_protein[i] = re.findall(r'>.+?',unknown_protein[i])[0]
        length=str(len(unknown_protein[i+1])-1)
        unknown_protein[i]+='\n Length:'
        unknown_protein[i]+=length
        unknown_protein[i]+='.\n'

unknown_DNA_to_protein=open('DNA_protein.fa','w') #add the context of list in the file 
for line in unknown_protein:
 unknown_DNA_to_protein.write(line)
unknown_DNA_to_protein.close()
