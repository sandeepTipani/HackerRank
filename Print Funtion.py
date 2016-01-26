#https://www.hackerrank.com/challenges/python-print
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

num = int(raw_input());
i =1;
result ="";
while True:
     if (i > num): break;
     result = result + str(i);
     i=i+1;
        
print (result,sep="");        