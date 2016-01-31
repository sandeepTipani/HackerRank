# Guess game

import random;

guess = 0;
num  = 0;
count = 0;

num = random.randint(1,9);

while (guess!= num and guess!="quit"):
      guess = input("Guess the number:" );
      count = count + 1;	
      if (guess > num or guess < num): 
	 print "Better Luck next time!!";  
      else: 
               print "You have done it, No of tries",count;
               break;	


   
