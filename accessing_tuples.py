#exaple of accessing tuples 
thisistuple=('a','b','c','d','e','f')
print(thisistuple[0]) #get the first iteam in tuples 
print(thisistuple[-1]) #get the last iteams 
print(thisistuple[2:5]) # get range between 2 5 but it is not include 5 
print(thisistuple[2:0]) # get range starting from 2
print(thisistuple[:4]) # get range before 4 and not include 4
print(thisistuple[-4:-1])

if 'e' in thisistuple:
  print('e is in the tuple')
  
