'''
Write Python code of a program that reads two numbers from the user.
Your program should then print "First is greater" if the first number is greater,
"Second is greater" if the second number is greater,
and "The numbers are equal" otherwise.
==========================================================
Example:
Input:
-4
-4

Output:
The numbers are equal
==========================================================
Example:
Input:
-40
-4

Output:
Second is greater
'''
#Code Starts From Here
a=int(input('enter a number'))
b=int(input('enter another number'))
if (a>b):
            print('First is greater')
elif (b>a):
            print('Second is greater')
else:
            print('The numbers are equal')