import numpy as np
import matplotlib.pyplot as plt

array = [[0.5,-1.1,0.24,-0.22,-1.8],[0.15,-1.4,0.11,-0.28,-0.3],[0.1,-1.4,0.11,0.6,-1.11]]
desired=[1,-1,1]

x = np.array(array)

weight = [0.1, 0.17,0.2,-1.1, -0.4]

output = []

c =1 
p = 0

def signum(y):
    if(y>0): y=1
    elif(y<0): y=-1
    return y
list=[]
a=100
while(desired!=output):
    a=0
    output=[]

    for i in range(3):
        y = 0
        

        for j in range(len(x[i])):
            y = y + x[i][j]*weight[j]
        
        y=signum(y)
        
        output.append(y)
        weight = weight + c*(desired[i]-y)*x[i]
        
        print("List Output",weight,output)
        a+=desired[i]-y
    
    p=p+1
    
    print("\n{} epoch {}\n".format(p,output))

    print(a)
    # print("Error is ")
    list.append(a)

print(list)
plt.plot(list)
