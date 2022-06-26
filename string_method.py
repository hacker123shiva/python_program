#capitalize()
str="Shiva is my Best friend"
str1=str.capitalize()
print( str1)
st="shiva"
print('CAPITALIZE',st.capitalize())
#casefold()
str2=str.casefold()
print(str2)
st="shiva  srivaStava"
print('CAEFOLD',st.casefold())

#uppercase
str3=str.upper()
print(str3)
st="shiva srivastava"
print('UPPERCASE',st.upper())
#casefold
str2=str3.casefold()
print('CASEFOLD',str2)

#lowercase
str4=str3.lower()
print('LOVERCASE',str4)

#center

str5=str4.center(40,"o")
print(str5)
st="shiva"*8
print(st.center(50,"_"))
#ljust
str="shiva is good boy"
str1=str.ljust(50,"@")
print(str1)

#rjust
str="shiva is good boy"
str1=str.rjust(50,"@")
print(str1)

#lstrip
str="shiva is good boy"
str1=str.lstrip("avb")
print(str1)
st="  shiva+srivasstava "
print(st.lstrip(" ").rstrip(" "))
#rstrip
str="shiva is good boy"
str1=str.rstrip("oy")
print(str1)

#count
str6=str3.count("S")
print(str6)
st="shiva srivastava"
print(st.count("s"))
#encode()
str="shiva is good  boy"
str1=str.encode(encoding='UTF-16',errors='strict')
print(str1)
st="shiva srivastava"
st=st.encode(encoding='UTF-16',errors='strict')
print(st)
#endswith()
str2=str.endswith("boy")
print(str2)
st="shiva srivastava is emotional fool boy"
print(st.endswith("fool"))


#expandtabs()
str="shiva is best friend"
str1=str.expandtabs(40)
print(str1)



#FIND
str1=str.find("si")
print(str1)

#isalnum
str1=str.isalnum()
print(str1)

#isalpha

str1=str.isalpha()
print(str1)

#isdecimal

str1=str.isdecimal()
print(str1)

#isidentifier
str="shiva_12"
str1=str.isidentifier()
print(str1)

#islower
str="shiva"
str1=str.islower()
print(str1)

#isnumeric
str="123434"
str1=str.isnumeric()
print(str1)

#isprintable
str="\nshiva"
str1=str.isprintable()
print(str1)

#isspace
str="    "
str1=str.isspace()
print(str1)

#istitle
str="Shiva Is Good Boy"
str1=str.istitle()
print(str1)

#isupper
str="SHIVA IS "
str1=str.isupper()
print(str1)

#join
str="shiva srivastava"
str1=str.join("harsh")
print(str1)

#replace
str="shiva srivastava is a student of gla university"
str1=str.replace("is","are")
print(str)
print(str1)

# join
str="shiva  srivastava"
str=str.join(["hello","bye"])
print(str)

# split
str="shivasrivastava_harshsrivastava_kumarsingh"
str=str.split("_")
print(str)
