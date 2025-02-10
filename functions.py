#1) a) Write a function to find maximum of two numbers in Python

def max_of_two_numbers(a,b):
   if a>b:
      return a
   else:
      return b
k = max_of_two_numbers(10,11)
print(k)

#b) Use inbuilt function to find maximum of two numbers 
print(max(10,15))
#c) find maximum of two numbers using Lambda function
j = lambda x,y: x if x>y else y
print(j(12,13))

#2) 
list_1 = [1,2,3,4,5,6,7,8,9]
 #--> Generate a list of even number from above sample using lambda\
f= lambda x : True if x%2 == 0 else False
f1 = filter(f, list_1)
print(list(f1))

 #--> Generate a list with square of each number in the above sample using lambda
sq = lambda x : x*x
sq1 = list(map(sq,list_1))
print(sq1)

#3) program to multiply all values in the list using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
mul1 = lambda x,y : x*y
mul2 = reduce(mul1,list1)
print(mul2)