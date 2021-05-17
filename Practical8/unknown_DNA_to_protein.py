import re
DNA=input()
seq=open(str(DNA),'r')
lines=sequence.readlines()

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

for i in range(len(lines)):
  if re.findall('unknown function',lines[i]):
    name=re.search(r'(>.+?)_',lines[i])
    unknown_protein[i]+='Name:'
    unknown_protein[i]+=name.group()
    unknown_protein.append(name)

    sequence=''
    code=''
    sequence+='\n'
    for x in range(len(lines[i:len(lines)])):
        if lines[i+x+1].startswith('>'):
            break
        else:
            code+=str(lines[i+x+1])
    code=re.split(r'([ATCG]{3})',lines)
for i in code:
 if i == "":
  code.remove(i)
protein=''
for i in code:
 if codetable[i]=="Y":
   break
 else:
    protein+= codetable[i]

    sequence+=preseq.replace('\n','')
    unknown_protein.append(sequence)

    length=''
    unknown_protein.append(length)
dictionary={}
for i in range(len(unknown_function)):
     m=unknown_protein[i]
     if m.startswith('>'):
        length=str(len(unknown_function[i+1])-1)
        unknown_protein[i+2]+='\n Length: '
        unknown_protein[i+2]+=length
        unknown_protein[i+2]+='.\n\n'
        dictionary[unknown_protein[i]]=unknown_function[i+1:i+2]
unknown_protein.append(length)
unknown=open('DNA_protein.fa','w')
for i in unknown_protein:
 n=str(i)
 m=str(n)
 unknown.write(m)
unknown.close()