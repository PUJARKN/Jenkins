import sys
import random

print(sys.version)

fruits = ['Banana ','Apple ',"pineapple"]

x,y,z = fruits

# print(x,y,z)
# print(x+y+z)

r = range(5)
#print(r)
# print(random.randrange(1,12))


st = "Hello, We are not there"

# print(st.strip())
#print(st)
#rint(st.split(" "))

txt = "so we are cllaed \"vikings\" from North"

#print(txt)

#print(bool({"K":453,"d":"Pujari"}))

# Python Operator 

d1 = 29
d2 = 7

#print(d1%d2)

def operators():
    if d1 > 23  and d2 > 10 :
        print("True1")
    elif d1 > 12 or d2 > 9 :
        print("True2")

#operators()

thislist1 = [ "Cherry","Apple","Banana" ,"banana","cherry","apple","banana" ,"banana",]
thistuple = ("kiwi", "orange")
thislist1.extend(thistuple)
#print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
#print(thislist)
thislist1.sort(key=str.lower)
#print(thislist1)

mydict = {"Company":"Tata",
          "Variant":"Pure" ,  
          "Model": "Punch"}

#print(mydict.get("Model"))
#print(mydict.keys())

mydict["Year"] = "2019"

#print(mydict.keys())

Child1 = { "Name":"Yudhishthir","Year":2024}
Child2 = { "Name":"Om","Year":2025}

myFamily = {"Pujari": Child1,"Swami": Child2,}


#print(myFamily["Swami"]["Year"])

for x,value in myFamily.items():
    print(x,value)
    for y in value:
        print(y +':',value[y]) 
