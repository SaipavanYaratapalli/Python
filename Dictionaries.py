#Dictionary Exercise:
#1)Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get('model','not found'))

#2)Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['year'] = 2020
print(car)

#3)Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['color'] = 'red'
print(car)

#4)Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop('model')
print(car)

#5)Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

#6) What is the output for the below
dictt = {i : i+2 for i in range(10)}  
print(dictt)
#7)print sum of all values from a dict
dict = {'a': 100, 'b': 200, 'c': 300}
sum = 0
for i,j in dict.items():
    sum += j
print(sum)
#8) dict={1:2,"adic":{"key":"val"},"role":"sse"} --> program to get output adic
dict={1:2,"adic":{"key":"val"},"role":"sse"}
m = list(dict.keys())[1]
print(m)

#9) Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {}
for i in range(0,min(len(keys),len(values))):
    dict[keys[i]] = values[i]

print(dict)
    
