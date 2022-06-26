#Tuple
mtuple=("apple","banana","cherry")
# A tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets
print(mtuple)
# Tuple Items
## Tuple items are ordered, unchangeable, and allow duplicate values
##Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
##When we say that tuples are ordered, it  means that the items have a defined order, and that order will not change

# Unchangeable
##Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow Duplicates
##Since tuples are indexed, they can have items with the same value:
thistuple=("shiva","muskan","muskan","uday","harsh","shiva")
print(thistuple)

# Tuple length
##To determine how many items a tuple has ,use the len() function:

#Create Tuple With One Item
''' To create a tuple with only one item , you have to add a comma after the item,
otherwise python will not recognize it as a tuple '''
thistuple=("shiva",)
print(type(thistuple))

# Tuple Items -Data Types
##Tuple items can be OF any data type:

tuple1=("apple","banana","cherry")
tuple2=(1,5,7,9,3)
tuple3=(True,True,False)
##Atuple can contain differnt data types:
tuple4=("shiva",3,True,3.4)
tuple1=("abc",34,True,40,"male")

# type()
##From python perspective ,tuples are defined as objects with data 'tuple'
#The Tuple Constructor
##It is also possible to use the tuple() constructor to make a tuple
thistuple=tuple()
print(thistuple)

thistuple=()
print(thistuple)

#Access Tuple Items
##You can access tuple items by referring to the index number, inside square brackets:
thistuple=("shiva","muskan","uday","dheeraj")
print(thistuple[1])

# Negativ Indexing
##Negative indexing means start from the end
## -1 refers to the last item ,-2 refers to the second last item etc
thistuple=("shiva","muskan","uday","dheeeraj")
print(thistuple[-1])

# Range of Indexes
## You can specify a range of indexes by specifying where to start and where to end the range.
## When specifying a range, the return value will be a new tuple with the specified items

thistuple=("shiva","muskan","uday","dheeraj")
print(thistuple[1:3])
##Note: The search will start at index 2 (included) and end at index 5 (not included)
##By leaving out the start value, the range will start at the first item:
thistuple=("shiva","muskan","uday","dheeraj","mohit","ritika")
print(thistuple[:4])
##By leaving out the end value, the range will go on to the end of the list:
thistuple=("shiva","uday","muskan","dheeraj")
print(thistuple[2:])

# update Tuples
##Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created

#Change Tuple Values
##Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called
###But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
lst=["shiva","muskan","uday","dheeraj","muskan","shiva","shiva",8]
lst=set(lst)
lst=list(lst)
print(lst)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items
'''Since tuples are immutable ,they do not have a a buillod -in append() method ,but
there are other ways to add items to a tupel
!. Conver i ntoa list : Hist lijhe the owekatoind for chanhinf a ru ple yoi  can  comvert it inti a list , 
add uour items an d connveru it vavk irnto a tupele
'''
thistuple=("shiva","banana","sour")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

'''Add tuple to a tuple You are allowed  to add  tuples to tuples , so if you want 
to add one items ,(or many) ,create a new tuple woth the items(s
,and add  it to the existing tuple:'''

thistuple=("shiva","muskan","uday","dheeraj")
y=("mohit",)
thistuple+=y
print(thistuple)

y=list(thistuple)
y.append("ritika")
thistuple=tuple(y)
print(thistuple)
# RemoveItems
## You cannot remove items in a tuple
'''Tuples are unchangeable , so you cannot remove items from it , but you
can use the same workaround as we used for changing and adding tuple items:'''

thistuple=("shiva","muskan",'uday',"dheeraj")
y=list(thistuple)
y.remove("dheeraj")
thistuple=tuple(y)

#del keyword can delete the tuple completely
thistuple=("shiva","muskan","uday","dheeraj")
del thistuple
# print(thistuple)#this will raise an error because the tuple no longer exists

# Unpack  Tuples
## Unpacking a Tuple
'''When we create a tuple  , we normally assign values to it . This is called 
"packing" a  tuple'''
# Packing
thistuple=("shiva","muskan","uday")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list

"""

# Using Asterisk *
"""
If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned 
to the variable as a list:
"""
thistuple=("shiva","muskan","uday","dheeraj")
(a,b,*c)=thistuple
print(a)
print(b)
print(c)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

"""If the asterisk is added to another variable name than the last, 
Python will assign values to the variable until the number of values 
left matches the number of variables left.
"""

# Join Tuples
##To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# Multiply Tuples
thistuple=("shiva","harsh","uday","muskan")
thistuple=thistuple*3
print(thistuple)

counting=thistuple.count("shiva")
print(counting)

ind=thistuple.index("shiva")
print(ind)
lst=list(thistuple)
lst.remove("shiva")
print(lst)
lst.append("shiva")
print(lst)
lst.pop()
print(lst)
