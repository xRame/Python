n = int(input())
max = 1
l = []
for i in range(n):
	l.append(int(input()))
for i in range(0,n):
	for j in range(i+1,n):
		if max < (l[i]*l[j] ) and ((l[i]*l[j] )%26) == 0:
			max = (l[i]*l[j])
print(max)			