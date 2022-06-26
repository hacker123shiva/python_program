# Dictionaries
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
# Dictionaries are used to store data values in key:value pairs  .
# A dictionary is a collection which is orderd* ,changeable and do not allow duplicates

#### NOTE: As of Python 3.7 , dictionaries are ordered .In Python 3.6 and earlier dictionaries are unorrderd

#Dictionaries are written with curly brackets , and have keys and values:


# Dictionary Items
"""
Dictionary items are orderd , changeable , and does not allow duplicates 
Dictionary items are presented in key: vlaue pairs , and can be referred to by using the key name.
"""
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict["brand"])

# Ordered or Unorderd
"""
>>As of python 3.7 , dictionaries are orderd . in python 3.6 and earlier dictioanries are unordeerd .
>>When we say that dictionaries are orderd , it means that the items have a defined 
order , and that order will not change.
>>Unorderd means that the items does not have a defined order  , you cannot refer toa  item by using an index

"""

#Changeable
"""
dictionaries are unchangeable , meaning that we can change , add or remove 
items after the dictionary has been created
"""
# Duplicates Not Allowed
">>Dictionaries cannot have two items with same key:"

">>Duplicate values will overwrite existing values:"
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}
print(thisdict)

# Dictionary Length
"To  determine the items in dictionary , use the len() function:"
print(len(thisdict))

# Dictionary items -Data Types
"The Values in dictionary items can be of any data type :"
thisdict={
    "brand":"ford",
    "electric":False,
     "year":1964,
      "colors":["red","white","blue"]
}


# type()
"From Python's perspective , dictionaries are defined as objects with data type 'dict' "
"<class 'dict'>"
print(type(thisdict))

#Accessing items
"""
you can access the items of a dictionary by refering to its key name , inside square brackets:

"""
thisdict={
    "member1":"Shiva",
    "member2":"Muskan",
    "member3":"Uday",
    "member4":"dheeraj",
    1:"sh"
}

print(thisdict)
print(thisdict[1])

"There is also a method called get() that will give you the same result:"
x=thisdict.get(1)
print(x)

# Get keys
print("get keys")
"The keys() method will return a list of all keys in the dictionary"
x=thisdict.keys()
print(x)
"""
The list of the keys is a view of the dictionary, meaning that any changes done to the 
dictionary will be reflected in the keys list
"""
member={
    "muskan":1,
    "Uday":2,
    "dheeraj":3,
    "shiva":4
}
x=member.keys()
print(x)
###Imp: "dict_keys" objects is not subscriptable hence we cannot get x.[0]

# Get Values
print("get values")

"The 'values()' method will return a list of all the values in the dictionary"

x=member.values()
print(x)
x=list(x)
print(x[0])
"We can change dict_keys or dict_values in list,tuple or set "
"""The list of the values is aview of the dictionary, meaning that any chnage " \
change  done to the dictionary will be reflected in the values list"""
this={1:1,2:2,3:3}
x=this.values()
y=this.values()
print(id(x),id(y),sep='\n')

# Get Items
print("\nget items")
"the items() method will return each item in a dictionary, as tuples in a list"
x=thisdict.items()
print(x)
"the returned list is a view of the items of the dictionary, meaning that any changes" \
"done to the dictionary will  be reflected in the items list"

# Check if Key Exists
"To determine if a specified key is present in a dictionary use 'in' keyword"
thisdict={
    "member1":"shiva",
    "member2":"muskan",
    "member3":"uday",
    "member4":"dheeraj"
}
if "member5" in thisdict:
    print("Yes , 'member5' is one of the key is thisdict")

    # Change Values
    "You can change the value of a specific item by referring to its key name"
thisdict={
    "brand":"Tata",
    "model":"Hero",
    "year": 2020
}
thisdict['year']=2022
print(thisdict['year'])
print(thisdict)
# Update Dictionary
"""
the update() method will update the dictionary with the items from the given argumnet
The argument must be a dictionary , or an iterable object with key:value pairs
"""
thisdict.update({"range":100000})
print(thisdict)

# Adding items
"""adding an item to the dictionary is done by using a new index key and assigning a value to it:"""
thisdict["color"]="Red"
print(thisdict)

# Update Dictionary
"""The update method will update the dictionary with the items from a
given argument. If the item does not exist, the item will be added
The argument must be a dictioanry, or an iterable  object with key:value pairs"""
thisdict.update({"age":20})

# Removing Items
"There are several methods to remove items from a dictionary"
"The pop() method removes  the item with the specified key name:"
thisdict.pop("model")
print(thisdict)

"the popitem() methode removes the last inserted item(in version  before 3.7, a random item is removed innstead): "
thisdict.popitem()
print(thisdict)

"the del keyword removes the item with the specified key name :"
del  thisdict['year']
print(thisdict)

# Imp: this  will cause an error because "thisdict" no longer exists.
del thisdict
# print(thisdict) Produce an error

"The clear() method empties the dictionary:"
thisdict={
    "brand":"tata",
    "model":"armour",
    "year":2000
}
thisdict.clear()
print(thisdict)

# Loop dictionaries

"""You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, 
but there are methods to return the values as well."""
thisdict={"shiva":4,"dheeraj":3,"uday":2,"muskan":1}
for  x in thisdict:
    print(x)

"print all values in the dictionary one by one"
for x in thisdict:
    print(thisdict[x])

"We can also use the values() method to return values of a dictionary:"
for x in thisdict.values():
    print(x)
"You can use the keys() method to return the keys of a dictionary:"
for x in thisdict.keys():
    print(x)
"Loop through both keys and values, by using the items() method:"
for x,y in thisdict.items():
    print(x,y)

# Copy a dictionary
"""You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, and changes made 
in dict1 will automatically also be made in dict2.
"""
"There are ways to make a copy, one way is  to use buit-in Dictionary method copy()"
"Make a copy of a dictionary with the copy() method:"
thisdict={1:[2,3,4],2:'shiva'}
mydict=thisdict.copy()
print(mydict)
print(id(mydict),id(thisdict),sep='\n')
print(id(mydict[1]),id(mydict[2]),id(thisdict[1]),id(thisdict[2]),sep='\n')
mydict[2]="muskan"
print(id(mydict[1]),id(mydict[2]),id(thisdict[1]),id(thisdict[2]),sep='\n')
mydict[1][0]=1
print(id(mydict[1]),id(mydict[2]),id(thisdict[1]),id(thisdict[2]),sep='\n')
"Another way to make a copy is to use the built-in function dict()"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# Nested Dictionaries
"A dictionary can contain dictionaries, this is called nested dictionaries"
mycollege={
    "btech":{
        "name":"shiva",
        "year":2025
    },
    "bba":{
        "name":"muskan",
        "year":2024
    },
    "ba":{
        "name":"uday",
        "year":2024,
    }
}
print(mycollege)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

# fromkeys()
"The fromkeys() method returns a dictionary with"
" the specified keys and the specified value."
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# setdefault()
"""The setdefault() method returns the value of the item with the specified key.

If the key does not exist, insert the key, with the specified value, see example below"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

print(car)
"""Get the value of the "color" item, if the "color" item
 does not exist, insert "color" with the value "white":
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
