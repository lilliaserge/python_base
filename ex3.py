n=int(input())
m=['зима', 'весна', 'лето', 'осень']
if n<=2 or n==12:
  print(m[0])
  if n>2 and n<=5:
    print(m[1])
    if n>5 and n<=8:
      print(m[2])
      if n>8 and n<=11:
        print (m[3])
