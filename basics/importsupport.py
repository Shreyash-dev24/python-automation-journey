import sys 
sys.path.append('C:/Users/Shreyash/Desktop')

from my_module import *  

courses = ['History','Art','Physics','Compsci']

index = find(courses,'Art')
print(index)