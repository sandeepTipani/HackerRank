# Generating random lists and extracting common and distinct elements 

# for x in lista,listb results will not fetch correctly. Each object is taken differently


import random

#lista = random.sample(range(100),10);
#listb = random.sample(range(100),6);
lista  = [1,1,2,3,4,5,6,6,7];
listb  = [1,1,5,21,54,7];
result = [];
distinct = [];
for x in lista:
    if(x in listb): 
      if(x not in result):
         result.append(x)
print lista;
print listb;
print "Common elements in the list are:"; print result;

for y in lista:
    if(y not in listb):
      if(y not in distinct):
         distinct.append(y);

for y in listb:
    if(y not in lista):
      if(y not in distinct):
         distinct.append(y);

print "The distinct elements in each list are:"
print distinct;

print "Distinct Method 2:"

distinct2 = [];

dummy = lista + listb;

for x in dummy:
    if(x not in result):
      if ( x not in distinct2):
          distinct2.append(x);

print distinct2;