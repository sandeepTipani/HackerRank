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
	 print "Ebbeyyy Uhuuu!!";  
      else: 
               print "You have done it my byoyyy, No of tries",count;
               break;	


   
