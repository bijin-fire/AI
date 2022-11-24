import math
import matplotlib.pyplot as plt
import numpy as np


def max(a,b):
  if(a>=b):
    return a
  return b

def getMember(element):
  value = round( abs((10-element)/max(10,element)),4)
  if(value>1):
    return 0
  return 1-value



start = 0
end=20
count=100
diff = (end-start)/count

nums=list()
membership = list()
tempMember = list()

gama = [1,2,3,4,5]

temp=start

while(temp<end):
  nums.append(temp)
  temp = round((temp+diff),2)


for i in  nums:
  value = getMember(i)
  membership.append(value)

for i in gama:
  for j in membership:
    element = i*j
    tempMember.append(element)
  plt.plot(nums,tempMember)
  # print(np.shape(nums),np.shape(tempMember))
  # print(tempMember)
  
  plt.show()
  tempMember.clear()

