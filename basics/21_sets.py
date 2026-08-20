# numbers = {10, 20, 30, 20, 10}
# print(numbers)


# fruits = {"apple", "banana", "mango"}
# fruits.add("orange")
# print(fruits)


# numbers.add(40)
# print(numbers)

# fruits.remove("banana")
# print(fruits)

# fruits.discard("orange")


languages  = {"pyhton", "java", "go", "python"}
print(languages)
languages.remove("java")
print(languages)
languages.add("linux")
print(languages)

#set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


fruits = {"apple", "banana", "mango"}
print("apple" in fruits)
print("orange" in fruits)

if "banana" in fruits:
    print("banana is avaliable")
if "apple" in fruits:
    print("apple is avaliable")
if "orange" not in fruits:
    print("orange is not avaliable")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.difference(b))
print(a.intersection(b))
print(a.union(b))