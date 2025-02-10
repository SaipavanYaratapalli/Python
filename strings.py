
#Strings Exercise:
#1)Write a program to find all occurrences of “USA” in a given string ignoring the case.
Str = "Welcome to USA. usa awesome, isn't it?"
new_str = Str.lower()
print(new_str.count('usa'))


#2)Calculate the sum and average of the digits present in a string.
Str="hi156hello890"
sum1 = 0
count = 0
for i in Str:
    if i.isdigit():
        sum1+= int(i) 
        count+=1
print('sum is',sum1)
if count >0:
    average = sum1/count
else:
    average = 0
print(' is avg',average)

#3)Write a program to count occurrences of Characters within a string
str1 = "Apple"
count = 0
for i in str1:
    if i.isalnum():
        count+=1
    else:
        count+=0
if count>0:
    print('no of chars is', count)
else:
    print('print no chars found')

#4)Reverse a given string -- using slicing
Str1='Apple'
print(str1[::-1].lower())
#5)Split a string on hyphens
str1 = 'Emma-IS-a-data-scientist'
print(str1.split('-'))

#6)Count all chars, digits and symbols in a string
str1 = "P@#yn26at^&i5ve"
count = 0
for i in str1:
    count+=1

print(count)