import array as arr

values = arr.array("i",[1,2,3,4,5,6])

print(f"The length of values is {values}")

print(values.reverse)
print(values)
values.reverse
print(values)

a = arr.array("i",[])

inputs = int(input("enter the length of the array \n"))
for i in range(inputs):
    numbers = int(input(f"enter number {i} \nS"))
    a.append(numbers)

for i in range(inputs):
    print(i)