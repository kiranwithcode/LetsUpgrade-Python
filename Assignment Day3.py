# Question 1
# You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
# 1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
# the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
# later”
num=int(input("Enter Number:"))
if num<1000:
    print("Land The Plane")
elif num==1000:
    print("Safe To Land")
elif num==4500:
    print("Bring Down To 1000")
elif num==6500:
    print("Turn Around")
else:
    pass

# Output:
# Enter Number:100
# Land The Plane

# Enter Number:1000
# Safe To Land

# Enter Number:4500
# Bring Down To 1000

# Enter Number:6500
# Turn Around




# Question 2
# Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
# function.
num=1
l=[]
for i in range(num,201):
    if i%2!=0:
        l.append(i)
print(l)

# OutPut:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
#  53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101,
#  103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 
#  143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 
#  183, 185, 187, 189, 191, 193, 195, 197, 199]
    
        

    
