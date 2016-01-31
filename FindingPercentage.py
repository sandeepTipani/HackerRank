# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/finding-the-percentage
n = int(raw_input());
a = {}
while (n>0):
    invalue = raw_input();
    name,m1,m2,m3 = invalue.split(); 
    m1i = float(m1);
    m2i = float(m2);
    m3i = float(m3);
    a[name] = (m1i+m2i+m3i)/3;         
    n = n-1;
find =  raw_input();

if (find in a):
   print "%.2f" %a[find]; 

    
    