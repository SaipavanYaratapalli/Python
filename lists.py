#List Exercises:
#1) Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2)Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[1] = 'kiwi'
print(fruits)
#3)Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
print(fruits)
#4)Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,'lemon')
print(fruits)

#5)Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove('banana')
#del fruits[1]
print(fruits)
#6)Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7)Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(0,len(fruits)+1):
    if i in range(3,6):
        print(fruits[i])

#8)Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#9) List=[0,1,0,2,0,3] get output as [1,2,3,0,0,0]
lst=[0,1,0,2,0,3]
l1 = []
l2 = []
for i in lst:
    if i>0:
        l1.append(i)
    else:
        l2.append(i)
print(l1+l2)
#10) Remove duplicates fhrom list[1,2,3,4,1,2,3]
lst = [1,2,3,4,1,2,3]
l1 = list(set(lst)) # convert list to set so duplicated will be omitted
print(l1)
res = []    #m2
for i in lst:
    if i not in res:
        res.append(i)
print(res)

r1 = []     #m3
[r1.append(j) for j in lst if j not in r1]
print(r1)


#11) A = ['ABC',[],'XYZ',[],'abc',[]] --> program to get output ['ABC','XYZ','abc']
A = ['ABC',[],'XYZ',[],'abc',[]]
temp = []
for i in A:
    if i != []:
        temp.append(i)
print(temp)

'''#12)x=[20,50,10,5,99,39,11,6] --> Ascending and Descending 
#don't use sort method, sort the above list
#use the below concepts on List:

#remove --> List 
#append --> List
#operator <
#for loop 
#if condition class'''
x=[20,50,10,5,99,39,11,6]
for i in range(0,len(x)):       #Ascending order 
    for j in range(i+1,len(x)):
        if x[i]>= x[j]:
            x[i],x[j] = x[j],x[i]
print(x)

for i in range(0,len(x)):       #Decending order
    for j in range(i+1,len(x)):
        if x[i] <= x[j]:
            x[i],x[j]= x[j],x[i]

print(x)

#13) Python program to find largest number and second largest number in a list

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
large = 0
large2 = 0
for i in list1:
    if i > large:
        if large >large2:
            large2 = large
    large = i

print("largest number of list:" , large)
print("second largest number of the list:" , large2)

#14) Count occurance of an element in the list ex:8

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
print(lst.count(8))


#15) Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new = []
for i in range(0,min(len(list1),len(list2))):
    new.append(list1[i] + list2[i])
print(new)


#joining two strings indexwise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
final_list = []
for i in range(0,len(list1)):
    final_list.append(list1[i])
    final_list.append(list2[i])
print(final_list)
