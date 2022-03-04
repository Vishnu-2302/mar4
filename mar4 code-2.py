n=int(input())
l=[]
t=input().split()
for i in t:
	l.append(int(i))
l2=[]
for i in l:
	if i not in l2:
		l2.append(i)
for i in l2:
	l.remove(i)
l3=[]
for i in l:
	if i not in l3:
		l3.append(i)
for i in l3:
	l2.remove(i)
l2.sort(reverse=True)
print(l2[1])