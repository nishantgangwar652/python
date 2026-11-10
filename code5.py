# List

# marks = [98, 97, 99,76, 'A', 99.2]

# print(marks, type(marks))

# length

# print(len(marks))

#index

# print(marks[0])
# print(marks[2])
# print(marks[-1])


# # slicing a list -list[st:end]
# print(marks[:2]) 



# marks.append(70)
# print(marks)

# Tuple - immutable

# marks = (98, 99, 97, 95, 93, 95, 95)

# print(marks.index(95))


# set => unique items  collection

# marks = {98, 97, 95, 96, 95, 96}
# print(len(marks), marks) # 4

# for score in marks:
#     print(score)


# Dictionary {key => val}

marks = {"math": 99, "physics": 97, "chemistry": 98}
# print(marks, type(marks))
for key in marks:
    print(key, marks[key])