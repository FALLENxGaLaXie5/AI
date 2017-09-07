# -*- coding: utf-8 -*-

#Spyder Editor

def fibonacci(x=10):
  seq = []
  if x==0:
    return seq
  elif x==1:
    seq.append(1)
    return seq
  else:
    seq = [1,1]
    for i in range(2,x):
      seq.append(seq[i-2] + seq[i-1])
    return seq
print (fibonacci(20))


#This is a temporary script file.


