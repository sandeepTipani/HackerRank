# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-tuples
import __builtin__

N = int(raw_input());
T = tuple(map(int,raw_input().split()));
print hash(T);