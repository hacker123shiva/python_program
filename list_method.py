# list are used to store multiple items in a single variable
lst=["apple","banana","cherry"]
print(lst)
# List items are ordered , changeable, and allow duplicate values
lst=["apple","banana","cherry","apple","cherry"]
print(lst)
# List length
lst=["apple","banana","cherry"]
print(len(lst))
# List items can be any data types
list1=["apples","banana","cherry"]
print(list1)
list2=[1,5,7,9,3]
print(list2)
list3=[True,False,None]
print(list3)
# A list can have differnt data types
list4=["shiva",19e2,374]
print(list4)
# list() constructor
lst=list(("apple","banana","cherry"))
print(lst)
lst=list("shiva")
"""There are four collection data types in python programming language
List: is a collection which is ordered and changeable.Allows duplicate
Tuple:is a collection which is ordered and unchangeable .Allows duplicate members
Set:is a collection which is unordered ,unchangeable* and unindexed .No
duplicate members.
Dictionary:is a collection which is orderd** and changeable.No duplicate 
members
"""
"""*Set items are unchangeable , but you can remove and /or add items 
whenever you like 
** As of python version 3.7 ,dictionaries are orderd .In Python 3.6 and earlier
dictionaries and unordered"""

"""When choosing a collection type , it is useful to  understand the properties
of that data types.Choosing the right type for a particular data set could 
mean retention of meaning , and ,it could mean an increase in efficiency
 or security."""
# Access Items
lst=['apple','banana','cherry']
print(lst[1])

# Negative Indexing
"""  
Negative indexing means start from the end 
-1 refers to the lat item , -2 refers to the second last item etc.
"""

# Range of Indexes
""">>> when we can specify a range of indexes by specifying wher to 
start and where to end the range
   >>> When specifying a range , the return value will be a new list 
   with the specified items
   """
lst=["apple","banana","cherry","orange","kiwi","melon","melon"]
print(lst.append("shiva"),lst ,sep="\n")
print(lst ,lst.append("harsh")  ,sep="\n")
print(lst,lst[2:5],sep="\n")

# Range of negative Indexes
"""specify negative indexes if you want to start the search from the 
end of the list """
lst=["shiva","uday","dheeraj","muskan","ritika","mohit"]
print(lst)

# Check if Item Exists
"""To determine if a specified item is present in a list use 'in' keyword:
"""
lst=["apple","banana","cherry"]
if "apple" in lst:
    print("yes, 'apple is in fruits list")
# Change item Value
"""
To change the value of a specific item , refer to the index number
"""
lst=["apple","banana","cherry"]
lst[1]="guava"
print(lst)

# Change a Range of Items Values
"""
To change the vlaue of items within a soecific range , define a list
with new values,and refer to  the range of index numbers where you want to inssert
the new value:"""
print("Change a Range of Items Values")
lst=["apple","banana","cherry","orange","kiwi","mango"]
lst[1:3]=["guava","litchi"]
print(lst)

""" if you insert more items than you replace, the new items will be
inserted where specified, and the remaining items move accordingly"""
lst=["apple","banana","cherry"]
lst[1:2]=["guava","mango"]
print(lst)
""" if you insert less items than you replace, the new items will be 
inserted where you specified , and the remaing items will move accordingly
"""
lst=["shiva","harsh","arsh"]
lst[1:3]=["babu"]
print(lst)
# Insert items
"""To insert a new item, without replacing any of the existing values ,
we can use the insert() method
"""
# insert items
lst=["shiva","harsh","aarsh"]
lst.insert(1,"muskan")
print(lst)

# Append Items
lst=["shiva","harsh","uday"]
lst.append("muskan")
print(lst)

# Extend Items
lst1=["shiva","muskan","uday","dheeraj"]
lst2=["anik","ayush","mansi","divyanshi"]
lst1.extend(lst2)
print(lst1)

# Add Any Iterable
"""The extend() method does not have to append lists, you can add any iterable object 
(tuples, sets, dictionaries etc.)."""
lst=["shiva","harsh"]
tup=("kiwi","orange")
lst.extend(tup)
print(lst)

#Remove element
## lst.remove()
lst=["shiva","muskan","uday","dheeraj","ritika"]
lst.remove("ritika")
print(lst)

## lst.pop()
lst=["shiva","muskan","uday","dheeraj","ritika"]
lst.pop()
print(lst)
lst.pop(3)
print(lst)

## delfunction
lst=["shiva","muskan","uday","dheeraj","ritika"]
del lst[4]
print(lst)

## lst.clear()
lst=["shiva","muskan","uday","dheeraj","ritika"]
lst.clear()
print(lst)

#Loop list
## for and while

# List comprehension
# #List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# ordinary way of creating list
lst=["shiva","harsh","babu","arsh"]
new_list=[]
for x in lst:
    if "a" in x:
        new_list.append(x)
print(new_list)
# using list comprehenstion
lst=["shiva","harsh","babu","arsh"]
new_list=[x for x in lst if "a" in x]
print(new_list)
# newlist = [expression for item in iterable if condition == True]
newlist = [x if x != "banana" else "orange" for x in lst]
newlist = ['hello' for x in lst]
newlist = [x.upper() for x in lst]
newlist = [x for x in range(10) if x < 5]
newlist = [x for x in range(10)]
newlist = [x for x in lst]
newlist = [x for x in lst if x != "apple"]

# Sorting
lst=[2,1,34,3,0,9]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
lst.reverse()

print(lst)

## sorted function
lst=[2,12,4,5,0,44]
res=sorted(lst,reverse=True)
print(res)

# Copy List
lst1=["shiva","muskan","uday","dheeraj"]
lst2=lst1
print("using assignment")
print(id(lst1),id(lst2),lst1,lst2)

lst2=lst1.copy()
print("Uing copy method of list")
print(id(lst1),id(lst2),lst1,lst2)

lst2=list(lst1)
print("usig list function")
print(id(lst1),id(lst2),lst1,lst2)

import copy
lst2=copy.deepcopy(lst1)
print("using deepcopy")
print(id(lst1),id(lst2),lst1,lst2)

# join list
lst1=["shiva","uday","dheeraj","uday"]
lst2=["anik","mansi","ayush","divyanshi"]
print(lst1,id(lst1))
lst1=lst1+lst2
print(lst1,id(lst1))

## using extend()

lst1=["shiva","uday","dheeraj","uday"]
lst2=["anik","mansi","ayush","divyanshi"]
print(lst1,id(lst1))
lst1.extend(lst2)
print(lst1,id(lst1))

lst=["shiva","harsh","muskan","ananya"]
lst_new=lst
print(id(lst[1]),id(lst),id(lst_new[1]))
lst[1]=2
print(id(lst[1]),id(lst),id(lst_new[1]))
lst1=["shiva","uday","dheeraj","uday",[1,2,3]]
lst2=lst1.copy()
print("Uing copy method of list")
print(id(lst1),id(lst2),lst1,lst2)
print(id(lst1[4]),id(lst2[4]))
a=[1,2,3]
a[:]=1,2,3,4
print(a)
#a[::3]=1,2,3,4 #attempt to assign sequence of size 4 to extended slice of size 1
print(a)
