lists = [1, 2, 3, 4,5,6]


print(lists[0:])
print(lists)

lists.append(10)
lists[2]=60
print(lists)

#clear list
lists.clear
# first digit defines position, the latter defines the value
lists.insert(2,65)
print(lists)
# enter the value to remove
lists.remove(65)
# removes according to the key
lists.pop(1)
lists.sort()
