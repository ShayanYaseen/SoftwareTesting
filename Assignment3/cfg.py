import numpy as np                  #import numpy
import matplotlib.pyplot as plt     #import Matplotlib
import networkx as nx               #import networkx
my_obj = open("test.py","r")       #created an object to open a file
cif = 0								#count for if
cfor = 0							#count for for
k = 0								#initializing variable to store number of nodes
for line in my_obj:
    subif = "if"					#sub string if
    subfor = "for"					#sub string for
    cif = line.count(subif) + cif	#number of if(s)	
    cfor = line.count(subfor) + cfor#number of for(s)
c = cfor + cif    					
k = k + 3*cif
k = k + 3*cfor
mat = np.zeros((k,k))				#initializing zero matrix
cur = 0								#current node
while (c>0):
	
	ex = cur + 1					#exit node
	nxt = ex + 1					#next node
	mat[cur][ex] = 1				#writing in matrix
	mat[cur][nxt] = 1
	mat[nxt][ex] = 1
	cur = nxt +1
	c = c-1
	if (c>0):
		mat[ex][cur] = 1
print("adjacency matrix")		
print(mat)							#printing Adjecency matrix
ed = []								#edges list
for i in range(k):
	for j in range(k):
		if(mat[i][j] ==1):
			x = i,j
			ed.append(x)
print("Edges are")			
print(ed)							#printing number of edges
G = nx.Graph()						#creating graph
G.add_edges_from(ed)				#adding nodes in Graph
num = 0								
print("Independent paths are :")		
for path in nx.all_simple_paths(G, source=0, target=k-1):
	print(path)						#printing paths one by one
	num = num+1
print("number of independent paths are :",num)
Bounded_regions = num - 1
print("Number of bounded regions are :",Bounded_regions)   #Number of bounded regions
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()							#ploting CFG
print("Program Over...")			
my_obj.close()						#closing file