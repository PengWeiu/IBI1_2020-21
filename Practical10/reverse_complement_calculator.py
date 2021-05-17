def reverse_caculator(DNA):
 DNA=DNA.upper() #make it possible to read any input sequence with case insensitive
 DNA_complement='' #get the complementary sequence
 for i in range(0,len(DNA)):
  if DNA[i]=='A':
   DNA_complement+='T'
  elif DNA[i]=='T':
   DNA_complement+='A'
  elif DNA[i]=='G':
   DNA_complement+='C'
  elif DNA[i]=='C':
   DNA_complement+='G'
 result=DNA_complement[::-1] #reverse the complementary sequence 
 return  print (result)

#example
reverse_caculator('AtGcGCA')

