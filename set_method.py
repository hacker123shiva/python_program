# Sets
"""
Sets are used to store multiple items in a single variable
>>Set is one of 4 built -in data types in python used to store collections of data
the others 3 are list ,tuples and Dictionary all with differnt qualities  and usage

>>A Set is a collection which is unordered , unchangeable* and unindexed
Note : set items are unchanged , but you can remove items and add any items

"""

"""
Sets are writeen  with curly brackets
"""
thisset={"shiva","muskan" ,"uday","dheeraj"}
print(thisset)

# Sets are unorderd , so you canot be sure in which order the items will appear

# Sets items are unorderd , unchangeable , and do not allow duplicate  values
# Unorderd
"""
Unorderd means that the items in a set do not have a defined order 
Set items can appear in a differnt order every time you use them , and cannot be refered to by indexx or key

"""

# Unchangeable
"""
>>Set items are unchangeable , meaning that we cannot change items afte the set ]
has been created 
>>Once a set is created , you cannot change its items and add new items
"""

# Duplicates Not Allow
"""
>>Sets cannot have two items with the same value
>>Duplicate values be ignored
"""

thisset={"shiva","muskan","uday","dheeraj","shiva",'muskan'}
print(thisset)

# Get the Length of a Set
"""
To determine how many items a set has , use the len() function
"""
thisset={"shiva","musakn","uday","dheeraj"}
print(len(thisset))

# Set Items -Data Types
"""
set items can be of any data types
"""
set1={"shiva","muskan"}
set2={1,2,3,4,5}
set3={True,False,None}
set4={(2,3),(3,4)}
print(set1)
print(set2)
print(set3)
print(set4)
"""
unhashable type
 
set5={{"a":"shiva","b":"muskan","c":"uday","d":"dheeraj"},{1:"sh"}}
set6={[1,2,3],['e','t']}
 
print(set5)
print(set6)"""

# type()
"""
>>From Python's perspective, sets are defined as objects with the data type 'set'
<class 'set'>

"""
myset={"shiva","muskan","uday","dheeraj"}
print(type(myset))

# The set() Constructor
"It is also possible to use the set() constructor to make a set."

myset=set(("shiva","muskan","uday","dheeraj"))
print(myset)
"""
There are four collection data types in the Python programming language:

>>List is a collection which is ordered and changeable. Allows duplicate members.
>>Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
>>Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
>>Dictionary is a collection which is ordered** and changeable. No duplicate members.

>>>>*Set items are unchangeable, but you can remove items and add new items.

>>>>**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

# Access Items
"""
>>You cannot access items in a set by referring to an index or a key.
>>But you can loop through the set items using a for loop, or
 ask if a specified value is present in a set, by using the in keyword
"""

myset={"shiva","muskan","uday","dheeraj"}
for x in myset:
    print(x)

print("shiva" in myset)
# Change Items

# # Add Set items
print("--------------Add set items-------------------")
"Once a set is created, you cannot change its items, but you can add new items"
"To add one item to a set use the add() method"

myset={'shiva',"uday",'dheeraj',"muskan"}
print(id(myset))
myset.add("ritika")
print(id(myset))


print(myset)
myset1={"shiva","muskan","uday","dheeraj"}
myset2={"Anilk","Ayush","Mansi","Divyanshi"}
print(id(myset1))
myset1.update(myset2)
print(id(myset1))
set1={'shiva','muskan'}
print(id(set1))
set2={'anik','ayush'}
set1.update(set2)
print(set1,id(set1))



# Add Any Iterable
print('---------------Add any Iterable------------------------')
"""
The object in the update() methods does not have to  be a set , it can 
be any iterable object (tuples ,lists , dictionaries etc)
"""
sett={12,13,14}
set1={1,2,3,4}
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
dict1={'a':1,'b':2,'c':3}
print(set(set1))
print(set(list1))
print(set(tuple1))
print(set(dict1))
sett.update(set1)
print(sett)
sett.update(list1)
print(sett)
sett.update(tuple1)
print(sett)
sett.update(dict1)
print(sett)

# Remove item

"To remove an item in a set , use the remove() or the discard() method"
print("remove")
## using remove()
myset={"shiva","muskan","uday","dheeraj","ritika"}
print(id(myset))
myset.remove("ritika")
print(myset,id(myset))
"Note: If the item to remove does not exist, remove() will raise an error."
# myset.remove("ritika") give error

myset.add("ritika")
print(myset)
## using discard
myset.discard("ritika")
print(myset)
st1={"shiva,muskan,kusam"}
print(st1.discard("kusam"))
"Note: If the item to remove does not exist, discard() will NOT raise an error."
# myset.discard("ritika")  not raise an error
print(myset)

myset.add("ritika")
"""
>>You can also use the pop() method to remove an item, 
but this method will remove the last item.
>>Remember that sets are unordered, so you will not know what item 
 that gets removed.
