#Simple Calculator
from math import sin,cos
print(' 1.Add \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Power \n 6.Percentage of number \n 7.Sin(x) \n 8.Cos(x)')
ent=int(input('Select operation: '))
val1=int(input('Enter the first number: '))
val2=int(input('Enter the second number: '))
while True:
  if ent==1:
    add=val1+val2
    print('Equal:',add)
  elif ent==2:
    sub=val1-val2
    print('Equal:',sub)
  elif ent==3:
    mult=val1*val2
    print('Equal:',mult)
  elif ent==4:
    div=val1/val2
    print('Equal:',div)
  elif ent==5:
    pow=val1**val2
    print('Equal:',pow)
  elif ent==6:
    per=val1*val2/100
    print('Equal:',per)
  elif ent==7:
    x=int(input('Enter the x: '))
    sin=sin(x)
    print('Equal:',sin) 
  elif ent==8:
    x=int(input('Enter the x: '))
    cos=cos(x)
    print('Equal:',cos)  
  break
else:
  print('Invalid input')