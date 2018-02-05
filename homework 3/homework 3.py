# task_1 

a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if a < b + c and b < a + c and c < a + b:
    print("True") 
else:
    print("False")

# task_2

number = int(input("Enter a number: "))
i = 0 
a = 0 
b = 1

while i < number:
    i+=1
    result = a + b
    a = b
    b = result

print(result)

    

    
