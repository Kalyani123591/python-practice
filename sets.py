#add an item using add()
fruits= {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)

#add multiple items using update()
fruits.update(["cherry", "berry"])
print(fruits)

#remove an item using remove()
fruits.remove("banana")
print(fruits)

#clear all items
fruits.clear()
print(fruits)

#SET Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)                 #union

print(A & B)                #intersection

print(A - B)                #difference

print(A ^ B)                #symmetric

C = {1, 2}
print(C.issubset(A))         #subset

print(A.issuperset(C))       #superset

