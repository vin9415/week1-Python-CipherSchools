# ask a user for name 
# Example -- > Sumit Goswami
# print count of each words
# output:
        # S : 1
        # u : 1
        # m : 2
        # i : 2
        # t : 1
        #   :  
        # G : 1

'''name = input("")
   a = name.count("s")
   print(a)
'''

# name = input("")
# i = 0
# while i < len(name):
#     print(name[i] ,":" ,name.count(name[i]))
#     # print(f"{name[i]} : {name.count(name[i])}")
#     i = i+1   # i += 1

## if we run this code , like sumit goswami, sooo here it count "s" two time ,and give their count in the string,for that we can do some changes in the above code

name = input("")
temp_var = " "
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(name[i] ,":" ,name.count(name[i]))
    # print(f"{name[i]} : {name.count(name[i])}")
    i = i+1   # i += 1


'''now it will give count chr once it,so this is right method we can say'''    

    
        





