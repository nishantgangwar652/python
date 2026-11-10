# # range(5) #[0, 1, 2, 3, 4]

# nums = range(5)
# print(nums)

# # 1 to 5

# range(1, 6)


#  LOOPS

# # counter: 1, 2 , 3, 4 ,5 ,6

# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1

    
    # FOR LOOPS

# nums = range(5) # 0 to 4

# for i in nums:
#     print(i)

# 1 to 5

# for i in range(1, 6):
#     print(i)

# 1 to 10 => Even

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)



# Break $ continue statement

# # multiples of 3 [1 to 50] >= 21

# for i in range(1, 51):
#     if(i == 21):
#         break
#     if(i % 3 == 0):
#         print(i)

# print("out of loop")        


# multiples of 3 [1 to 50] >= 21 skip

for i in range(1, 51):
    if(i == 21):
        continue
    if(i % 3 == 0):
        print(i)

print("out of loop")    