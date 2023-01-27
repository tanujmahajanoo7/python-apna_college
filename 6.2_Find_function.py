name = "Tony Stark"

print("S is present on the location : ")
print(name.find('S'))                       # s is capital

print("s is not present so : ")
print(name.find('s'))                       # s is small

print("Stark is present on the location : ")
print(name.find('Stark'))                   # s is capital

print("Stark is present on the location : ")
print(name.find('stark'))                   # s is small
# Insdexing start from 0th position

print(name.replace("Tony Stark","Ironman")) #replacing string

print(name.replace("T","M"))                 #replacing letter

print("T" in name)                           #searching letter

