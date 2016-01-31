# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-lists
n = int(raw_input());
a = []
while (n>0):
    invalue = raw_input();
    count = len(invalue.split()); 
    command = invalue.split();
    if ((count > 2) and (command[0] == "insert")):
        a.insert(int(command[1]),int(command[2])); 
    elif ((count == 2) and (command[0] == "remove")):
        a.remove(int(command[1]));
    elif ((count == 2) and (command[0] == "append")):
        a.append(int(command[1]));
    elif ((count == 1) and (command[0] == "print")):
        print a;
    elif ((count == 1) and (command[0] == "sort")):
        a.sort();
    elif ((count == 1) and (command[0] == "reverse")):
        a.reverse();
    elif ((count == 1) and (command[0] == "pop")):
        a.pop();
    else:   
        print "Invalid Command";
    n = n-1;

    
    