list1 = [1,2,3, "uzair", 2.5, True]
print(list1)
print(type(list1))

list2=[1,2,3,4,5,6,7,8,9]
print(list2[-5])


print(list2[2:7])
print(list2[2:6])
print(list2[2:])
print(list2[-7:-2])
print(list2[-2:-7])
print(list2[:4])


#append(insert at last) and insert(insert at specific index)
list2.append("uzair")
print(list2)

list2.insert(3, "lgu")
print(list2)

#list extend 
list3=['a', 'b']
list3.extend(list2)
print(list3)


#extend at specific index
a=[1,2,3,4,5]
b=['a', 'b', 'c']
b.extend(a[:4])
print(b)

#extend a list with tuple
tuple1=("a",36)
a.extend(tuple1)
print(a)

#remove function
list1.remove("uzair")
print(list1)

#class task

#list
list4=[1,2,3,"uzair"]
print(list4)

#tuple
tuple1=(4,5,6,7,8)

#extend with tuple
list4.extend(tuple1)
print(list4)

#remove
list4.remove(6)
print(list4)

#set written with curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset)
#set length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print(type(thisset))

#dictionary 
thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

#dictionary with duplicate values
thisdict =	{"brand": "Ford",
             "model": "Mustang",
             "year": 1964,
             "year": 2018}
print(thisdict)

#print the brand value of the dictionary
thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])

 