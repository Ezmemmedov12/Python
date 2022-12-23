#random password generator
import random
len=int(input('Enter the length of password: '))
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
num = "0123456789"
symbol = "[]{}#()*;._-!@$%^+=`~"
all = lower + upper + num + symbol
rand = random.sample(all,len)
password = "".join(rand)
print(password)