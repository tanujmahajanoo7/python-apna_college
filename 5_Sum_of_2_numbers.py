first = input("Enter first number: ")
second = input("Enter second number: ")
sum = int(first) + int(second)                # type cvonversion is important for addition of 2 numbers 
print(sum)


#same codes in two different ways


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# type conversion is importaant

sum = (first) + (second)  
print("the sum is : "+ str(sum))          #concatination will not done with with onw string and one int (error) so str is used 
#                                         ................print("the sum is : "+ sum).................