>>The return value of the pop() method is the removed item.
"""
myset.pop()
print(myset)

# clear()
"The clear() method empties the set"
myset.clear()
print(myset)

# del keyword
"The del keyword will delete the set completely"
myset={"shiva","muskan","dheeraj","uday"}
del myset
# print(myset) give error since myset not exist

# Loop Sets
"Loop Items"
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Python -Join Sets
# # Join two Sets
"""
There are several ways to join two or more sets in python 
You  can use the union() method that returns a new set containing all items 
from both sets, or the update() method that inserts all the items from one set into 
another:
"""
# Union Method
"The union() method returns a new set with all items from both sets:"
set1={"shiva","muskan","uday","dheeraj"}
set2={"anik","ayush","mansi","ritika"}
set3=set1.union(set2)
print(set1,set2,set3)

# update() method
set1={"shiva","muskan",'uday',"dheeraj"}
set2={"anik","ayush","mansi","divyanshi"}
set3=set1.update(set2)
print(set1,set3)

"Note: Both union() and update() will exclude any duplicate items."

# intersection_update()
"""
The intersection_update() method will
 keep only the items that are present in both sets.
"""
"st.intersection_intersection"
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(id(x))
x.intersection_update(y)
print(x,id(x))

# intersection()
"""
The intersection() method will return a new set,
 that only contains the items that are present in both sets
 
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

x={"love","hate","satisfaction"}
y={"satisfaction","positive approach"}
z=x.intersection(y)
print(z)

# Keep all, But NOt the Duplicates

"The symmetric_difference_update() method  will keep  only the elements that " \
"are NOT present in both sets"
print("symmetric_differnce_update()")
myset={"shiva","muskan","uday","dheeraj","ritika","divyanshi"}
myset2={"anik","ayush","mansi","ritika","divyanshi"}
myset.symmetric_difference_update(myset2)
print(myset)

# symmetric_difference()
"""
The symmetric_difference() method will return a new set, 
that contains only the elements that are NOT present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

"""
Python has a set of built-in methods that you can use on sets.

Method	                       Description
add()	                     Adds an element to the set
clear()	                      Removes all the elements from the set
copy()	                     Returns a copy of the set
difference()	               Returns a set containing the difference between two or more sets
difference_update()           	Removes the items in this set that are also included in another, specified set
discard()	           Remove the specified item
intersection()	         Returns a set, that is the intersection of two other sets
intersection_update()	         Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	         Returns whether two sets have a intersection or not
issubset()	           Returns whether another set contains this set or not
issuperset()	       Returns whether this set contains another set or not
pop()	                   Removes an element from the set
remove()	                Removes the specified element
symmetric_difference()	    Returns a set with the symmetric differences of two sets
symmetric_difference_update()	 inserts the symmetric differences from this set and another
union()	                         Return a set containing the union of sets
update()	                  Update the set with the union of this set and others
"""




st1={"shiva","muskan","dheeraj","uday","ritika","jew"}
st2={"anik","ayush","mansi","jew"}
st_1=st1^st2   #symmetric differnce
st_2=st1|st2   #union
st_3=st1-st2   #differnce
st_4=st1&st2   #Intersection
print(st_1)
print(st_2)
print(st_4)
print(st_3)
st1.symmetric_difference_update(st2)
print(st1)
