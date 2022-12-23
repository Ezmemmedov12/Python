import numpy as np
x=np.full((3,3),' ' )
def fun():
    for i in range (3):
      if x[i][0]==x[i][1]==x[i][2]!=' ' :
        print('The winner is: ',x[i][0])
    for j in range(3):
      if x[0][j]==x[1][j]==x[2][j]!=' ':
        print('The winner is: ',x[0][j])
    if x[0][0]==x[1][1]==x[2][2]!=' ':
      print('The winner is: ',x[0][0])
    elif x[0][2]==x[1][1]==x[2][0]!=' ':
      print('The winner is: ',x[0][2])
    return False

def fun2():
  i = (val1 - 1) // 3
  j = val1 % 3 - 1
  if x[i][j] == ' ':
    x[i][j] = val2
    print(x)
    fun()
  else:
    print('This position is full. Please enter another position: ')
while fun()==False:
    for i in range(1,999):
      if i%2==0:
        val1=int(input('Second player enter position: '))
        val2='o'
        fun2()
        break
      else:
        val1=int(input('First player enter position : '))
        val2='x'
        fun2()
      fun()
