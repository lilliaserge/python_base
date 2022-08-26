s = input()
l = s.split()
n = len(l)
for i in range(n//2):
print(l[2*i+1], l[2*i], end=' ')
if n%2==1:
print(l[-1])
