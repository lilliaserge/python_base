k = input()
s = k.split()
n = len(s)
for i in range(n):
if len(s[i])<=10:
print(i+1,s[i])
else:
print(i+1, s[i][:10])
