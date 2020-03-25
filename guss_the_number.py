import random
help = input("please help me :)")
hads = random.randint(1, 100)
print (hads)
temp_b = 100
temp_k = 1

while help != "d":
    if help == "b":
        temp_k = hads + 1
        hads = random.randint(temp_k, temp_b)
    else:
        temp_b = hads - 1
        hads = random.randint(temp_k, temp_b)
        
    print ("the computer guss is: ",hads)
    help = input("please help me :)")

print ("damet garm computer!!!")