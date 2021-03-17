#imput two list
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,843,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#define the list of averge exon length
exon_lengths=[gene_lengths[0]/exon_counts[0]]
#calculate and add them into the list
for i in range (1,10):
  exon_lengths1=[gene_lengths[i]/exon_counts[i]]
  exon_lengths += exon_lengths1
  i=i+1

print (exon_lengths)
  
#add a plot
import numpy as np
import matplotlib.pyplot as plt
#input the score
score = exon_lengths
#make a plot
plt.boxplot(score, vert =True, whis = 1.5,patch_artist =True, meanline = True,showbox =True, showfliers =True, notch= True)
plt.show()
