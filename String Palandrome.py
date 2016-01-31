# Program to find whether a given string is palindrome or not

intext = input("Enter the text: ");

if(intext == intext[::-1]):
  print "The given text is palindrome";
else:
  print "The given text is Not a palindrome";

num = len(intext);

result = "";
while True:
      result = result + intext[num-1];  
      num=num-1;
      if (num == 0): break;

print "String is palindrome" if (intext == result) else "String is not palindrome";

