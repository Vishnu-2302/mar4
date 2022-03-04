l=[]
l=input().split()
r=[]
for i in l:
	if i not in r:
		r.append(i)
print(len(l)-len(r))