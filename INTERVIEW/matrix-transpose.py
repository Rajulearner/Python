matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#[[row[i] for row in matrix] for i in range(4)]
final=[]
for i in range(4):
    final.append([row[i] for row in matrix])
print(final)
    
