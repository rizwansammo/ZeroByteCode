'''
Write Python code of a program that reads the radius of a circle and prints its circumference and area.
==========================================================
hint(1): import math and then use math.pi for getting the value of pi.
For details read from https://docs.python.org/3/library/math.html
hints(2): You can import math and use math function for making squares math.pow(number, power)
Or you can simply write using power opeartor. For example: S**2.
==========================================================
Example01:
Input: 4

Output:
Area is 50.26548245743669
Circumference is 25.132741228718345
==========================================================
Example02:
Input: 3.5

Output:
Area is 38.48451000647496
Circumference is 21.991148575128552
==========================================================
'''
#Code Starts from Here
import math
radius = float(input("please enter the radius value:"))

area=math.pi*radius**2
print('area=',area)
circumference=math.pi*2*radius
print('circumference=',circumference)